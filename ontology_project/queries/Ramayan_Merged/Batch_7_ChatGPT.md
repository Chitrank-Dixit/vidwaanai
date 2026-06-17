# Merged Batch 7 (Files 97-112)
# Assigned Agent: ChatGPT



--- Start of Ramayan_batch_97.md ---

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



--- End of Ramayan_batch_97.md ---


--- Start of Ramayan_batch_98.md ---

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

### Verse 1 (Ramayan 0.1941)
- **Original**: Credits March 18, 2008 Project Gutenberg TEI edition 1 Produced by Juliet Sutherland, John Bruno Hare, David King, and the Online Distributed Proofreading Team at <http://www.pgdp.net/>. Page-images available at <http://www.pgdp.net/projects/projectID3e283e798085a/>
- **Translation**: 

---

### Verse 2 (Ramayan 0.1942)
- **Original**: A Word from Project Gutenberg This file should be named 24869-pdf.pdf or 24869-pdf.zip. This and all associated files of various formats will be found in: http://www.gutenberg.org/dirs/2/4/8/6/24869/ Updated editions will replace the previous one— the old editions will be renamed. Creating the works from public domain print editions means that no one owns a United States copyright in these works, so the Foundation (and you!) can copy and distribute it in the United States without permission and without paying copyright royalties. Special rules, set forth in the General Terms of Use part of this license, apply to copying and distributing Project Gutenberg™ electronic works to protect the Project Gutenberg™ concept and trademark. Project Gutenberg is a registered trademark, and may not be used if you charge for the eBooks, unless you receive specific permission. If you do not charge anything for copies of this eBook, complying with the rules is very easy. You may use this eBook for nearly any purpose such as creation of deriva- tive works, reports, performances and research. They may be modified and printed and given away— you may do practically anythingwith public domain eBooks. Redistribution is subject to the trademark license, especially commercial redistribution.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1943)
- **Original**: The Full Project Gutenberg License Please read this before you distribute or use this work. To protect the Project Gutenberg™ mission of promoting the free distribution of electronic works, by using or distributing this work (or any other work associated in any way with the phrase “Project Gutenberg”), you agree to comply with all the terms of the Full Project Gutenberg™ License (available with this file or online at http://www.gutenberg.org/license). Section 1. General Terms of Use & Redistributing Project Gutenberg™ electronic works 1.A. By reading or using any part of this Project Gutenberg™ elec- tronic work, you indicate that you have read, understand, agree to and accept all the terms of this license and intellectual property (trademark/copyright) agreement. If you do not agree to abide by all the terms of this agreement, you must cease using and return or destroy all copies of Project Gutenberg™ electronic works in your possession. If you paid a fee for obtaining a copy of or access to a Project Gutenberg™ electronic work and you do not agree to be bound by the terms of this agreement, you may obtain a refund from the person or entity to whom you paid the fee as set forth in paragraph 1.E.8.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1944)
- **Original**: The Full Project Gutenberg License 1929 1.B. “Project Gutenberg” is a registered trademark. It may only be used on or associated in any way with an electronic work by people who agree to be bound by the terms of this agreement. There are a few things that you can do with most Project Guten- berg™ electronic works even without complying with the full terms of this agreement. See paragraph 1.C below. There are a lot of things you can do with Project Gutenberg™ electronic works if you follow the terms of this agreement and help preserve free future access to Project Gutenberg™ electronic works. See paragraph 1.E below. 1.C. The Project Gutenberg Literary Archive Foundation (“the Foun- dation” or PGLAF), owns a compilation copyright in the col- lection of Project Gutenberg™ electronic works. Nearly all the individual works in the collection are in the public domain in the United States. If an individual work is in the public domain in the United States and you are located in the United States, we do not claim a right to prevent you from copying, distributing, performing, displaying or creating derivative works based on the work as long as all references to Project Gutenberg are removed. Of course, we hope that you will support the Project Gutenberg™ mission of promoting free access to electronic works by freely sharing Project Gutenberg™ works in compliance with the terms of this agreement for keeping the Project Gutenberg™ name associated with the work. You can easily comply with the terms of this agreement by keeping this work in the same format with its attached full Project Gutenberg™ License when you share it without charge with others.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1945)
- **Original**: 1930 The Ramayana 1.D. The copyright laws of the place where you are located also govern what you can do with this work. Copyright laws in most countries are in a constant state of change. If you are outside the United States, check the laws of your country in addition to the terms of this agreement before downloading, copying, displaying, performing, distributing or creating derivative works based on this work or any other Project Gutenberg™ work. The Foundation makes no representations concerning the copyright status of any work in any country outside the United States. 1.E. Unless you have removed all references to Project Gutenberg: 1.E.1. The following sentence, with active links to, or other immediate access to, the full Project Gutenberg™ License must appear prominently whenever any copy of a Project Gutenberg™ work (any work on which the phrase“Project Gutenberg” appears, or with which the phrase“Project Gutenberg” is associated) is accessed, displayed, performed, viewed, copied or distributed: This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at http://www.gutenberg.org 1.E.2.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1946)
- **Original**: The Full Project Gutenberg License 1931 If an individual Project Gutenberg™ electronic work is derived from the public domain (does not contain a notice indicating that it is posted with permission of the copyright holder), the work can be copied and distributed to anyone in the United States without paying any fees or charges. If you are redistributing or providing access to a work with the phrase“Project Gutenberg” associated with or appearing on the work, you must comply either with the requirements of paragraphs 1.E.1 through 1.E.7 or obtain permission for the use of the work and the Project Gutenberg™ trademark as set forth in paragraphs 1.E.8 or 1.E.9. 1.E.3. If an individual Project Gutenberg™ electronic work is posted with the permission of the copyright holder, your use and dis- tribution must comply with both paragraphs 1.E.1 through 1.E.7 and any additional terms imposed by the copyright holder. Ad- ditional terms will be linked to the Project Gutenberg™ License for all works posted with the permission of the copyright holder found at the beginning of this work. 1.E.4. Do not unlink or detach or remove the full Project Gutenberg™ License terms from this work, or any files containing a part of this work or any other work associated with Project Gutenberg™ . 1.E.5. Do not copy, display, perform, distribute or redistribute this electronic work, or any part of this electronic work, without prominently displaying the sentence set forth in paragraph 1.E.1
- **Translation**: 

---

### Verse 7 (Ramayan 0.1947)
- **Original**: 1932 The Ramayana with active links or immediate access to the full terms of the Project Gutenberg™ License. 1.E.6. You may convert to and distribute this work in any binary, compressed, marked up, nonproprietary or proprietary form, in- cluding any word processing or hypertext form. However, if you provide access to or distribute copies of a Project Gutenberg™ work in a format other than“Plain Vanilla ASCII” or other format used in the official version posted on the official Project Gutenberg™ web site (http://www.gutenberg.org), you must, at no additional cost, fee or expense to the user, provide a copy, a means of exporting a copy, or a means of obtaining a copy upon request, of the work in its original“Plain Vanilla ASCII” or other form. Any alternate format must include the full Project Gutenberg™ License as specified in paragraph 1.E.1. 1.E.7. Do not charge a fee for access to, viewing, displaying, per- forming, copying or distributing any Project Gutenberg™ works unless you comply with paragraph 1.E.8 or 1.E.9. 1.E.8. You may charge a reasonable fee for copies of or providing access to or distributing Project Gutenberg™ electronic works provided that • You pay a royalty fee of 20% of the gross profits you derive from the use of Project Gutenberg™ works calculated using the method you already use to calculate your applicable tax- es. The fee is owed to the owner of the Project Gutenberg™
- **Translation**: 

---

### Verse 8 (Ramayan 0.1948)
- **Original**: The Full Project Gutenberg License 1933 trademark, but he has agreed to donate royalties under this paragraph to the Project Gutenberg Literary Archive Foun- dation. Royalty payments must be paid within 60 days following each date on which you prepare (or are legally required to prepare) your periodic tax returns. Royalty payments should be clearly marked as such and sent to the Project Gutenberg Literary Archive Foundation at the ad- dress specified in Section 4,“Information about donations to the Project Gutenberg Literary Archive Foundation.” You provide a full refund of any money paid by a user who notifies you in writing (or by e-mail) within 30 days of receipt that s/he does not agree to the terms of the full Project Gutenberg™ License. You must require such a user to return or destroy all copies of the works possessed in a physical medium and discontinue all use of and all access to other copies of Project Gutenberg™ works. You provide, in accordance with paragraph 1.F.3, a full refund of any money paid for a work or a replacement copy, if a defect in the electronic work is discovered and reported to you within 90 days of receipt of the work. You comply with all other terms of this agreement for free distribution of Project Gutenberg™ works. 1.E.9. If you wish to charge a fee or distribute a Project Gutenberg™ electronic work or group of works on different terms than are set forth in this agreement, you must obtain permission in writing from both the Project Gutenberg Literary Archive Foundation and Michael Hart, the owner of the Project Gutenberg™ trademark. Contact the Foundation as set forth in Section 3 below. 1.F.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1949)
- **Original**: 1934 The Ramayana 1.F.1. Project Gutenberg volunteers and employees expend consider- able effort to identify, do copyright research on, transcribe and proofread public domain works in creating the Project Guten- berg™ collection. Despite these efforts, Project Gutenberg™ electronic works, and the medium on which they may be stored, may contain“Defects,” such as, but not limited to, incomplete, inaccurate or corrupt data, transcription errors, a copyright or other intellectual property infringement, a defective or damaged disk or other medium, a computer virus, or computer codes that damage or cannot be read by your equipment. 1.F.2. LIMITED WARRANTY, DISCLAIMER OF DAMAGES — Except for the“Right of Replacement or Refund” described in paragraph 1.F.3, the Project Gutenberg Literary Archive Foun- dation, the owner of the Project Gutenberg™ trademark, and any other party distributing a Project Gutenberg™ electronic work under this agreement, disclaim all liability to you for damages, costs and expenses, including legal fees. YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE PROVIDED IN PARAGRAPH F3. YOU AGREE THAT THE FOUNDATION, THE TRADE- MARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE LIABLE TO YOU FOR AC- TUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH DAMAGE. 1.F.3.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1950)
- **Original**: The Full Project Gutenberg License 1935 LIMITED RIGHT OF REPLACEMENT OR REFUND — If you discover a defect in this electronic work within 90 days of receiving it, you can receive a refund of the money (if any) you paid for it by sending a written explanation to the person you received the work from. If you received the work on a physical medium, you must return the medium with your written explanation. The person or entity that provided you with the defective work may elect to provide a replacement copy in lieu of a refund. If you received the work electronically, the person or entity providing it to you may choose to give you a second opportunity to receive the work electronically in lieu of a refund. If the second copy is also defective, you may demand a refund in writing without further opportunities to fix the problem. 1.F.4. Except for the limited right of replacement or refund set forth in paragraph 1.F.3, this work is provided to you 'AS-IS,' WITH NO OTHER WARRANTIES OF ANY KIND, EXPRESS OR IM- PLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTIBILITY OR FITNESS FOR ANY PURPOSE. 1.F.5. Some states do not allow disclaimers of certain implied war- ranties or the exclusion or limitation of certain types of damages. If any disclaimer or limitation set forth in this agreement violates the law of the state applicable to this agreement, the agreement shall be interpreted to make the maximum disclaimer or limi- tation permitted by the applicable state law. The invalidity or unenforceability of any provision of this agreement shall not void the remaining provisions.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1951)
- **Original**: 1936 The Ramayana 1.F.6. INDEMNITY — You agree to indemnify and hold the Foun- dation, the trademark owner, any agent or employee of the Foundation, anyone providing copies of Project Gutenberg™ electronic works in accordance with this agreement, and any volunteers associated with the production, promotion and distri- bution of Project Gutenberg™ electronic works, harmless from all liability, costs and expenses, including legal fees, that arise directly or indirectly from any of the following which you do or cause to occur: (a) distribution of this or any Project Gutenberg™ work, (b) alteration, modification, or additions or deletions to any Project Gutenberg™ work, and (c) any Defect you cause. Section 2. Information about the Mission of Project Gutenberg™ Project Gutenberg™ is synonymous with the free distribution of electronic works in formats readable by the widest variety of computers including obsolete, old, middle-aged and new com- puters. It exists because of the efforts of hundreds of volunteers and donations from people in all walks of life. Volunteers and financial support to provide volunteers with the assistance they need, is critical to reaching Project Gutenberg™ 's goals and ensuring that the Project Gutenberg™ collection will remain freely available for generations to come. In 2001, the Project Gutenberg Literary Archive Foundation was created to provide a secure and permanent future for Project Gutenberg™
- **Translation**: 

---

### Verse 12 (Ramayan 0.1952)
- **Original**: The Full Project Gutenberg License 1937 and future generations. To learn more about the Project Guten- berg Literary Archive Foundation and how your efforts and donations can help, see Sections 3 and 4 and the Foundation web page at http://www.pglaf.org. Section 3. Information about the Project Gutenberg Literary Archive Foundation The Project Gutenberg Literary Archive Foundation is a non profit 501(c)(3) educational corporation organized under the laws of the state of Mississippi and granted tax exempt status by the Internal Revenue Service. The Foundation's EIN or federal tax identification number is 64-6221541. Its 501(c)(3) letter is posted at http://www.gutenberg.org/fundraising/pglaf. Contribu- tions to the Project Gutenberg Literary Archive Foundation are tax deductible to the full extent permitted by U.S. federal laws and your state's laws. The Foundation's principal office is located at 4557 Melan Dr. S. Fairbanks, AK, 99712., but its volunteers and employees are scattered throughout numerous locations. Its business office is located at 809 North 1500 West, Salt Lake City, UT 84116, (801) 596-1887, email business@pglaf.org. Email contact links and up to date contact information can be found at the Foundation's web site and official page at http://www.pglaf.org For additional contact information: Dr. Gregory B. Newby Chief Executive and Director gbnewby@pglaf.org
- **Translation**: 

---

### Verse 13 (Ramayan 0.1953)
- **Original**: 1938 The Ramayana Section 4. Information about Donations to the Project Gutenberg Literary Archive Foundation Project Gutenberg™ depends upon and cannot survive without wide spread public support and donations to carry out its mission of increasing the number of public domain and licensed works that can be freely distributed in machine readable form accessible by the widest array of equipment including outdated equipment. Many small donations ($1 to $5,000) are particularly important to maintaining tax exempt status with the IRS. The Foundation is committed to complying with the laws regulating charities and charitable donations in all 50 states of the United States. Compliance requirements are not uniform and it takes a considerable effort, much paperwork and many fees to meet and keep up with these requirements. We do not solicit donations in locations where we have not received writ- ten confirmation of compliance. To SEND DONATIONS or determine the status of compliance for any particular state visit http://www.gutenberg.org/fundraising/donate While we cannot and do not solicit contributions from states where we have not met the solicitation requirements, we know of no prohibition against accepting unsolicited donations from donors in such states who approach us with offers to donate. International donations are gratefully accepted, but we cannot make any statements concerning tax treatment of donations re- ceived from outside the United States. U.S. laws alone swamp our small staff. Please check the Project Gutenberg Web pages for current donation methods and addresses. Donations are accepted in a number of other ways including checks, online payments and
- **Translation**: 

---

### Verse 14 (Ramayan 0.1954)
- **Original**: The Full Project Gutenberg License 1939 credit card donations. To donate, please visit: http://www.guten- berg.org/fundraising/donate Section 5. General Information About Project Gutenberg™ electronic works. Professor Michael S. Hart is the originator of the Project Guten- berg™ concept of a library of electronic works that could be freely shared with anyone. For thirty years, he produced and dis- tributed Project Gutenberg™ eBooks with only a loose network of volunteer support. Project Gutenberg™ eBooks are often created from several printed editions, all of which are confirmed as Public Domain in the U.S. unless a copyright notice is included. Thus, we do not necessarily keep eBooks in compliance with any particular paper edition. Each eBook is in a subdirectory of the same number as the eBook's eBook number, often in several formats including plain vanilla ASCII, compressed (zipped), HTML and others. Correctededitionsof our eBooks replace the old file and take over the old filename and etext number. The replaced older file is renamed.Versionsbased on separate sources are treated as new eBooks receiving new filenames and etext numbers. Most people start at our Web site which has the main PG search facility: http://www.gutenberg.org
- **Translation**: 

---

### Verse 15 (Ramayan 0.1955)
- **Original**: 1940 The Ramayana This Web site includes information about Project Guten- berg™ , including how to make donations to the Project Guten- berg Literary Archive Foundation, how to help produce our new eBooks, and how to subscribe to our email newsletter to hear about new eBooks.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1)
- **Original**: The Project Gutenberg EBook of The Ramayana This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at http://www.guten- berg.org/license Title: The Ramayana Release Date: March 18, 2008 [Ebook 24869] Language: English ***START OF THE PROJECT GUTENBERG EBOOK THE RAMAYANA***
- **Translation**: 

---

### Verse 17 (Ramayana 0.2)
- **Original**: The RÁMÁYAN of VÁLMÍKI Translated into English Verse by Ralph T. H. Griffith, M.A. Principal of the Benares College London: Trübner & Co. Benares: E. J. Lazarus and Co. 1870-1874
- **Translation**: 

---

### Verse 18 (Ramayana 0.3)
- **Original**: Contents Invocation. . . . . . . . . . . . . . . . . . . . . . . . . .2 Book I. . . . . . . . . . . . . . . . . . . . . . . . . . . .4 Canto I. Nárad. . . . . . . . . . . . . . . . . . . . . .4 Canto II. Brahmá's Visit . . . . . . . . . . . . . . . . .19 Canto III. The Argument. . . . . . . . . . . . . . . . .26 Canto IV. The Rhapsodists. . . . . . . . . . . . . . . .31 Canto V. Ayodhyá. . . . . . . . . . . . . . . . . . . .35 Canto VI. The King. . . . . . . . . . . . . . . . . . . .38 Canto VII. The Ministers. . . . . . . . . . . . . . . . .43 Canto VIII. Sumantra's Speech. . . . . . . . . . . . . .45 Canto IX. Rishyasring. . . . . . . . . . . . . . . . . .49 Canto X. Rishyasring Invited. . . . . . . . . . . . . . .58 Canto XI. The Sacrifice Decreed. . . . . . . . . . . . .62 Canto XII. The Sacrifice Begun. . . . . . . . . . . . .65 Canto XIII. The Sacrifice Finished. . . . . . . . . . . .69 Canto XIV. Rávan Doomed. . . . . . . . . . . . . . .79 Canto XV. The Nectar. . . . . . . . . . . . . . . . . .84 Canto XVI. The Vánars. . . . . . . . . . . . . . . . .88 Canto XVII. Rishyasring's Return. . . . . . . . . . . .92 Canto XVIII. Rishyasring's Departure. . . . . . . . . .97 Canto XIX. The Birth Of The Princes. . . . . . . . . .100 Canto XX. Visvámitra's Visit. . . . . . . . . . . . . .105 Canto XXI. Visvámitra's Speech. . . . . . . . . . . . .108 Canto XXII. Dasaratha's Speech. . . . . . . . . . . . .111 Canto XXIII. Vasishtha's Speech. . . . . . . . . . . . .114 Canto XXIV. The Spells. . . . . . . . . . . . . . . . .117 Canto XXV. The Hermitage Of Love. . . . . . . . . .120 Canto XXVI. The Forest Of Tádaká. . . . . . . . . . .123 Canto XXVII. The Birth Of Tádaká. . . . . . . . . . .128
- **Translation**: 

---

### Verse 19 (Ramayana 0.4)
- **Original**: iv The Ramayana Canto XXVIII. The Death Of Tádaká. . . . . . . . . .130 Canto XXIX. The Celestial Arms. . . . . . . . . . . .134 Canto XXX. The Mysterious Powers. . . . . . . . . .138 Canto XXXI. The Perfect Hermitage. . . . . . . . . . .140 Canto XXXII. Visvámitra's Sacrifice. . . . . . . . . .144 Canto XXXIII. The Sone. . . . . . . . . . . . . . . . .147 Canto XXXIV. Brahmadatta. . . . . . . . . . . . . . .149 Canto XXXV. Visvámitra's Lineage. . . . . . . . . . .156 Canto XXXVI. The Birth Of Gangá. . . . . . . . . . .159 Canto XXXIX. The Sons Of Sagar. . . . . . . . . . . .162 Canto XL. The Cleaving Of The Earth. . . . . . . . . .165 Canto XLI. Kapil. . . . . . . . . . . . . . . . . . . . .168 Canto XLII. Sagar's Sacrifice. . . . . . . . . . . . . .173 Canto XLIII. Bhagírath. . . . . . . . . . . . . . . . . .176 Canto XLIV. The Descent Of Gangá. . . . . . . . . . .179 Canto XLV. The Quest Of The Amrit. . . . . . . . . .186 Canto XLVI. Diti's Hope. . . . . . . . . . . . . . . . .194 Canto XLVII. Sumati. . . . . . . . . . . . . . . . . . .196 Canto XLVIII. Indra And Ahalyá . . . . . . . . . . . .199 Canto XLIX. Ahalyá Freed. . . . . . . . . . . . . . . .202 Canto L. Janak. . . . . . . . . . . . . . . . . . . . . .204 Canto LI. Visvámitra. . . . . . . . . . . . . . . . . . .207 Canto LII. Vasishtha's Feast. . . . . . . . . . . . . . .210 Canto LIII. Visvámitra's Request. . . . . . . . . . . . .213 Canto LIV. The Battle. . . . . . . . . . . . . . . . . .217 Canto LV. The Hermitage Burnt. . . . . . . . . . . . .220 Canto LVI. Visvámitra's Vow. . . . . . . . . . . . . .224 Canto LVII. Trisanku. . . . . . . . . . . . . . . . . . .227 Canto LVIII. Trisanku Cursed. . . . . . . . . . . . . .230 Canto LIX. The Sons Of Vasishtha. . . . . . . . . . .234 Canto LX. Trisanku's Ascension. . . . . . . . . . . . .236 Canto LXI. Sunahsepha. . . . . . . . . . . . . . . . .241 Canto LXII. Ambarísha's Sacrifice. . . . . . . . . . . .245 Canto LXIII. Menaká. . . . . . . . . . . . . . . . . . .248
- **Translation**: 

---

### Verse 20 (Ramayana 0.5)
- **Original**: v Canto LXIV. Rambhá. . . . . . . . . . . . . . . . . .252 Canto LXV. Visvámitra's Triumph . . . . . . . . . . .255 Canto LXVI. Janak's Speech. . . . . . . . . . . . . . .259 Canto LXVII. The Breaking Of The Bow. . . . . . . .263 Canto LXVIII. The Envoys' Speech. . . . . . . . . . .266 Canto LXIX. Dasaratha's Visit. . . . . . . . . . . . . .268 Canto LXX. The Maidens Sought. . . . . . . . . . . .270 Canto LXXI. Janak's Pedigree. . . . . . . . . . . . . .276 Canto LXXII. The Gift Of Kine. . . . . . . . . . . . .279 Canto LXXIII. The Nuptials. . . . . . . . . . . . . . .281 Canto LXXIV. Ráma With The Axe. . . . . . . . . . .286 Canto LXXV. The Parle. . . . . . . . . . . . . . . . .289 Canto LXXVI. Debarred From Heaven. . . . . . . . .293 Canto LXXVII. Bharat's Departure. . . . . . . . . . .296 BOOK II. . . . . . . . . . . . . . . . . . . . . . . . . . .301 Canto I. The Heir Apparent. . . . . . . . . . . . . . .301 Canto II. The People's Speech. . . . . . . . . . . . . .305 Canto III. Dasaratha's Precepts. . . . . . . . . . . . . .310 Canto IV. Ráma Summoned. . . . . . . . . . . . . . .316 Canto V. Ráma's Fast. . . . . . . . . . . . . . . . . . .322 Canto VI. The City Decorated. . . . . . . . . . . . . .325 Canto VII. Manthará's Lament. . . . . . . . . . . . . .328 Canto VIII. Manthará's Speech. . . . . . . . . . . . . .332 Canto IX. The Plot. . . . . . . . . . . . . . . . . . . .337 Canto X. Dasaratha's Speech. . . . . . . . . . . . . . .344 Canto XI. The Queen's Demand. . . . . . . . . . . . .349 Canto XII. Dasaratha's Lament. . . . . . . . . . . . . .352 Canto XIII. Dasaratha's Distress. . . . . . . . . . . . .365 Canto XIV. Ráma Summoned. . . . . . . . . . . . . .367 Canto XV. The Preparations. . . . . . . . . . . . . . .375 Canto XVI. Ráma Summoned. . . . . . . . . . . . . .381 Canto XVII. Ráma's Approach. . . . . . . . . . . . . .387 Canto XVIII. The Sentence. . . . . . . . . . . . . . . .389 Canto XIX. Ráma's Promise. . . . . . . . . . . . . . .394
- **Translation**: 

---



--- End of Ramayan_batch_98.md ---


--- Start of Ramayan_batch_99.md ---

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

### Verse 1 (Ramayana 0.6)
- **Original**: vi The Ramayana Canto XX. Kausalyá's Lament. . . . . . . . . . . . . .399 Canto XXI. Kausalyá Calmed. . . . . . . . . . . . . .405 Canto XXII. Lakshman Calmed. . . . . . . . . . . . .413 Canto XXIII. Lakshman's Anger. . . . . . . . . . . . .417 Canto XXIV. Kausalyá Calmed. . . . . . . . . . . . .422 Canto XXV. Kausalyá's Blessing. . . . . . . . . . . .427 Canto XXVI. Alone With Sítá. . . . . . . . . . . . . .433 Canto XXVII. Sítá's Speech. . . . . . . . . . . . . . .437 Canto XXVIII. The Dangers Of The Wood. . . . . . .440 Canto XXIX. Sítá's Appeal. . . . . . . . . . . . . . . .443 Canto XXX. The Triumph Of Love. . . . . . . . . . .446 Canto XXXI. Lakshman's Prayer. . . . . . . . . . . . .452 Canto XXXII. The Gift Of The Treasures. . . . . . . .456 Canto XXXIII. The People's Lament. . . . . . . . . . .462 Canto XXXIV. Ráma In The Palace. . . . . . . . . . .465 Canto XXXV. Kaikeyí Reproached. . . . . . . . . . .472 Canto XXXVI. Siddhárth's Speech. . . . . . . . . . . .476 Canto XXXVII. The Coats Of Bark. . . . . . . . . . .480 Canto XXXVIII. Care For Kausalyá . . . . . . . . . .484 Canto XXXIX. Counsel To Sítá. . . . . . . . . . . . .486 Canto XL. Ráma's Departure. . . . . . . . . . . . . . .491 Canto XLI. The Citizens' Lament. . . . . . . . . . . .497 Canto XLII. Dasaratha's Lament. . . . . . . . . . . . .500 Canto XLIII. Kausalyá's Lament. . . . . . . . . . . . .504 Canto XLIV. Sumitrá's Speech. . . . . . . . . . . . . .507 Canto XLV. The Tamasá. . . . . . . . . . . . . . . . .510 Canto XLVI. The Halt. . . . . . . . . . . . . . . . . .514 Canto XLVII. The Citizens' Return. . . . . . . . . . .518 Canto XLVIII. The Women's Lament. . . . . . . . . .521 Canto XLIX. The Crossing Of The Rivers. . . . . . . .525 Canto L. The Halt Under The Ingudí. . . . . . . . . . .527 Canto LI. Lakshman's Lament. . . . . . . . . . . . . .532 Canto LII. The Crossing Of Gangá. . . . . . . . . . . .534 Canto LIII. Ráma's Lament. . . . . . . . . . . . . . . .547
- **Translation**: 

---

### Verse 2 (Ramayana 0.7)
- **Original**: vii Canto LIV. Bharadvája's Hermitage. . . . . . . . . . .551 Canto LV. The Passage Of Yamuná. . . . . . . . . . .557 Canto LVI. Chitrakúta . . . . . . . . . . . . . . . . .561 Canto LVII. Sumantra's Return. . . . . . . . . . . . .566 Canto LVIII. Ráma's Message. . . . . . . . . . . . . .570 Canto LIX. Dasaratha's Lament. . . . . . . . . . . . .574 Canto LX. Kausalyá Consoled. . . . . . . . . . . . . .579 Canto LXI. Kausalyá's Lament. . . . . . . . . . . . . .582 Canto LXII. Dasaratha Consoled. . . . . . . . . . . . .585 Canto LXIII. The Hermit's Son. . . . . . . . . . . . . .587 Canto LXIV. Dasaratha's Death. . . . . . . . . . . . .593 Canto LXV. The Women's Lament. . . . . . . . . . .602 Canto LXVI. The Embalming. . . . . . . . . . . . . .606 Canto LXVII. The Praise Of Kings. . . . . . . . . . .608 Canto LXVIII. The Envoys. . . . . . . . . . . . . . . .612 Canto LXIX. Bharat's Dream. . . . . . . . . . . . . . .617 Canto LXX. Bharat's Departure. . . . . . . . . . . . .619 Canto LXXI. Bharat's Return. . . . . . . . . . . . . . .623 Canto LXXII. Bharat's Inquiry. . . . . . . . . . . . . .628 Canto LXXIII. Kaikeyí Reproached. . . . . . . . . . .635 Canto LXXIV. Bharat's Lament. . . . . . . . . . . . .638 Canto LXXV. The Abjuration. . . . . . . . . . . . . .642 Canto LXXVI. The Funeral. . . . . . . . . . . . . . .648 Canto LXXVII. The Gathering Of The Ashes. . . . . .651 Canto LXXVIII. Manthará Punished. . . . . . . . . . .654 Canto LXXIX. Bharat's Commands. . . . . . . . . . .657 Canto LXXX. The Way Prepared. . . . . . . . . . . .659 Canto LXXXI. The Assembly. . . . . . . . . . . . . .662 Canto LXXXII. The Departure. . . . . . . . . . . . . .665 Canto LXXXIII. The Journey Begun. . . . . . . . . . .669 Canto LXXXIV. Guha's Anger. . . . . . . . . . . . . .672 Canto LXXXV. Guha And Bharat. . . . . . . . . . . .675 Canto LXXXVI. Guha's Speech. . . . . . . . . . . . .678 Canto LXXXVII. Guha's Story. . . . . . . . . . . . . .680
- **Translation**: 

---

### Verse 3 (Ramayana 0.8)
- **Original**: viii The Ramayana Canto LXXXVIII. The Ingudí Tree. . . . . . . . . . .683 Canto LXXXIX. The Passage Of Gangá. . . . . . . . .687 Canto XC. The Hermitage. . . . . . . . . . . . . . . .689 Canto XCI. Bharadvája's Feast. . . . . . . . . . . . . .692 Canto XCII. Bharat's Farewell. . . . . . . . . . . . . .702 Canto XCIII. Chitrakúta In Sight. . . . . . . . . . . . .707 Canto XCIV. Chitrakúta. . . . . . . . . . . . . . . . .710 Canto XCV. Mandákiní. . . . . . . . . . . . . . . . .714 Canto XCVI. The Magic Shaft. . . . . . . . . . . . . .716 Canto XCVII. Lakshman's Anger. . . . . . . . . . . .723 Canto XCVIII. Lakshman Calmed. . . . . . . . . . . .727 Canto XCIX. Bharat's Approach. . . . . . . . . . . . .731 Canto C. The Meeting. . . . . . . . . . . . . . . . . .732 Canto CI. Bharata Questioned. . . . . . . . . . . . . .737 Canto CII. Bharat's Tidings. . . . . . . . . . . . . . .740 Canto CIII. The Funeral Libation. . . . . . . . . . . .741 Canto CIV. The Meeting With The Queens. . . . . . .747 Canto CV. Ráma's Speech. . . . . . . . . . . . . . . .750 Canto CVI. Bharat's Speech. . . . . . . . . . . . . . .755 Canto CVII. Ráma's Speech. . . . . . . . . . . . . . .759 Canto CVIII. Jáváli's Speech. . . . . . . . . . . . . . .762 Canto CIX. The Praises Of Truth. . . . . . . . . . . .764 Canto CX. The Sons Of Ikshváku. . . . . . . . . . . .770 Canto CXI. Counsel To Bharat. . . . . . . . . . . . . .774 Canto CXII. The Sandals. . . . . . . . . . . . . . . . .778 Canto CXIII. Bharat's Return. . . . . . . . . . . . . . .782 Canto CXIV. Bharat's Departure. . . . . . . . . . . . .785 Canto CXV. Nandigrám. . . . . . . . . . . . . . . . .787 Canto CXVI. The Hermit's Speech. . . . . . . . . . . .790 Canto CXVII. Anasúyá. . . . . . . . . . . . . . . . . .793 Canto CXVIII. Anasúyá's Gifts. . . . . . . . . . . . .797 Canto CXIX. The Forest. . . . . . . . . . . . . . . . .803 BOOK III. . . . . . . . . . . . . . . . . . . . . . . . . . .807 Canto I. The Hermitage. . . . . . . . . . . . . . . . . .807
- **Translation**: 

---

### Verse 4 (Ramayana 0.9)
- **Original**: ix Canto II. Virádha. . . . . . . . . . . . . . . . . . . . .810 Canto III. Virádha Attacked. . . . . . . . . . . . . . .813 Canto IV. Virádha's Death. . . . . . . . . . . . . . . .817 Canto V. Sarabhanga. . . . . . . . . . . . . . . . . . .822 Canto VI. Ráma's Promise. . . . . . . . . . . . . . . .828 Canto VII. Sutíkshna. . . . . . . . . . . . . . . . . . .831 Canto VIII. The Hermitage. . . . . . . . . . . . . . . .835 Canto IX. Sítá's Speech. . . . . . . . . . . . . . . . . .838 Canto X. Ráma's Reply. . . . . . . . . . . . . . . . . .842 Canto XI. Agastya. . . . . . . . . . . . . . . . . . . .845 Canto XII. The Heavenly Bow. . . . . . . . . . . . . .856 Canto XIII. Agastya's Counsel. . . . . . . . . . . . . .862 Canto XIV. Jatáyus. . . . . . . . . . . . . . . . . . . .865 Canto XV. Panchavatí. . . . . . . . . . . . . . . . . .870 Canto XVI. Winter. . . . . . . . . . . . . . . . . . . .875 Canto XVII. Súrpanakhá. . . . . . . . . . . . . . . . .880 Canto XVIII. The Mutilation. . . . . . . . . . . . . . .884 Canto XIX. The Rousing Of Khara. . . . . . . . . . .888 Canto XX. The Giants' Death. . . . . . . . . . . . . .891 Canto XXI. The Rousing Of Khara. . . . . . . . . . .895 Canto XXII. Khara's Wrath. . . . . . . . . . . . . . .897 Canto XXIII. The Omens. . . . . . . . . . . . . . . . .900 Canto XXIV. The Host In Sight. . . . . . . . . . . . .904 Canto XXV. The Battle. . . . . . . . . . . . . . . . . .910 Canto XXVI. Dúshan's Death. . . . . . . . . . . . . .915 Canto XXVII. The Death Of Trisirás. . . . . . . . . .920 Canto XXVIII. Khara Dismounted. . . . . . . . . . . .923 Canto XXIX. Khara's Defeat. . . . . . . . . . . . . . .927 Canto XXX. Khara's Death. . . . . . . . . . . . . . . .931 Canto XXXI. Rávan. . . . . . . . . . . . . . . . . . .936 Canto XXXII. Rávan Roused. . . . . . . . . . . . . .944 Canto XXXIII. Súrpanakhá's Speech. . . . . . . . . . .947 Canto XXXIV. Súrpanakhá's Speech. . . . . . . . . .951 Canto XXXV. Rávan's Journey. . . . . . . . . . . . .954
- **Translation**: 

---

### Verse 5 (Ramayana 0.10)
- **Original**: x The Ramayana Canto XXXVI. Rávan's Speech. . . . . . . . . . . . .960 Canto XXXVII. Márícha's Speech. . . . . . . . . . . .963 Canto XXXVIII. Márícha's Speech. . . . . . . . . . .966 Canto XXXIX. Márícha's Speech. . . . . . . . . . . .971 Canto XL. Rávan's Speech. . . . . . . . . . . . . . . .974 Canto XLI. Márícha's Reply. . . . . . . . . . . . . . .978 Canto XLII. Márícha Transformed. . . . . . . . . . . .980 Canto XLIII. The Wondrous Deer. . . . . . . . . . . .985 Canto XLIV. Márícha's Death. . . . . . . . . . . . . .991 Canto XLV. Lakshman's Departure. . . . . . . . . . .995 Canto XLVI. The Guest. . . . . . . . . . . . . . . . .1000 Canto XLVII. Rávan's Wooing. . . . . . . . . . . . . .1005 Canto XLVIII. Rávan's Speech. . . . . . . . . . . . . .1011 Canto XLIX. The Rape Of Sítá. . . . . . . . . . . . . .1014 Canto L. Jatáyus. . . . . . . . . . . . . . . . . . . . .1020 Canto LI. The Combat. . . . . . . . . . . . . . . . . .1023 Canto LII. Rávan's Flight. . . . . . . . . . . . . . . . .1029 Canto LIII. Sítá's Threats. . . . . . . . . . . . . . . . .1035 Canto LIV. Lanká. . . . . . . . . . . . . . . . . . . .1038 Canto LV. Sítá In Prison. . . . . . . . . . . . . . . . .1042 Canto LVI. Sítá's Disdain. . . . . . . . . . . . . . . .1047 Canto LVII. Sítá Comforted. . . . . . . . . . . . . . .1051 Canto LVIII. The Brothers' Meeting. . . . . . . . . . .1055 Canto LIX. Ráma's Return. . . . . . . . . . . . . . . .1058 Canto LX. Lakshman Reproved. . . . . . . . . . . . .1061 Canto LXI. Ráma's Lament. . . . . . . . . . . . . . .1064 Canto LXII. Ráma's Lament. . . . . . . . . . . . . . .1069 Canto LXIII. Ráma's Lament. . . . . . . . . . . . . . .1073 Canto LXIV. Ráma's Lament. . . . . . . . . . . . . . .1075 Canto LXV. Ráma's Wrath. . . . . . . . . . . . . . . .1079 Canto LXVI. Lakshman's Speech. . . . . . . . . . . .1088 Canto LXVII. Ráma Appeased. . . . . . . . . . . . . .1090 Canto LXVIII. Jatáyus. . . . . . . . . . . . . . . . . .1093 Canto LXIX. The Death Of Jatáyus. . . . . . . . . . .1097
- **Translation**: 

---

### Verse 6 (Ramayana 0.11)
- **Original**: xi Canto LXX. Kabandha. . . . . . . . . . . . . . . . . .1102 Canto LXXI. Kabandha's Speech. . . . . . . . . . . .1109 Canto LXXII. Kabandha's Tale. . . . . . . . . . . . .1112 Canto LXXIII. Kabandha's Counsel. . . . . . . . . . .1116 Canto LXXIV. Kabandha's Death. . . . . . . . . . . .1119 Canto LXXV. Savarí. . . . . . . . . . . . . . . . . . .1125 Canto LXXVI. Pampá. . . . . . . . . . . . . . . . . .1129 BOOK IV. . . . . . . . . . . . . . . . . . . . . . . . . . .1134 Canto I. Ráma's Lament. . . . . . . . . . . . . . . . .1134 Canto II. Sugríva's Alarm. . . . . . . . . . . . . . . .1151 Canto III. Hanumán's Speech. . . . . . . . . . . . . . .1155 Canto IV. Lakshman's Reply. . . . . . . . . . . . . . .1160 Canto V. The League. . . . . . . . . . . . . . . . . . .1166 Canto VI. The Tokens. . . . . . . . . . . . . . . . . .1170 Canto VII. Ráma Consoled. . . . . . . . . . . . . . . .1174 Canto VIII. Ráma's Promise. . . . . . . . . . . . . . .1177 Canto IX. Sugríva's Story. . . . . . . . . . . . . . . .1183 Canto X. Sugríva's Story. . . . . . . . . . . . . . . . .1186 Canto XI. Dundubhi. . . . . . . . . . . . . . . . . . .1190 Canto XII. The Palm Trees. . . . . . . . . . . . . . . .1201 Canto XIII. The Return To Kishkindhá. . . . . . . . .1206 Canto XIV. The Challenge. . . . . . . . . . . . . . . .1210 Canto XV. Tárá. . . . . . . . . . . . . . . . . . . . . .1212 Canto XVI. The Fall Of Báli. . . . . . . . . . . . . . .1216 Canto XVII. Báli's Speech. . . . . . . . . . . . . . . .1220 Canto XVIII. Ráma's Reply. . . . . . . . . . . . . . .1228 Canto XIX. Tárá's Grief. . . . . . . . . . . . . . . . .1236 Canto XX. Tárá's Lament. . . . . . . . . . . . . . . .1240 Canto XXI. Hanumán's Speech. . . . . . . . . . . . .1243 Canto XXII. Báli Dead. . . . . . . . . . . . . . . . . .1245 Canto XXIII. Tárá's Lament. . . . . . . . . . . . . . .1250 Canto XXIV. Sugríva's Lament. . . . . . . . . . . . .1254 Canto XXV. Ráma's Speech. . . . . . . . . . . . . . .1256 Canto XXVI. The Coronation. . . . . . . . . . . . . .1262
- **Translation**: 

---

### Verse 7 (Ramayana 0.12)
- **Original**: xii The Ramayana Canto XXVII. Ráma On The Hill. . . . . . . . . . . .1267 Canto XXVIII. The Rains. . . . . . . . . . . . . . . .1272 Canto XXIX. Hanumán's Counsel. . . . . . . . . . . .1276 Canto XXX. Ráma's Lament. . . . . . . . . . . . . . .1280 Canto XXXI. The Envoy. . . . . . . . . . . . . . . . .1284 Canto XXXII. Hanumán's Counsel. . . . . . . . . . . .1290 Canto XXXIII. Lakshman's Entry. . . . . . . . . . . .1292 Canto XXXIV. Lakshman's Speech. . . . . . . . . . .1299 Canto XXXV. Tárá's Speech. . . . . . . . . . . . . . .1301 Canto XXXVI. Sugríva's Speech. . . . . . . . . . . . .1304 Canto XXXVII. The Gathering. . . . . . . . . . . . . .1306 Canto XXXVIII. Sugríva's Departure. . . . . . . . . .1311 Canto XXXIX. The Vánar Host. . . . . . . . . . . . .1314 Canto XL. The Army Of The East. . . . . . . . . . . .1318 Canto XLI. The Army Of The South. . . . . . . . . . .1326 Canto XLII. The Army Of The West. . . . . . . . . . .1331 Canto XLIII. The Army Of The North. . . . . . . . . .1336 Canto XLIV. The Ring. . . . . . . . . . . . . . . . . .1339 Canto XLV. The Departure. . . . . . . . . . . . . . . .1340 Canto XLVI. Sugríva's Tale. . . . . . . . . . . . . . .1342 Canto XLVII. The Return. . . . . . . . . . . . . . . .1344 Canto XLVIII. The Asur's Death. . . . . . . . . . . . .1345 Canto XLIX. Angad's Speech. . . . . . . . . . . . . .1347 Canto L. The Enchanted Cave. . . . . . . . . . . . . .1349 Canto LI. Svayamprabhá. . . . . . . . . . . . . . . . .1351 Canto LII. The Exit. . . . . . . . . . . . . . . . . . . .1353 Canto LIII. Angad's Counsel. . . . . . . . . . . . . . .1356 Canto LIV. Hanumán's Speech. . . . . . . . . . . . . .1358 Canto LV. Angad's Reply. . . . . . . . . . . . . . . .1360 Canto LVI. Sampáti. . . . . . . . . . . . . . . . . . .1363 Canto LVII. Angad's Speech. . . . . . . . . . . . . . .1365 Canto LVIII. Tidings Of Sítá. . . . . . . . . . . . . . .1367 Canto LIX. Sampáti's Story. . . . . . . . . . . . . . .1371 Canto LX. Sampáti's Story. . . . . . . . . . . . . . . .1373
- **Translation**: 

---

### Verse 8 (Ramayana 0.13)
- **Original**: xiii Canto LXI. Sampáti's Story. . . . . . . . . . . . . . .1375 Canto LXII. Sampáti's Story. . . . . . . . . . . . . . .1377 Canto LXIII. Sampáti's Story. . . . . . . . . . . . . . .1379 Canto LXIV. The Sea. . . . . . . . . . . . . . . . . .1381 Canto LXV. The Council. . . . . . . . . . . . . . . . .1383 Canto LXVI. Hanumán. . . . . . . . . . . . . . . . . .1385 Canto LXVII. Hanumán's Speech. . . . . . . . . . . .1389 BOOK V. . . . . . . . . . . . . . . . . . . . . . . . . . .1392 Canto I. Hanumán's Leap. . . . . . . . . . . . . . . . .1392 Canto II. Lanká. . . . . . . . . . . . . . . . . . . . . .1402 Canto III. The Guardian Goddess. . . . . . . . . . . .1405 Canto IV. Within The City. . . . . . . . . . . . . . . .1407 Canto VI. The Court. . . . . . . . . . . . . . . . . . .1409 Canto VII. Rávan's Palace. . . . . . . . . . . . . . . .1411 Canto VIII. The Enchanted Car. . . . . . . . . . . . .1413 Canto IX. The Ladies' Bower. . . . . . . . . . . . . .1414 Canto X. Rávan Asleep. . . . . . . . . . . . . . . . . .1417 Canto XI. The Banquet Hall. . . . . . . . . . . . . . .1419 Canto XII. The Search Renewed. . . . . . . . . . . . .1420 Canto XIII. Despair And Hope. . . . . . . . . . . . . .1422 Canto XIV. The Asoka Grove. . . . . . . . . . . . . .1425 Canto XV. Sítá. . . . . . . . . . . . . . . . . . . . . .1426 Canto XVI. Hanumán's Lament. . . . . . . . . . . . .1427 Canto XVII. Sítá's Guard. . . . . . . . . . . . . . . . .1429 Canto XVIII. Rávan. . . . . . . . . . . . . . . . . . .1430 Canto XIX. Sítá's Fear. . . . . . . . . . . . . . . . . .1432 Canto XX. Rávan's Wooing. . . . . . . . . . . . . . .1433 Canto XXI. Sítá's Scorn. . . . . . . . . . . . . . . . .1436 Canto XXII. Rávan's Threat. . . . . . . . . . . . . . .1438 Canto XXIII. The Demons' Threats. . . . . . . . . . .1441 Canto XXIV. Sítá's Reply. . . . . . . . . . . . . . . .1443 Canto XXV. Sítá's Lament. . . . . . . . . . . . . . . .1444 Canto XXVI. Sítá's Lament. . . . . . . . . . . . . . .1446 Canto XXVII. Trijatá's Dream. . . . . . . . . . . . . .1447
- **Translation**: 

---

### Verse 9 (Ramayana 0.14)
- **Original**: xiv The Ramayana Canto XXX. Hanumán's Deliberation. . . . . . . . . .1449 Canto XXXI. Hanumán's Speech. . . . . . . . . . . . .1452 Canto XXXII. Sítá's Doubt. . . . . . . . . . . . . . . .1453 Canto XXXIII. The Colloquy. . . . . . . . . . . . . .1454 Canto XXXIV. Hanumán's Speech. . . . . . . . . . . .1457 Canto XXXV. Hanumán's Speech. . . . . . . . . . . .1459 Canto XXXVI. Ráma's Ring. . . . . . . . . . . . . . .1460 Canto XXXVII. Sítá's Speech. . . . . . . . . . . . . .1463 Canto XXXVIII. Sítá's Gem. . . . . . . . . . . . . . .1466 Canto XLI. The Ruin Of The Grove. . . . . . . . . . .1468 Canto XLII. The Giants Roused. . . . . . . . . . . . .1470 Canto XLIII. The Ruin Of The Temple. . . . . . . . .1473 Canto XLIV. Jambumáli's Death. . . . . . . . . . . . .1474 Canto XLV. The Seven Defeated. . . . . . . . . . . .1476 Canto XLVI. The Captains. . . . . . . . . . . . . . . .1478 Canto XLVII. The Death Of Aksha. . . . . . . . . . .1479 Canto XLVIII. Hanumán Captured. . . . . . . . . . . .1481 Canto XLIX. Rávan. . . . . . . . . . . . . . . . . . .1483 Canto L. Prahasta's Questions. . . . . . . . . . . . . .1484 Canto LI. Hanumán's Reply. . . . . . . . . . . . . . .1486 Canto LII. Vibhishan's Speech. . . . . . . . . . . . . .1488 Canto LIII. The Punishment. . . . . . . . . . . . . . .1489 Canto LIV. The Burning Of Lanká. . . . . . . . . . . .1491 Canto LV. Fear For Sítá. . . . . . . . . . . . . . . . .1493 Canto LVI. Mount Arishta. . . . . . . . . . . . . . . .1495 Canto LVII. Hanumán's Return. . . . . . . . . . . . .1496 Canto LVIII. The Feast Of Honey. . . . . . . . . . . .1498 Canto LXV. The Tidings. . . . . . . . . . . . . . . . .1500 Canto LXVI. Ráma's Speech. . . . . . . . . . . . . . .1501 BOOK VI. . . . . . . . . . . . . . . . . . . . . . . . . . .1504 Canto I. Ráma's Speech. . . . . . . . . . . . . . . . .1504 Canto II. Sugríva's Speech. . . . . . . . . . . . . . . .1505 Canto III. Lanká. . . . . . . . . . . . . . . . . . . . .1506 Canto IV. The March. . . . . . . . . . . . . . . . . . .1508
- **Translation**: 

---

### Verse 10 (Ramayana 0.15)
- **Original**: xv Canto V. Ráma's Lament. . . . . . . . . . . . . . . . .1515 Canto VI. Rávan's Speech. . . . . . . . . . . . . . . .1517 Canto VII. Rávan Encouraged. . . . . . . . . . . . . .1519 Canto VIII. Prahasta's Speech. . . . . . . . . . . . . .1521 Canto IX. Vibhishan's Counsel. . . . . . . . . . . . . .1524 Canto X. Vibhishan's Counsel. . . . . . . . . . . . . .1526 Canto XI. The Summons. . . . . . . . . . . . . . . . .1529 Canto XII. Rávan's Speech. . . . . . . . . . . . . . . .1531 Canto XIII. Rávan's Speech. . . . . . . . . . . . . . .1535 Canto XIV. Vibhishan's Speech. . . . . . . . . . . . .1537 Canto XV. Indrajít's Speech. . . . . . . . . . . . . . .1539 Canto XVI. Rávan's Speech. . . . . . . . . . . . . . .1541 Canto XVII. Vibhishan's Flight. . . . . . . . . . . . .1544 Canto XVIII. Ráma's Speech. . . . . . . . . . . . . . .1550 Canto XIX. Vibhishan's Counsel. . . . . . . . . . . . .1553 Canto XX. The Spies. . . . . . . . . . . . . . . . . . .1556 Canto XXI. Ocean Threatened. . . . . . . . . . . . . .1560 Canto XXII. Ocean Threatened. . . . . . . . . . . . .1562 Canto XXIII. The Omens. . . . . . . . . . . . . . . . .1569 Canto XXIV. The Spy's Return. . . . . . . . . . . . .1570 Canto XXV. Rávan's Spies. . . . . . . . . . . . . . . .1574 Canto XXVI. The Vánar Chiefs. . . . . . . . . . . . .1578 Canto XXVII. The Vánar Chiefs. . . . . . . . . . . . .1581 Canto XXVIII. The Chieftains. . . . . . . . . . . . . .1583 Canto XXIX. Sárdúla Captured. . . . . . . . . . . . .1585 Canto XXX. Sárdúla's Speech. . . . . . . . . . . . . .1588 Canto XXXI. The Magic Head. . . . . . . . . . . . . .1589 Canto XXXII. Sítá's Lament. . . . . . . . . . . . . . .1592 Canto XXXIII. Saramá. . . . . . . . . . . . . . . . . .1596 Canto XXXIV. Saramá's Tidings. . . . . . . . . . . . .1599 Canto XXXV. Malyaván's Speech. . . . . . . . . . . .1601 Canto XXXVI. Rávan's Reply. . . . . . . . . . . . . .1604 Canto XXXVII. Preparations. . . . . . . . . . . . . . .1606 Canto XXXVIII. The Ascent Of Suvela. . . . . . . . .1608
- **Translation**: 

---

### Verse 11 (Ramayana 0.16)
- **Original**: xvi The Ramayana Canto XXXIX. Lanká. . . . . . . . . . . . . . . . . .1610 Canto XL. Rávan Attacked. . . . . . . . . . . . . . . .1611 Canto XLI. Ráma's Envoy. . . . . . . . . . . . . . . .1614 Canto XLII. The Sally. . . . . . . . . . . . . . . . . .1618 Canto XLIII. The Single Combats. . . . . . . . . . . .1620 Canto XLIV. The Night. . . . . . . . . . . . . . . . .1622 Canto XLV. Indrajít's Victory. . . . . . . . . . . . . .1625 Canto XLVI. Indrajít's Triumph. . . . . . . . . . . . .1626 Canto XLVII. Sítá. . . . . . . . . . . . . . . . . . . .1629 Canto XLVIII. Sítá's Lament. . . . . . . . . . . . . . .1631 Canto XLIX. Ráma's Lament. . . . . . . . . . . . . . .1634 Canto L. The Broken Spell. . . . . . . . . . . . . . . .1637 Canto LI. Dhúmráksha's Sally. . . . . . . . . . . . . .1641 Canto LII. Dhúmráksha's Death. . . . . . . . . . . . .1643 Canto LIII. Vajradanshtra's Sally. . . . . . . . . . . . .1646 Canto LIV. Vajradanshtra's Death. . . . . . . . . . . .1647 Canto LIX. Rávan's Sally. . . . . . . . . . . . . . . . .1650 Canto LX. Kumbhakarna Roused. . . . . . . . . . . .1660 Canto LXI. The Vánars' Alarm. . . . . . . . . . . . . .1666 Canto LXII. Rávan's Request. . . . . . . . . . . . . . .1668 Canto LXIII. Kumbhakarna's Boast. . . . . . . . . . .1670 Canto LXIV. Mahodar's Speech. . . . . . . . . . . . .1672 Canto LXV. Kumbhakarna's Speech. . . . . . . . . . .1674 Canto LXVI. Kumbhakarna's Sally. . . . . . . . . . .1676 Canto LXVII. Kumbhakarna's Death. . . . . . . . . . .1678 Canto LXVIII. Rávan's Lament. . . . . . . . . . . . .1687 Canto LXIX. Narántak's Death. . . . . . . . . . . . . .1689 Canto LXX. The Death Of Trisirás. . . . . . . . . . . .1692 Canto LXXI. Atikáya's Death. . . . . . . . . . . . . .1695 Canto LXXII. Rávan's Speech. . . . . . . . . . . . . .1700 Canto LXXIII. Indrajít's Victory. . . . . . . . . . . . .1701 Canto LXXIV. The Medicinal Herbs. . . . . . . . . . .1704 Canto LXXV. The Night Attack. . . . . . . . . . . . .1708 Canto XCIII. Rávan's Lament. . . . . . . . . . . . . .1712
- **Translation**: 

---

### Verse 12 (Ramayana 0.17)
- **Original**: xvii Canto XCVI. Rávan's Sally. . . . . . . . . . . . . . .1715 Canto C. Rávan In The Field. . . . . . . . . . . . . . .1717 Canto CI. Lakshman's Fall. . . . . . . . . . . . . . . .1720 Canto CII. Lakshman Healed. . . . . . . . . . . . . . .1722 Canto CIII. Indra's Car. . . . . . . . . . . . . . . . . .1724 Canto CVI. Glory To The Sun. . . . . . . . . . . . . .1727 Canto CVIII. The Battle. . . . . . . . . . . . . . . . .1730 Canto CIX. The Battle. . . . . . . . . . . . . . . . . .1731 Canto CX. Rávan's Death. . . . . . . . . . . . . . . .1733 Canto CXI. Vibhishan's Lament. . . . . . . . . . . . .1734 Canto CXII. The Rákshas Dames. . . . . . . . . . . .1736 Canto CXIII. Mandodarí's Lament. . . . . . . . . . . .1737 Canto CXIV. Vibhishan Consecrated. . . . . . . . . .1741 Canto CXV. Sítá's Joy. . . . . . . . . . . . . . . . . .1743 Canto CXVI. The Meeting. . . . . . . . . . . . . . . .1746 Canto CXVII. Sítá's Disgrace. . . . . . . . . . . . . .1749 Canto CXVIII. Sítá's Reply. . . . . . . . . . . . . . .1750 Canto CXIX. Glory To Vishnu. . . . . . . . . . . . . .1753 Canto CXX. Sítá Restored. . . . . . . . . . . . . . . .1755 Canto CXXI. Dasaratha. . . . . . . . . . . . . . . . .1757 Canto CXXII. Indra's Boon. . . . . . . . . . . . . . .1760 Canto CXXIII. The Magic Car. . . . . . . . . . . . . .1762 Canto CXXIV. The Departure. . . . . . . . . . . . . .1764 Canto CXXV. The Return. . . . . . . . . . . . . . . .1766 Canto CXXVI. Bharat Consoled. . . . . . . . . . . . .1768 Canto CXXVII. Ráma's Message. . . . . . . . . . . .1771 Canto CXXVIII. Hanumán's Story. . . . . . . . . . . .1774 Canto CXXIX. The Meeting With Bharat. . . . . . . .1775 Canto CXXX. The Consecration. . . . . . . . . . . . .1780 APPENDIX. . . . . . . . . . . . . . . . . . . . . . . . . .1787 Section XIII. Rávan Doomed. . . . . . . . . . . . . . .1787 Caput XIV. RATIO NECANDI RAVANAE EXCOG- ITATA. . . . . . . . . . . . . . . . . . . . . . .1790
- **Translation**: 

---

### Verse 13 (Ramayana 0.18)
- **Original**: xviii The Ramayana Caput XIV. IL MEZZO STABILITO PER UC- CIDERE RÁVANO. . . . . . . . . . . . . . . .1793 XIV. . . . . . . . . . . . . . . . . . . . . . . . . . . .1796 Uttarakánda. . . . . . . . . . . . . . . . . . . . . . . .1799 ADDITIONAL NOTES. . . . . . . . . . . . . . . . . . .1812 Queen Fortune. . . . . . . . . . . . . . . . . . . . . .1812 Indra. . . . . . . . . . . . . . . . . . . . . . . . . . .1813 Vishnu. . . . . . . . . . . . . . . . . . . . . . . . . .1813 Siva. . . . . . . . . . . . . . . . . . . . . . . . . . . .1815 Apsarases. . . . . . . . . . . . . . . . . . . . . . . . .1816 Vishnu's Incarnation As Ráma. . . . . . . . . . . . . .1817 Kusa and Lava. . . . . . . . . . . . . . . . . . . . . .1820 Parasuráma, . . . . . . . . . . . . . . . . . . .1827 Yáma, . . . . . . . . . . . . . . . . . . . . . .1828 Fate, . . . . . . . . . . . . . . . . . . . . . . .1829 Visvámitra, . . . . . . . . . . . . . . . . . . .1829 Household Gods, . . . . . . . . . . . . . . . .1829 . . . . . . . . . . . . . . . . . . . . . . . . .1830 . . . . . . . . . . . . . . . . . . . . . . . . .1833 . . . . . . . . . . . . . . . . . . . . . . . . .1835 . . . . . . . . . . . . . . . . . . . . . . . . .1835 . . . . . . . . . . . . . . . . . . . . . . . . .1836 . . . . . . . . . . . . . . . . . . . . . . . . .1836 . . . . . . . . . . . . . . . . . . . . . . . . .1838 . . . . . . . . . . . . . . . . . . . . . . . . .1838 . . . . . . . . . . . . . . . . . . . . . . . . .1838 . . . . . . . . . . . . . . . . . . . . . . . . .1840 . . . . . . . . . . . . . . . . . . . . . . . . .1840 . . . . . . . . . . . . . . . . . . . . . . . . .1841 . The Praise Of Kings . . . . . . . . . . . . .1841 . Sálmalí. . . . . . . . . . . . . . . . . . . .1842 . Bharat's Return. . . . . . . . . . . . . . . .1843 . . . . . . . . . . . . . . . . . . . . . . . . .1844 . . . . . . . . . . . . . . . . . . . . . . . . .1844
- **Translation**: 

---

### Verse 14 (Ramayana 0.19)
- **Original**: xix . . . . . . . . . . . . . . . . . . . . . . . . .1845 . . . . . . . . . . . . . . . . . . . . . . . . .1849 . . . . . . . . . . . . . . . . . . . . . . . . .1849 . . . . . . . . . . . . . . . . . . . . . . . . .1849 . Urvasí. . . . . . . . . . . . . . . . . . . . .1854 . . . . . . . . . . . . . . . . . . . . . . . . .1856 . . . . . . . . . . . . . . . . . . . . . . . . .1856 . Ráma's Alliance With Sugríva. . . . . . . .1857 . The Fall Of Báli. . . . . . . . . . . . . . . .1858 . The Vánar Host. . . . . . . . . . . . . . . .1859 . . . . . . . . . . . . . . . . . . . . . . . . .1861 . . . . . . . . . . . . . . . . . . . . . . . . .1863 . Northern Kurus. . . . . . . . . . . . . . . .1866 . . . . . . . . . . . . . . . . . . . . . . . . .1868 . . . . . . . . . . . . . . . . . . . . . . . . .1868 . . . . . . . . . . . . . . . . . . . . . . . . .1869 . . . . . . . . . . . . . . . . . . . . . . . . .1869 . . . . . . . . . . . . . . . . . . . . . . . . .1869 . . . . . . . . . . . . . . . . . . . . . . . . .1870 . . . . . . . . . . . . . . . . . . . . . . . . .1870 . . . . . . . . . . . . . . . . . . . . . . . . .1871 . . . . . . . . . . . . . . . . . . . . . . . . .1871 . . . . . . . . . . . . . . . . . . . . . . . . .1872 . . . . . . . . . . . . . . . . . . . . . . . . .1873 . Rávan's Funeral. . . . . . . . . . . . . . . .1879 . . . . . . . . . . . . . . . . . . . . . . . . .1880 . The Meeting. . . . . . . . . . . . . . . . . .1883 Final Notes. . . . . . . . . . . . . . . . . . . . . . . .1885 INDEX OF PRINCIPAL NAMES . . . . . . . . . . . . .1893 Footnotes . . . . . . . . . . . . . . . . . . . . . . . . . .1921
- **Translation**: 

---

### Verse 15 (Ramayana 0.20)
- **Original**: Invocation.1 Praise to Válmíki,2 bird of charming song,3 Who mounts on Poesy's sublimest spray, And sweetly sings with accent clear and strong Ráma, aye Ráma, in his deathless lay. Where breathes the man can listen to the strain That flows in music from Válmíki's tongue, Nor feel his feet the path of bliss attain When Ráma's glory by the saint is sung! 1 The MSS. vary very considerably in these stanzas of invocation: many lines are generally prefixed in which not only the poet, but those who play the chief parts in the poem are panegyrized. It is self-apparent that they are not by the author of the Rámáyan himself. 2 “Válmíki was the son of VaruGa, the regent of the waters, one of whose names is Prachetas. According to theAdhyátmá RámáyaGa, the sage, although a Bráhman by birth, associated with foresters and robbers. Attacking on one occasion the seven Rishis, they expostulated with him successfully, and taught him themantraof Ráma reversed, orMará, Mará, in the inaudible repetition of which he remained immovable for thousands of years, so that when the sages returned to the same spot they found him still there, converted into avalmíkor ant-hill, by the nests of the termites, whence his name of Válmíki.” W ILSON {FNS .Specimens of the Hindu Theatre, Vol. I. p. 313. “Válmíki is said to have lived a solitary life in the woods: he is called both a muni and arishi. The former word properly signifies an anchorite or hermit; the latter has reference chiefly to wisdom. The two words are frequently used promiscuously, and may both be rendered by the Latinvatesin its earliest meaning ofseer: Válmíki was both poet and seer, as he is said to have sung the exploits of Ráma by the aid of divining insight rather than of knowledge naturally acquired.” SCHLEGEL {FNS . 3 Literally,Kokila, the Koïl, or Indian Cuckoo. Schlegel translates“luscini-
- **Translation**: 

---

### Verse 16 (Ramayana 0.21)
- **Original**: Invocation. 3 The stream Rámáyan leaves its sacred fount The whole wide world from sin and stain to free.4 The Prince of Hermits is the parent mount, The lordly Ráma is the darling sea. Glory to him whose fame is ever bright! Glory to him, Prachetas'5holy son! Whose pure lips quaff with ever new delight The nectar-sea of deeds by Ráma done. Hail, arch-ascetic, pious, good, and kind! Hail, Saint Válmíki, lord of every lore! Hail, holy Hermit, calm and pure of mind! Hail, First of Bards, Válmíki, hail once more! um.” 4 Comparison with the Ganges is implied, that river being called the purifier of the world. 5 “This name may have been given to the father of Válmíki allegorically. If we look at the derivation of the word (pra, before, andchetas, mind) it is as if the poet were called the son of Prometheus, the Forethinker.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 17 (Ramayana 0.22)
- **Original**: Book I.6 Canto I. Nárad.7 OM. 8 To sainted Nárad, prince of those Whose lore in words of wisdom flows. Whose constant care and chief delight Were Scripture and ascetic rite, The good Válmíki, first and best[002] Of hermit saints, these words addressed:9 “In all this world, I pray thee, who Is virtuous, heroic, true? Firm in his vows, of grateful mind, To every creature good and kind? Bounteous, and holy, just, and wise, Alone most fair to all men's eyes? Devoid of envy, firm, and sage, 6 Called in Sanskrit alsoBála-KáG a, and in HindíBál-KáG ,i.e.the Book describing Ráma's childhood,bálameaning a boy up to his sixteenth year. 7 A divine saint, son of Brahmá. He is the eloquent messenger of the Gods, a musician of exquisite skill, and the inventor of thevíGá or Indian lute. He bears a strong resemblance to Hermes or Mercury. 8 This mystic syllable, said to typify the supreme Deity, the Gods collectively, the Vedas, the three spheres of the world, the three holy fires, the three steps of VishGu etc., prefaces the prayers and most venerated writings of the Hindus. 9 This colloquy is supposed to have taken place about sixteen years after Ráma's return from his wanderings and occupation of his ancestral throne.
- **Translation**: 

---

### Verse 18 (Ramayana 0.23)
- **Original**: Canto I. Nárad. 5 Whose tranquil soul ne'er yields to rage? Whom, when his warrior wrath is high, Do Gods embattled fear and fly? Whose noble might and gentle skill The triple world can guard from ill? Who is the best of princes, he Who loves his people's good to see? The store of bliss, the living mine Where brightest joys and virtues shine? Queen Fortune's10 best and dearest friend, Whose steps her choicest gifts attend? Who may with Sun and Moon compare, With Indra,11 VishGu,12 Fire, and Air? Grant, Saint divine,13 the boon I ask, For thee, I ween, an easy task, To whom the power is given to know If such a man breathe here below.” Then Nárad, clear before whose eye The present, past, and future lie,14 10 Called alsoZrí and Lakshmí, the consort of VishGu, the Queen of Beauty as well as the Dea Fortuna. Her birth“from the full-flushed wave” is described in Canto XLV of this Book. 11 One of the most prominent objects of worship in the Rig-veda, Indra was superseded in later times by the more popular deities VishGu andZiva. He is the God of the firmament, and answers in many respects to the Jupiter Pluvius of the Romans. SeeAdditional Notes. 12 The second God of the Trimúrti or Indian Trinity. Derived from the root vi[ to penetrate, the meaning of the name appears to behe who penetrates or pervades all things. An embodiment of the preserving power of nature, he is worshipped as a Saviour who has nine times been incarnate for the good of the world and will descend on earth once more. SeeAdditional Notesand Muir's Sanskrit Textspassim. 13 In Sanskritdevarshi. Rishi is the general appellation of sages, and another word is frequently prefixed to distinguish the degrees. ABrahmarshi is a theologian or Bráhmanical sage; a Rájarshi is a royal sage or sainted king; a Devarshiis a divine or deified sage or saint. 14 Trikálajùa. Literallyknower of the three times. Both Schlegel and Gorresio
- **Translation**: 

---

### Verse 19 (Ramayana 0.24)
- **Original**: 6 The Ramayana Made ready answer:“Hermit, where Are graces found so high and rare? Yet listen, and my tongue shall tell In whom alone these virtues dwell. From old Ikshváku's15 line he came, Known to the world by Ráma's name: With soul subdued, a chief of might, In Scripture versed, in glory bright, His steps in virtue's paths are bent, Obedient, pure, and eloquent. In each emprise he wins success, And dying foes his power confess. Tall and broad-shouldered, strong of limb, Fortune has set her mark on him. Graced with a conch-shell's triple line, His throat displays the auspicious sign.16[003] futurorum eventuum in unguibus atque etiam in dentibus.” Though the palmy days of Indian chiromancy have passed away, the art is still to some extent studied and believed in. quote Homer's. MÂ $´· Ä'y½Ä±,Äq Ä'ÃÃy¼µ½±, ÀÁy Ä'y½Ä±. “That sacred seer, whose comprehensive view, The past, the present, and the future knew.” The Bombay edition readstrilokajùa, who knows the three worlds(earth, air and heaven.)“It is bytapas(austere fervour) that rishis of subdued souls, subsisting on roots, fruits and air, obtain a vision of the three worlds with all things moving and stationary.” M ANU {FNS , XI. 236. 15 Son of Manu, the first king of Ko[ala and founder of the solar dynasty or family of the Children of the Sun, the God of that luminary being the father of Manu. 16 The Indians paid great attention to the art of physiognomy and believed that character and fortune could be foretold not from the face only but from marks upon the neck and hands. Three lines under the chin like those at the mouth of a conch (ZaDkha) were regarded as a peculiarly auspicious sign indicating, as did also the mark of VishGu's discus on the hand, one born to be achakravartin
- **Translation**: 

---

### Verse 20 (Ramayana 0.25)
- **Original**: Canto I. Nárad. 7 High destiny is clear impressed On massive jaw and ample chest, His mighty shafts he truly aims, And foemen in the battle tames. Deep in the muscle, scarcely shown, Embedded lies his collar-bone. His lordly steps are firm and free, His strong arms reach below his knee;17 All fairest graces join to deck His head, his brow, his stately neck, And limbs in fair proportion set: The manliest form e'er fashioned yet. Graced with each high imperial mark, His skin is soft and lustrous dark. Large are his eyes that sweetly shine With majesty almost divine. His plighted word he ne'er forgets; On erring sense a watch he sets. By nature wise, his teacher's skill Has trained him to subdue his will. Good, resolute and pure, and strong, He guards mankind from scathe and wrong, And lends his aid, and ne'er in vain, The cause of justice to maintain. Well has he studied o'er and o'er or universal emperor. In the palmistry of Europe the line of fortune, as well as the line of life, is in the hand. Cardan says that marks on the nails and teeth also show what is to happen to us:“Sunt etiam in nobis vestigia quædam 17 Long arms were regarded as a sign of heroic strength.
- **Translation**: 

---



--- End of Ramayan_batch_99.md ---


--- Start of Ramayan_batch_100.md ---

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

### Verse 1 (Ramayana 0.26)
- **Original**: 8 The Ramayana The Vedas18and their kindred lore. Well skilled is he the bow to draw,19 Well trained in arts and versed in law; High-souled and meet for happy fate, Most tender and compassionate; The noblest of all lordly givers, Whom good men follow, as the rivers Follow the King of Floods, the sea: So liberal, so just is he. 18 “Veda means originally knowing or knowledge, and this name is given by the Bráhmans not to one work, but to the whole body of their most ancient sacred literature. Veda is the same word which appears in the Greek¿w´±, I know, and in the English wise, wisdom, to wit. The name of Veda is commonly given to four collections of hymns, which are respectively known by the names of Rig-veda, Yajur-veda, Sáma-veda, and Atharva-veda.” “As the language of the Veda, the Sanskrit, is the most ancient type of the English of the present day, (Sanskrit and English are but varieties of one and the same language,) so its thoughts and feelings contain in reality the first roots and germs of that intellectual growth which by an unbroken chain connects our own generation with the ancestors of the Aryan race,— with those very people who at the rising and setting of the sun listened with trembling hearts to the songs of the Veda, that told them of bright powers above, and of a life to come after the sun of their own lives had set in the clouds of the evening. These men were the true ancestors of our race, and the Veda is the oldest book we have in which to study the first beginnings of our language, and of all that is embodied in language. We are by nature Aryan, Indo-European, not Semitic: our spiritual kith and kin are to be found in India, Persia, Greece, Italy, Germany: not in Mesopotamia, Egypt, or Palestine.” Chips from a German Workshop, Vol. I. pp. 8. 4. 19 As with the ancient Persians and Scythians, Indian princes were carefully
- **Translation**: 

---

### Verse 2 (Ramayana 0.27)
- **Original**: Canto I. Nárad. 9 The joy of Queen Kau[alyá's20heart, In every virtue he has part: Firm as Himálaya's21 snowy steep, Unfathomed like the mighty deep: The peer of VishGu's power and might, And lovely as the Lord of Night;22 Patient as Earth, but, roused to ire, Fierce as the world-destroying fire; In bounty like the Lord of Gold,23 And Justice self in human mould. With him, his best and eldest son, By all his princely virtues won King Da[aratha24 willed to share His kingdom as the Regent Heir. But when Kaikeyí, youngest queen, With eyes of envious hate had seen The solemn pomp and regal state Prepared the prince to consecrate, She bade the hapless king bestow Two gifts he promised long ago, That Ráma to the woods should flee, And that her child the heir should be. By chains of duty firmly tied, The wretched king perforce complied. [004] instructed in archery which stands for military science in general, of which, among Hindu heroes, it was the most important branch. 20 Chief of the three queens of Da[aratha and mother of Ráma. 21 From hima snow, (GreekÇµ¹¼-}½, Latin hiems) andálaya abode, the Mansion of snow. 22 The moon (Soma ,Indu,Chandra etc.) is masculine with the Indians as with the Germans. 23 Kuvera, the Indian Plutus, or God of Wealth. 24 The events here briefly mentioned will be related fully in the course of the poem. The first four cantos are introductory, and are evidently the work of a later hand than Valmiki's.
- **Translation**: 

---

### Verse 3 (Ramayana 0.28)
- **Original**: 10 The Ramayana Ráma, to please Kaikeyí went Obedient forth to banishment. Then LakshmaG's truth was nobly shown, Then were his love and courage known, When for his brother's sake he dared All perils, and his exile shared. And Sítá, Ráma's darling wife, Loved even as he loved his life, Whom happy marks combined to bless, A miracle of loveliness, Of Janak's royal lineage sprung, Most excellent of women, clung To her dear lord, like RohiGí Rejoicing with the Moon to be.25 The King and people, sad of mood, The hero's car awhile pursued. But when Prince Ráma lighted down At Zringavera's pleasant town, Where Gangá's holy waters flow, 25 “Chandra, or the Moon, is fabled to have been married to the twenty-seven daughters of the patriarch Daksha, or A[viní and the rest, who are in fact personifications of the Lunar Asterisms. His favourite amongst them was RohiGí to whom he so wholly devoted himself as to neglect the rest. They complained to their father, and Daksha repeatedly interposed, till, finding his remonstrances vain, he denounced a curse upon his son-in-law, in consequence of which he remained childless and became affected by consumption. The wives of Chandra having interceded in his behalf with their father, Daksha modified an imprecation which he could not recall, and pronounced that the decay should be periodical only, not permanent, and that it should alternate with periods of recovery. Hence the successive wane and increase of the Moon. Padma ,PuráGa,Swarga-KhaG a,Sec. II.RohiGíin Astronomy is the fourth lunar mansion, containing five stars, the principal of which is Aldebaran.” W ILSON {FNS ,Specimens of the Hindu Theatre. Vol. I. p.234. The Bengal recension has a different reading: “Shone with her husband like the light Attendant on the Lord of Night.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.29)
- **Original**: Canto I. Nárad. 11 He bade his driver turn and go. Guha, Nishádas' king, he met, And on the farther bank was set. Then on from wood to wood they strayed, O'er many a stream, through constant shade, As Bharadvája bade them, till They came to Chitrakúma's hill. And Ráma there, with LakshmaG's aid, A pleasant little cottage made, And spent his days with Sítá, dressed In coat of bark and deerskin vest.26 And Chitrakúma grew to be As bright with those illustrious three As Meru's27 sacred peaks that shine With glory, when the Gods recline Beneath them:Ziva's28 self between The Lord of Gold and Beauty's Queen. 26 The garb prescribed for ascetics by Manu. 27 “Mount Meru, situated like Kailása in the lofty regions to the north of the Himálayas, is celebrated in the traditions and myths of India. Meru and Kailása are the two Indian Olympi. Perhaps they were held in such veneration be- cause the Sanskrit-speaking Indians remembered the ancient home where they dwelt with the other primitive peoples of their family before they descended to occupy the vast plains which extend between the Indus and the Ganges.” G ORRESIO {FNS . 28 The third God of the Indian Triad, the God of destruction and reproduction. See Additional Notes.
- **Translation**: 

---

### Verse 5 (Ramayana 0.30)
- **Original**: 12 The Ramayana The aged king for Ráma pined, And for the skies the earth resigned. Bharat, his son, refused to reign, Though urged by all the twice-born29 train. Forth to the woods he fared to meet His brother, fell before his feet, And cried,“Thy claim all men allow: O come, our lord and king be thou.” But Ráma nobly chose to be Observant of his sire's decree. He placed his sandals30 in his hand A pledge that he would rule the land: And bade his brother turn again. Then Bharat, finding prayer was vain, The sandals took and went away; Nor in Ayodhyá would he stay. But turned to Nandigráma, where He ruled the realm with watchful care, Still longing eagerly to learn Tidings of Ráma's safe return. Then lest the people should repeat Their visit to his calm retreat, Away from Chitrakúma's hill Fared Ráma ever onward till[005] 29 The epithetdwija, ortwice-born, is usually appropriate to Bráhmans, but is applicable to the three higher castes. Investiture with the sacred thread and initiation of the neophyte into certain religious mysteries are regarded as his regeneration or second birth. 30 His shoes to be a memorial of the absent heir and to maintain his right. Kálidása (RaghuvaE[a, XII. 17.) says that they were to beadhidevateor guardian deities of the kingdom.
- **Translation**: 

---

### Verse 6 (Ramayana 0.31)
- **Original**: Canto I. Nárad. 13 Beneath the shady trees he stood Of DaG aká's primeval wood, Virádha, giant fiend, he slew, And then Agastya's friendship knew. Counselled by him he gained the sword And bow of Indra, heavenly lord: A pair of quivers too, that bore Of arrows an exhaustless store. While there he dwelt in greenwood shade The trembling hermits sought his aid, And bade him with his sword and bow Destroy the fiends who worked them woe: To come like Indra strong and brave, A guardian God to help and save. And Ráma's falchion left its trace Deep cut onZúrpaGakhá's face: A hideous giantess who came Burning for him with lawless flame. Their sister's cries the giants heard. And vengeance in each bosom stirred: The monster of the triple head. And DúshaG to the contest sped. But they and myriad fiends beside Beneath the might of Ráma died. When Ráva G, dreaded warrior, knew The slaughter of his giant crew: RávaG, the king, whose name of fear Earth, hell, and heaven all shook to hear: He bade the fiend Márícha aid The vengeful plot his fury laid. In vain the wise Márícha tried To turn him from his course aside: Not RávaG's self, he said, might hope
- **Translation**: 

---

### Verse 7 (Ramayana 0.32)
- **Original**: 14 The Ramayana With Ráma and his strength to cope. Impelled by fate and blind with rage He came to Ráma's hermitage. There, by Márícha's magic art, He wiled the princely youths apart, The vulture31 slew, and bore away The wife of Ráma as his prey. The son of Raghu32 came and found Jamáyu slain upon the ground. He rushed within his leafy cot; He sought his wife, but found her not. Then, then the hero's senses failed; In mad despair he wept and wailed. Upon the pile that bird he laid, And still in quest of Sítá strayed. A hideous giant then he saw, Kabandha named, a shape of awe. The monstrous fiend he smote and slew, And in the flame the body threw; When straight from out the funeral flame In lovely form Kabandha came, And bade him seek in his distress A wise and holy hermitess. By counsel of this saintly dame To Pampá's pleasant flood he came, And there the steadfast friendship won Of Hanumán the Wind-God's son. Counselled by him he told his grief 31 Jamáyu, a semi-divine bird, the friend of Ráma, who fought in defence of Sítá. 32 Raghu was one of the most celebrated ancestors of Ráma whose commonest appellation is, therefore, Rághava or descendant of Raghu. Kálidása in the RaghuraG[a makes him the son of Dilípa and great-grandfather of Ráma. See Idylls from the Sanskrit,“Aja” and “Dilípa.”
- **Translation**: 

---

### Verse 8 (Ramayana 0.33)
- **Original**: Canto I. Nárad. 15 To great Sugríva, Vánar chief, Who, knowing all the tale, before The sacred flame alliance swore. Sugríva to his new-found friend Told his own story to the end: His hate of Báli for the wrong And insult he had borne so long. And Ráma lent a willing ear And promised to allay his fear. Sugríva warned him of the might Of Báli, matchless in the fight, And, credence for his tale to gain, Showed the huge fiend33 by Báli slain. The prostrate corse of mountain size Seemed nothing in the hero's eyes; He lightly kicked it, as it lay, And cast it twenty leagues34 away. To prove his might his arrows through Seven palms in line, uninjured, flew. He cleft a mighty hill apart, And down to hell he hurled his dart. Then high Sugríva's spirit rose, Assured of conquest o'er his foes. With his new champion by his side To vast Kishkindhá's cave he hied. Then, summoned by his awful shout, King Báli came in fury out, First comforted his trembling wife, Then sought Sugríva in the strife. One shaft from Ráma's deadly bow The monarch in the dust laid low. 33 Dundhubi. 34 Literallyten yojanas. The yojana is a measure of uncertain length variously reckoned as equal to nine miles, five, and a little less.
- **Translation**: 

---

### Verse 9 (Ramayana 0.34)
- **Original**: 16 The Ramayana Then Ráma bade Sugríva reign In place of royal Báli slain. Then speedy envoys hurried forth Eastward and westward, south and north, Commanded by the grateful king Tidings of Ráma's spouse to bring. Then by Sampáti's counsel led, Brave Hanumán, who mocked at dread, Sprang at one wild tremendous leap Two hundred leagues across the deep. To Lanká's35 town he urged his way, Where RávaG held his royal sway.[006] There pensive 'neath A[oka36 boughs He found poor Sítá, Ráma's spouse. He gave the hapless girl a ring, A token from her lord and king. A pledge from her fair hand he bore; Then battered down the garden door. Five captains of the host he slew, Seven sons of councillors o'erthrew; Crushed youthful Aksha on the field, Then to his captors chose to yield. Soon from their bonds his limbs were free, But honouring the high decree Which Brahmá37 had pronounced of yore, 35 Ceylon. 36 The Jonesia A[oka is a most beautiful tree bearing a profusion of red blossoms. 37 Brahmá , the Creator, is usually regarded as the first God of the Indian Trinity, although, as Kálidása says: “Of Brahmá, VishGu,Ziva, each may be First, second, third, amid the blessed Three.” Brahmá had guaranteed RávaG's life against all enemies except man.
- **Translation**: 

---

### Verse 10 (Ramayana 0.35)
- **Original**: Canto I. Nárad. 17 He calmly all their insults bore. The town he burnt with hostile flame, And spoke again with Ráma's dame, Then swiftly back to Ráma flew With tidings of the interview. Then with Sugríva for his guide, Came Ráma to the ocean side. He smote the sea with shafts as bright As sunbeams in their summer height, And quick appeared the Rivers' King38 Obedient to the summoning. A bridge was thrown by Nala o'er The narrow sea from shore to shore.39 They crossed to Lanká's golden town, Where Ráma's hand smote RávaG down. VibhishaG there was left to reign Over his brother's wide domain. To meet her husband Sítá came; But Ráma, stung with ire and shame, With bitter words his wife addressed Before the crowd that round her pressed. But Sítá, touched with noble ire, Gave her fair body to the fire. Then straight the God of Wind appeared, And words from heaven her honour cleared. And Ráma clasped his wife again, Uninjured, pure from spot and stain, Obedient to the Lord of Fire And the high mandate of his sire. Led by the Lord who rules the sky, 38 Ocean personified. 39 The rocks lying between Ceylon and the mainland are still called Ráma's Bridge by the Hindus.
- **Translation**: 

---

### Verse 11 (Ramayana 0.36)
- **Original**: 18 The Ramayana The Gods and heavenly saints drew nigh, And honoured him with worthy meed, Rejoicing in each glorious deed. His task achieved, his foe removed, He triumphed, by the Gods approved. By grace of Heaven he raised to life The chieftains slain in mortal strife; Then in the magic chariot through The clouds to Nandigráma flew. Met by his faithful brothers there, He loosed his votive coil of hair: Thence fair Ayodhyá's town he gained, And o'er his father's kingdom reigned. Disease or famine ne'er oppressed His happy people, richly blest With all the joys of ample wealth, Of sweet content and perfect health. No widow mourned her well-loved mate, No sire his son's untimely fate. They feared not storm or robber's hand; No fire or flood laid waste the land: The Golden Age40 had come again To bless the days of Ráma's reign. From him, the great and glorious king, Shall many a princely scion spring. And he shall rule, beloved by men, 40 “The Bráhmans, with a system rather cosmogonical than chronological, divide the present mundane period into four ages oryugas as they call them: the Krita, the Tretá, the Dwápara, and the Kali. The Krita, called also the Deva-yuga or that of the Gods, is the age of truth, the perfect age, the Tretá is the age of the three sacred fires, domestic and sacrificial; the Dwápara is the age of doubt; the Kali, the present age, is the age of evil.” G ORRESIO .{FNS
- **Translation**: 

---

### Verse 12 (Ramayana 0.37)
- **Original**: Canto II. Brahmá's Visit 19 Ten thousand years and hundreds ten,41 And when his life on earth is past To Brahmá's world shall go at last.” Whoe'er this noble poem reads That tells the tale of Ráma's deeds, Good as the Scriptures, he shall be From every sin and blemish free. Whoever reads the saving strain, With all his kin the heavens shall gain. Bráhmans who read shall gather hence The highest praise for eloquence. The warrior, o'er the land shall reign, The merchant, luck in trade obtain; And Zúdras listening42 ne'er shall fail To reap advantage from the tale.43 [007] Canto II. Brahmá's Visit 41 The ancient kings of India enjoyed lives of more than patriarchal length as will appear in the course of the poem. 42 Zúdras, men of the fourth and lowest pure caste, were not allowed to read the poem, but might hear it recited. 43 The three[lokesor distichs which these twelve lines represent are evidently a still later and very awkward addition to the introduction.
- **Translation**: 

---

### Verse 13 (Ramayana 0.38)
- **Original**: 20 The Ramayana Válmíki, graceful speaker, heard, To highest admiration stirred. To him whose fame the tale rehearsed He paid his mental worship first; Then with his pupil humbly bent Before the saint most eloquent. Thus honoured and dismissed the seer Departed to his heavenly sphere. Then from his cot Válmíki hied To Tamasá's44 sequestered side, Not far remote from Gangá's tide. He stood and saw the ripples roll Pellucid o'er a pebbly shoal. To Bharadvája45 by his side He turned in ecstasy, and cried: “See, pupil dear, this lovely sight, The smooth-floored shallow, pure and bright, With not a speck or shade to mar, And clear as good men's bosoms are. Here on the brink thy pitcher lay, And bring my zone of bark, I pray. Here will I bathe: the rill has not, To lave the limbs, a fairer spot. Do quickly as I bid, nor waste The precious time; away, and haste.” 44 There are several rivers in India of this name, now corrupted intoTonse. The river here spoken of is that which falls into the Ganges a little below Allahabad. 45 “In Book II, Canto LIV, we meet with a saint of this name presiding over a convent of disciples in his hermitage at the confluence of the Ganges and the Jumna. Thence the later author of these introductory cantos has borrowed the name and person, inconsistently indeed, but with the intention of enhancing the dignity of the poet by ascribing to him so celebrated a disciple.” SCHLEGEL .{FNS
- **Translation**: 

---

### Verse 14 (Ramayana 0.39)
- **Original**: Canto II. Brahmá's Visit 21 Obedient to his master's hest Quick from the cot he brought the vest; The hermit took it from his hand, And tightened round his waist the band; Then duly dipped and bathed him there, And muttered low his secret prayer. To spirits and to Gods he made Libation of the stream, and strayed Viewing the forest deep and wide That spread its shade on every side. Close by the bank he saw a pair Of curlews sporting fearless there. But suddenly with evil mind An outcast fowler stole behind, And, with an aim too sure and true, The male bird near the hermit slew. The wretched hen in wild despair With fluttering pinions beat the air, And shrieked a long and bitter cry When low on earth she saw him lie, Her loved companion, quivering, dead, His dear wings with his lifeblood red; And for her golden crested mate She mourned, and was disconsolate. The hermit saw the slaughtered bird, And all his heart with ruth was stirred. The fowler's impious deed distressed His gentle sympathetic breast, And while the curlew's sad cries rang Within his ears, the hermit sang: “No fame be thine for endless time, Because, base outcast, of thy crime, Whose cruel hand was fain to slay
- **Translation**: 

---

### Verse 15 (Ramayana 0.40)
- **Original**: 22 The Ramayana One of this gentle pair at play!” E'en as he spoke his bosom wrought And laboured with the wondering thought What was the speech his ready tongue Had uttered when his heart was wrung. He pondered long upon the speech, Recalled the words and measured each, And thus exclaimed the saintly guide To Bharadvája by his side: “With equal lines of even feet, With rhythm and time and tone complete, The measured form of words I spoke In shock of grief be termed a[loke.”46 And Bharadvája, nothing slow His faithful love and zeal to show, Answered those words of wisdom,“Be The name, my lord, as pleases thee.” As rules prescribe the hermit took Some lustral water from the brook. But still on this his constant thought Kept brooding, as his home he sought; While Bharadvája paced behind, A pupil sage of lowly mind, And in his hand a pitcher bore With pure fresh water brimming o'er. Soon as they reached their calm retreat The holy hermit took his seat; His mind from worldly cares recalled, And mused in deepest thought enthralled. 46 The poet plays upon the similarity in sound of the two words:[oka, means grief,[loka, the heroic measure in which the poem is composed. It need scarcely be said that the derivation is fanciful.
- **Translation**: 

---

### Verse 16 (Ramayana 0.41)
- **Original**: Canto II. Brahmá's Visit 23 Then glorious Brahmá,47 Lord Most High, Creator of the earth and sky, [008] The four-faced God, to meet the sage Came to Válmíki's hermitage. Soon as the mighty God he saw, Up sprang the saint in wondering awe. Mute, with clasped hands, his head he bent, And stood before him reverent. His honoured guest he greeted well, Who bade him of his welfare tell; Gave water for his blessed feet, Brought offerings,48 and prepared a seat. In honoured place the God Most High Sate down, and bade the saint sit nigh. There sate before Válmíki's eyes The Father of the earth and skies; But still the hermit's thoughts were bent On one thing only, all intent On that poor curlew's mournful fate Lamenting for her slaughtered mate; And still his lips, in absent mood, The verse that told his grief, renewed: 47 Brahmá, the Creator, is usually regarded as the first person of the divine triad of India. The four heads with which he is represented are supposed to have allusion to the four corners of the earth which he is sometimes considered to personify. As an object of adoration Brahmá has been entirely superseded by Ziva and VishGu. In the whole of India there is, I believe, but one temple dedicated to his worship. In this point the first of the Indian triad curiously resembles the last of the divine fraternity of Greece, Aïdes the brother of Zeus and Poseidon.“In all Greece, says Pausanias, there is no single temple of Aïdes, except at a single spot in Elis.” See Gladstone's Juventus Mundi, p. 253. 48 The argha or arghya was a libation or offering to a deity, a Bráhman, or other venerable personage. According to one authority it consisted of water, milk, the points of Kúsa-grass, curds, clarified butter, rice, barley, and white mustard, according to another, of saffron, bel, unbroken grain, flowers, curds, dúrbá-grass, kúsa-grass, and sesamum.
- **Translation**: 

---

### Verse 17 (Ramayana 0.42)
- **Original**: 24 The Ramayana “Woe to the fowler's impious hand That did the deed that folly planned; That could to needless death devote The curlew of the tuneful throat!” The heavenly Father smiled in glee, And said,“O best of hermits, see, A verse, unconscious, thou hast made; No longer be the task delayed. Seek not to trace, with labour vain, The unpremeditated strain. The tuneful lines thy lips rehearsed Spontaneous from thy bosom burst. Then come, O best of seers, relate The life of Ráma good and great, The tale that saintly Nárad told, In all its glorious length unfold. Of all the deeds his arm has done Upon this earth, omit not one, And thus the noble life record Of that wise, brave, and virtuous lord. His every act to day displayed, His secret life to none betrayed: How Lakshma G, how the giants fought; With high emprise and hidden thought: And all that Janak's child49 befell Where all could see, where none could tell. The whole of this shall truly be Made known, O best of saints, to thee. In all thy poem, through my grace, No word of falsehood shall have place. Begin the story, and rehearse The tale divine in charming verse. 49 Sítá, daughter of Janak king of Míthilá.
- **Translation**: 

---

### Verse 18 (Ramayana 0.43)
- **Original**: Canto II. Brahmá's Visit 25 As long as in this firm-set land The streams shall flow, the mountains stand, So long throughout the world, be sure, The great Rámáyan shall endure.50 While the Rámáyan's ancient strain Shall glorious in the earth remain, To higher spheres shalt thou arise And dwell with me above the skies.” He spoke, and vanished into air, And left Válmíki wondering there. The pupils of the holy man, Moved by their love of him, began To chant that verse, and ever more They marvelled as they sang it o'er: “Behold, the four-lined balanced rime, Repeated over many a time, In words that from the hermit broke In shock of grief, becomes a[loke.” This measure now Válmíki chose Wherein his story to compose. In hundreds of such verses, sweet With equal lines and even feet, The saintly poet, lofty-souled, The glorious deeds of Ráma told. 50 “I congratulate myself,” says Schlegel in the preface to his, alas, unfinished edition of the Rámáyan,“that, by the favour of the Supreme Deity, I have been allowed to begin so great a work; I glory and make my boast that I too after so many ages have helped to confirm that ancient oracle declared to Válmíki by the Father of Gods and men: Dum stabunt montes, campis dum flumina current, Usque tuum toto carmen celebrabitur orbe.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.44)
- **Original**: 26 The Ramayana Canto III. The Argument. The hermit thus with watchful heed Received the poem's pregnant seed, And looked with eager thought around If fuller knowledge might be found.[009] His lips with water first bedewed,51 He sate, in reverent attitude On holy grass,52 the points all bent Together toward the orient;53 And thus in meditation he Entered the path of poesy. Then clearly, through his virtue's might, All lay discovered to his sight, Whate'er befell, through all their life, Ráma, his brother, and his wife: And Da [aratha and each queen At every time, in every scene: His people too, of every sort; The nobles of his princely court: Whate'er was said, whate'er decreed, Each time they sate each plan and deed: For holy thought and fervent rite Had so refined his keener sight That by his sanctity his view The present, past, and future knew, And he with mental eye could grasp, Like fruit within his fingers clasp, 51 “The sipping of water is a requisite introduction of all rites: without it, says the Sámha Purána, all acts of religion are vain.” C OLEBROOKE .{FNS 52 The darhha orku[a (Pea cynosuroides), a kind of grass used in sacrifice by the Hindus ascerbenawas by the Romans. 53 The direction in which the grass should be placed upon the ground as a seat for the Gods, on occasion of offerings made to them.
- **Translation**: 

---

### Verse 20 (Ramayana 0.45)
- **Original**: Canto III. The Argument. 27 The life of Ráma, great and good, Roaming with Sítá in the wood. He told, with secret-piercing eyes, The tale of Ráma's high emprise, Each listening ear that shall entice, A sea of pearls of highest price. Thus good Válmíki, sage divine, Rehearsed the tale of Raghu's line, As Nárad, heavenly saint, before Had traced the story's outline o'er. He sang of Ráma's princely birth, His kindness and heroic worth; His love for all, his patient youth, His gentleness and constant truth, And many a tale and legend old By holy Vi[vámitra told. How Janak's child he wooed and won, And broke the bow that bent to none. How he with every virtue fraught His namesake Ráma54 met and fought. The choice of Ráma for the throne; The malice by Kaikeyí shown, Whose evil counsel marred the plan And drove him forth a banisht man. How the king grieved and groaned, and cried, And swooned away and pining died. The subjects' woe when thus bereft; And how the following crowds he left: With Guha talked, and firmly stern Ordered his driver to return. How Gangá's farther shore he gained; By Bharadvája entertained, 54 Para[uráma or Ráma with the Axe. See Canto LXXIV.
- **Translation**: 

---



--- End of Ramayan_batch_100.md ---


--- Start of Ramayan_batch_101.md ---

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

### Verse 1 (Ramayana 0.46)
- **Original**: 28 The Ramayana By whose advice he journeyed still And came to Chitrakúma's hill. How there he dwelt and built a cot; How Bharat journeyed to the spot; His earnest supplication made; Drink-offerings to their father paid; The sandals given by Ráma's hand, As emblems of his right, to stand: How from his presence Bharat went And years in Nandigráma spent. How Ráma entered DaG ak wood And in SutíkhGa's presence stood. The favour Anasúyá showed, The wondrous balsam she bestowed. How Zarabhanga's dwelling-place They sought; saw Indra face to face; The meeting with Agastya gained; The heavenly bow from him obtained. How Ráma with Virádha met; Their home in Panchavama set. How ZúrpaGakhá underwent The mockery and disfigurement. Of Tri[irá's and Khara's fall, Of RávaG roused at vengeance call, Márícha doomed, without escape; The fair Videhan55 lady's rape. How Ráma wept and raved in vain, And how the Vulture-king was slain. How Ráma fierce Kabandha slew; Then to the side of Pampá drew, Met Hanumán, and her whose vows Were kept beneath the greenwood boughs. 55 Sítá. Videha was the country of which Míthilá was the capital.
- **Translation**: 

---

### Verse 2 (Ramayana 0.47)
- **Original**: Canto III. The Argument. 29 How Raghu's son, the lofty-souled, On Pampá's bank wept uncontrolled, Then journeyed, Rishyamúk to reach, And of Sugríva then had speech. The friendship made, which both had sought: How Báli and Sugríva fought. How Báli in the strife was slain, And how Sugríva came to reign. The treaty, Tára's wild lament; The rainy nights in watching spent. The wrath of Raghu's lion son; The gathering of the hosts in one. The sending of the spies about, And all the regions pointed out. The ring by Ráma's hand bestowed; The cave wherein the bear abode. The fast proposed, their lives to end; Sampati gained to be their friend. [010] The scaling of the hill, the leap Of Hanumán across the deep. Ocean's command that bade them seek Maináka of the lofty peak. The death of Sinhiká, the sight Of Lanká with her palace bright How Hanumán stole in at eve; His plan the giants to deceive. How through the square he made his way To chambers where the women lay, Within the A[oka garden came And there found Ráma's captive dame. His colloquy with her he sought, And giving of the ring he brought. How Sítá gave a gem o'erjoyed; How Hanumán the grove destroyed.
- **Translation**: 

---

### Verse 3 (Ramayana 0.48)
- **Original**: 30 The Ramayana How giantesses trembling fled, And servant fiends were smitten dead. How Hanumán was seized; their ire When Lanká blazed with hostile fire. His leap across the sea once more; The eating of the honey store. How Ráma he consoled, and how He showed the gem from Sítá's brow. With Ocean, Ráma's interview; The bridge that Nala o'er it threw. The crossing, and the sitting down At night round Lanká's royal town. The treaty with VibhíshaG made: The plan for RávaG's slaughter laid. How Kumbhakar Ga in his pride And Meghanáda fought and died. How Ráva G in the fight was slain, And captive Sítá brought again. VibhíshaG set upon the throne; The flying chariot Pushpak shown. How Brahmá and the Gods appeared, And Sítá's doubted honour cleared. How in the flying car they rode To Bharadvája's cabin abode. The Wind-God's son sent on afar; How Bharat met the flying car. How Ráma then was king ordained; The legions their discharge obtained. How Ráma cast his queen away; How grew the people's love each day. Thus did the saint Válmíki tell Whate'er in Ráma's life befell, And in the closing verses all That yet to come will once befall.
- **Translation**: 

---

### Verse 4 (Ramayana 0.49)
- **Original**: Canto IV. The Rhapsodists. 31 Canto IV. The Rhapsodists. When to the end the tale was brought, Rose in the sage's mind the thought; “Now who throughout this earth will go, And tell it forth that all may know?” As thus he mused with anxious breast, Behold, in hermit's raiment dressed, Ku [á and Lava56 came to greet Their master and embrace his feet. The twins he saw, that princely pair Sweet-voiced, who dwelt beside him there None for the task could be more fit, For skilled were they in Holy Writ; And so the great Rámáyan, fraught With lore divine, to these he taught: The lay whose verses sweet and clear Take with delight the listening ear, That tell of Sítá's noble life And RávaG's fall in battle strife. Great joy to all who hear they bring, Sweet to recite and sweet to sing. For music's sevenfold notes are there, And triple measure,57 wrought with care With melody and tone and time, And flavours58 that enhance the rime; 56 The twin sons of Ráma and Sítá, born after Ráma had repudiated Sítá, and brought up in the hermitage of Válmíki. As they were the first rhapsodists the combined name Ku[ílava signifies a reciter of poems, or an improvisatore, even to the present day. 57 Perhaps the bass, tenor, and treble, or quick, slow and middle times. we know but little of the ancient music of the Hindus. 58 Eight flavours or sentiments are usually enumerated, love, mirth, tender- ness, anger, heroism, terror, disgust, and surprise; tranquility or content, or
- **Translation**: 

---

### Verse 5 (Ramayana 0.50)
- **Original**: 32 The Ramayana Heroic might has ample place, And loathing of the false and base, With anger, mirth, and terror, blent With tenderness, surprise, content. When, half the hermit's grace to gain, And half because they loved the strain, The youth within their hearts had stored The poem that his lips outpoured, Válmíki kissed them on the head, As at his feet they bowed, and said; “Recite ye this heroic song In tranquil shades where sages throng: Recite it where the good resort, In lowly home and royal court.” The hermit ceased. The tuneful pair, Like heavenly minstrels sweet and fair, In music's art divinely skilled, Their saintly master's word fulfilled. Like Ráma's self, from whom they came, They showed their sire in face and frame,[011] As though from some fair sculptured stone Two selfsame images had grown. Sometimes the pair rose up to sing, Surrounded by a holy ring, Where seated on the grass had met Full many a musing anchoret. Then tears bedimmed those gentle eyes, As transport took them and surprise, And as they listened every one Cried in delight, Well done! Well done! paternal tenderness, is sometimes considered the ninth. WILSON {FNS . See the Sáhitya DarpaGa or Mirror of Compositiontranslated by Dr. Ballantyne and Bábú Pramadádása Mittra in theBibliotheca Indica.
- **Translation**: 

---

### Verse 6 (Ramayana 0.51)
- **Original**: Canto IV. The Rhapsodists. 33 Those sages versed in holy lore Praised the sweet minstrels more and more: And wondered at the singers' skill, And the bard's verses sweeter still, Which laid so clear before the eye The glorious deeds of days gone by. Thus by the virtuous hermits praised, Inspirited their voice they raised. Pleased with the song this holy man Would give the youths a water-can; One gave a fair ascetic dress, Or sweet fruit from the wilderness. One saint a black-deer's hide would bring, And one a sacrificial string: One, a clay pitcher from his hoard, And one, a twisted munja cord.59 One in his joy an axe would find, One braid, their plaited locks to bind. One gave a sacrificial cup, One rope to tie their fagots up; While fuel at their feet was laid, Or hermit's stool of fig-tree made. All gave, or if they gave not, none Forgot at least a benison. Some saints, delighted with their lays, Would promise health and length of days; Others with surest words would add Some boon to make their spirit glad. In such degree of honour then That song was held by holy men: That living song which life can give, 59 Saccharum Munja is a plant from whose fibres is twisted the sacred string which a Bráhman wears over one shoulder after he has been initiated by a rite which in some respects answers to confirmation.
- **Translation**: 

---

### Verse 7 (Ramayana 0.52)
- **Original**: 34 The Ramayana By which shall many a minstrel live. In seat of kings, in crowded hall, They sang the poem, praised of all. And Ráma chanced to hear their lay, While he the votive steed60 would slay, And sent fit messengers to bring The minstrel pair before the king. They came, and found the monarch high Enthroned in gold, his brothers nigh; While many a minister below, And noble, sate in lengthened row. The youthful pair awhile he viewed Graceful in modest attitude, And then in words like these addressed His brother LakshmaG and the rest: “Come, listen to the wondrous strain Recited by these godlike twain, Sweet singers of a story fraught With melody and lofty thought.” The pair, with voices sweet and strong, Rolled the full tide of noble song, With tone and accent deftly blent To suit the changing argument. Mid that assembly loud and clear Rang forth that lay so sweet to hear, That universal rapture stole Through each man's frame and heart and soul. “These minstrels, blest with every sign That marks a high and princely line, In holy shades who dwell, Enshrined in Saint Válmíki's lay, 60 A description of an A[vamedha or Horse Sacrifice is given in Canto XIII. of this Book.
- **Translation**: 

---

### Verse 8 (Ramayana 0.53)
- **Original**: Canto V. Ayodhyá. 35 A monument to live for aye, My deeds in song shall tell.” Thus Ráma spoke: their breasts were fired, And the great tale, as if inspired, The youths began to sing, While every heart with transport swelled, And mute and rapt attention held The concourse and the king. Canto V. Ayodhyá. “Ikshváku's sons from days of old Were ever brave and mighty-souled. The land their arms had made their own Was bounded by the sea alone. Their holy works have won them praise, Through countless years, from Manu's days. Their ancient sire was Sagar, he Whose high command dug out the sea:61 With sixty thousand sons to throng Around him as he marched along. From them this glorious tale proceeds: The great Rámáyan tells their deeds. This noble song whose lines contain Lessons of duty, love, and gain, We two will now at length recite, While good men listen with delight. 61 This exploit is related in Canto XL.
- **Translation**: 

---

### Verse 9 (Ramayana 0.54)
- **Original**: 36 The Ramayana On Sarjú's62 bank, of ample size, The happy realm of Ko[al lies,[012] With fertile length of fair champaign And flocks and herds and wealth of grain. There, famous in her old renown, Ayodhyá 63 stands, the royal town, In bygone ages built and planned By sainted Manu's64 princely hand. Imperial seat! her walls extend Twelve measured leagues from end to end, And three in width from side to side, With square and palace beautified. Her gates at even distance stand; Her ample roads are wisely planned. Right glorious is her royal street Where streams allay the dust and heat. On level ground in even row Her houses rise in goodly show: Terrace and palace, arch and gate The queenly city decorate. High are her ramparts, strong and vast, By ways at even distance passed, 62 The Sarjú or Ghaghra, anciently called Sarayú, rises in the Himalayas, and after flowing through the province of Oudh, falls into the Ganges. 63 The ruins of the ancient capital of Ráma and the Children of the Sun may still be traced in the present Ajudhyá near Fyzabad. Ajudhyá is the Jerusalem or Mecca of the Hindus. 64 A legislator and saint, the son of Brahmá or a personification of Brahmá himself, the creator of the world, and progenitor of mankind. Derived from the rootman to think, the word means originallyman , the thinker, and is found in this sense in the Rig-veda. Manu as a legislator is identified with the Cretan Minos, as progenitor of mankind with the German Mannus:“Celebrant carminibus antiquis, quod unum apud illos memoriæ et annalium genus est, Tuisconem deum terra editum, et filium Mannum, originem gentis conditoresque.” TACITUS {FNS ,Germania, Cap. II.
- **Translation**: 

---

### Verse 10 (Ramayana 0.55)
- **Original**: Canto V. Ayodhyá. 37 With circling moat, both deep and wide, And store of weapons fortified. King Da[aratha, lofty-souled, That city guarded and controlled, With towering Sál trees belted round,65 And many a grove and pleasure ground, As royal Indra, throned on high, Rules his fair city in the sky.66 She seems a painted city, fair With chess-board line and even square.67 And cool boughs shade the lovely lake Where weary men their thirst may slake. There gilded chariots gleam and shine, And stately piles the Gods enshrine. There gay sleek people ever throng To festival and dance and song. A mine is she of gems and sheen, The darling home of Fortune's Queen. With noblest sort of drink and meat, The fairest rice and golden wheat, And fragrant with the chaplet's scent With holy oil and incense blent. With many an elephant and steed, And wains for draught and cars for speed. With envoys sent by distant kings, And merchants with their precious things With banners o'er her roofs that play, 65 The Sál (Shorea Robusta) is a valuable timber tree of considerable height. 66 The city of Indra is called Amarávatí or Home of the Immortals. 67 Schlegel thinks that this refers to the marble of different colours with which the houses were adorned. It seems more natural to understand it as implying the regularity of the streets and houses.
- **Translation**: 

---

### Verse 11 (Ramayana 0.56)
- **Original**: 38 The Ramayana And weapons that a hundred slay;68 All warlike engines framed by man, And every class of artisan. A city rich beyond compare With bards and minstrels gathered there, And men and damsels who entrance The soul with play and song and dance. In every street is heard the lute, The drum, the tabret, and the flute, The Veda chanted soft and low, The ringing of the archer's bow; With bands of godlike heroes skilled In every warlike weapon, filled, And kept by warriors from the foe, As Nágas guard their home below.69 There wisest Bráhmans evermore The flame of worship feed, And versed in all the Vedas' lore, Their lives of virtue lead. Truthful and pure, they freely give; They keep each sense controlled, And in their holy fervour live Like the great saints of old. Canto VI. The King. 68 The Zataghní i.e. centicide, or slayer of a hundred, is generally supposed to be a sort of fire-arms, or the ancient Indian rocket; but it is also described as a stone set round with iron spikes. 69 The Nágas (serpents) are demigods with a human face and serpent body. They inhabit Pátála or the regions under the earth. Bhogavatí is the name of their capital city. Serpents are still worshipped in India. See Fergusson'sTree and Serpent Worship.
- **Translation**: 

---

### Verse 12 (Ramayana 0.57)
- **Original**: Canto VI. The King. 39 There reigned a king of name revered, To country and to town endeared, Great Da[aratha, good and sage, Well read in Scripture's holy page: [013] Upon his kingdom's weal intent, Mighty and brave and provident; The pride of old Ikshváku's seed For lofty thought and righteous deed. Peer of the saints, for virtues famed, For foes subdued and passions tamed: A rival in his wealth untold Of Indra and the Lord of Gold. Like Manu first of kings, he reigned, And worthily his state maintained. For firm and just and ever true Love, duty, gain he kept in view, And ruled his city rich and free, Like Indra's Amarávatí. And worthy of so fair a place There dwelt a just and happy race With troops of children blest. Each man contented sought no more, Nor longed with envy for the store By richer friends possessed. For poverty was there unknown, And each man counted as his own Kine, steeds, and gold, and grain. All dressed in raiment bright and clean, And every townsman might be seen With earrings, wreath, or chain. None deigned to feed on broken fare, And none was false or stingy there. A piece of gold, the smallest pay, Was earned by labour for a day.
- **Translation**: 

---

### Verse 13 (Ramayana 0.58)
- **Original**: 40 The Ramayana On every arm were bracelets worn, And none was faithless or forsworn, A braggart or unkind. None lived upon another's wealth, None pined with dread or broken health, Or dark disease of mind. High-souled were all. The slanderous word, The boastful lie, were never heard. Each man was constant to his vows, And lived devoted to his spouse. No other love his fancy knew, And she was tender, kind, and true. Her dames were fair of form and face, With charm of wit and gentle grace, With modest raiment simply neat, And winning manners soft and sweet. The twice-born sages, whose delight Was Scripture's page and holy rite, Their calm and settled course pursued, Nor sought the menial multitude. In many a Scripture each was versed, And each the flame of worship nursed, And gave with lavish hand. Each paid to Heaven the offerings due, And none was godless or untrue In all that holy band. To Bráhmans, as the laws ordain, The Warrior caste were ever fain The reverence due to pay; And these the Vai[yas' peaceful crowd, Who trade and toil for gain, were proud To honour and obey; And all were by theZúdras70 served, 70 The fourth and lowest pure caste whose duty was to serve the three first
- **Translation**: 

---

### Verse 14 (Ramayana 0.59)
- **Original**: Canto VI. The King. 41 Who never from their duty swerved, Their proper worship all addressed To Bráhman, spirits, God, and guest. Pure and unmixt their rites remained, Their race's honour ne'er was stained.71 Cheered by his grandsons, sons, and wife, Each passed a long and happy life. Thus was that famous city held By one who all his race excelled, Blest in his gentle reign, As the whole land aforetime swayed By Manu, prince of men, obeyed Her king from main to main. And heroes kept her, strong and brave, As lions guard their mountain cave: Fierce as devouring flame they burned, And fought till death, but never turned. Horses had she of noblest breed, Like Indra's for their form and speed, From Váhlí's72 hills and Sindhu's73 sand, classes. 71 By forbidden marriages between persons of different castes. 72 Váhlí or Váhlíka is Bactriana; its name is preserved in the modern Balkh. 73 The Sanskrit word Sindhu is in the singular the name of the river Indus, in the plural of the people and territories on its banks. The name appears asHidku in the cuneiform inscription of Darius' son of Hystaspes, in which the nations tributary to that king are enumerated. The Hebrew form isHodda (Esther, I. 1.). In Zend it appears asHendu in a somewhat wider sense. With the Persians later the signification ofHind seems to have co-extended with their increasing acquaintance with the country. The weak Ionic dialect omitted the Persianh, and we find in Hecatæus and Herodotus<½´¿Â and ! 8 ½´¹ºu. In this form the Romans received the names and transmitted them to us. The Arabian geographers in their ignorance that Hind and Sind are two forms of the same word have made of them two brothers and traced their decent from Noah. See Lassen's Indische Alterthumskunde Vol. I. pp. 2, 3.
- **Translation**: 

---

### Verse 15 (Ramayana 0.60)
- **Original**: 42 The Ramayana Vanáyu74 and Kámboja's land.75[014] Her noble elephants had strayed Through Vindhyan and Himálayan shade, Gigantic in their bulk and height, Yet gentle in their matchless might. They rivalled well the world-spread fame Of the great stock from which they came, Of Váman, vast of size, Of Mahápadma's glorious line, Thine, Anjan, and, Airávat, thine.76 Upholders of the skies. With those, enrolled in fourfold class, Who all their mighty kin surpass, Whom men Matangas name, And Mrigas spotted black and white, And Bhadras of unwearied might, And Mandras hard to tame.77 Thus, worthy of the name she bore,78 Ayodhyá for a league or more Cast a bright glory round, Where Da[aratha wise and great 74 The situation of Vanáyu is not exactly determined: it seems to have lain to the north-west of India. 75 Kámboja was probably still further to the north-west. Lassen thinks that the name is etymologically connected withCambyses which in the cuneiform inscription of Behistun is written Ka(m)bujia. 76 The elephants of Indra and other deities who preside over the four points of the compass. 77 “There are four kinds of elephants. 1Bhaddar. It is well proportioned, has an erect head, a broad chest, large ears, a long tail, and is bold and can bear fatigue. 2Mand . It is black, has yellow eyes, a uniformly sized body, and is wild and ungovernable. 3Mirg. It has a whitish skin, with black spots. 4Mir. It has a small head, and obeys readily. It gets frightened when it thunders.” Aín-i-Akbarí.. Translated by H. Blochmann, Aín 41,The Imperial Elephant Stables. 78 Ayodhyá means not to be fought against.
- **Translation**: 

---

### Verse 16 (Ramayana 0.61)
- **Original**: Canto VII. The Ministers. 43 Governed his fair ancestral state, With every virtue crowned. Like Indra in the skies he reigned In that good town whose wall contained High domes and turrets proud, With gates and arcs of triumph decked, And sturdy barriers to protect Her gay and countless crowd. Canto VII. The Ministers. Two sages, holy saints, had he, His ministers and priests to be: Va [ishmha, faithful to advise, And Vámadeva, Scripture-wise. Eight other lords around him stood, All skilled to counsel, wise and good: Jayanta, Vijay, Dhrishmi bold In fight, affairs of war controlled: Siddhárth and Arthasádhak true Watched o'er expense and revenue, And Dharmapál and wise A[ok Of right and law and justice spoke. With these the sage Sumantra, skilled To urge the car, high station filled. All these in knowledge duly trained Each passion and each sense restrained: With modest manners, nobly bred Each plan and nod and look they read, Upon their neighbours' good intent, Most active and benevolent:
- **Translation**: 

---

### Verse 17 (Ramayana 0.62)
- **Original**: 44 The Ramayana As sit the Vasus79 round their king, They sate around him counselling. They ne'er in virtue's loftier pride Another's lowly gifts decried. In fair and seemly garb arrayed, No weak uncertain plans they made. Well skilled in business, fair and just, They gained the people's love and trust, And thus without oppression stored The swelling treasury of their lord. Bound in sweet friendship each to each, They spoke kind thoughts in gentle speech. They looked alike with equal eye On every caste, on low and high. Devoted to their king, they sought, Ere his tongue spoke, to learn his thought, And knew, as each occasion rose, To hide their counsel or disclose. In foreign lands or in their own Whatever passed, to them was known. By secret spies they timely knew What men were doing or would do. Skilled in the grounds of war and peace They saw the monarch's state increase, Watching his weal with conquering eye That never let occasion by, While nature lent her aid to bless Their labours with unbought success. Never for anger, lust, or gain, Would they their lips with falsehood stain. Inclined to mercy they could scan The weakness and the strength of man. 79 Attendants of Indra, eight Gods whose names signify fire, light and its phenomena.
- **Translation**: 

---

### Verse 18 (Ramayana 0.63)
- **Original**: Canto VIII. Sumantra's Speech. 45 They fairly judged both high and low, And ne'er would wrong a guiltless foe; Yet if a fault were proved, each one Would punish e'en his own dear son. But there and in the kingdom's bound No thief or man impure was found: None of loose life or evil fame, No tempter of another's dame. Contented with their lot each caste [015] Calm days in blissful quiet passed; And, all in fitting tasks employed, Country and town deep rest enjoyed, With these wise lords around his throne The monarch justly reigned, And making every heart his own The love of all men gained. With trusty agents, as beseems, Each distant realm he scanned, As the sun visits with his beams Each corner of the land. Ne'er would he on a mightier foe With hostile troops advance, Nor at an equal strike a blow In war's delusive chance. These lords in council bore their part With ready brain and faithful heart, With skill and knowledge, sense and tact, Good to advise and bold to act. And high and endless fame he won With these to guide his schemes, As, risen in his might, the sun Wins glory with his beams.
- **Translation**: 

---

### Verse 19 (Ramayana 0.64)
- **Original**: 46 The Ramayana Canto VIII. Sumantra's Speech. But splendid, just, and great of mind, The childless king for offspring pined. No son had he his name to grace, Transmitter of his royal race. Long had his anxious bosom wrought, And as he pondered rose the thought: “A votive steed 'twere good to slay, So might a son the gift repay.” Before his lords his plan he laid, And bade them with their wisdom aid: Then with these words Sumantra, best Of royal counsellors, addressed: “Hither, Va[ishmha at their head, Let all my priestly guides be led.” To him Sumantra made reply: “Hear, Sire, a tale of days gone by. To many a sage in time of old, Sanatkumár, the saint, foretold How from thine ancient line, O King, A son, when years came round, should spring. “Here dwells,” 'twas thus the seer began, “Of Ka[yap's80 race, a holy man, VibháGdak named: to him shall spring A son, the famous Rishya[ring. Bred with the deer that round him roam, The wood shall be that hermit's home. To him no mortal shall be known Except his holy sire alone. Still by those laws shall he abide 80 Ka [yap was a grandson of the God Brahmá. He is supposed to have given his name to Kashmír = Ka[yapa-míra, Ka[yap's Lake.
- **Translation**: 

---

### Verse 20 (Ramayana 0.65)
- **Original**: Canto VIII. Sumantra's Speech. 47 Which lives of youthful Bráhmans guide, Obedient to the strictest rule That forms the young ascetic's school: And all the wondering world shall hear Of his stern life and penance drear; His care to nurse the holy fire And do the bidding of his sire. Then, seated on the Angas'81 throne, Shall Lomapád to fame be known. But folly wrought by that great king A plague upon the land shall bring; No rain for many a year shall fall And grievous drought shall ruin all. The troubled king with many a prayer Shall bid the priests some cure declare: “The lore of Heaven 'tis yours to know, Nor are ye blind to things below: Declare, O holy men, the way This plague to expiate and stay.” Those best of Bráhmans shall reply: “By every art, O Monarch, try Hither to bring VibháGdak's child, Persuaded, captured, or beguiled. And when the boy is hither led To him thy daughter duly wed.” 81 The people of Anga.“Anga is said in the lexicons to be Bengal; but here certainly another region is intended situated at the confluence of the Sarjú with the Ganges, and not far distant from Da[aratha's dominions.” G ORRESIO {FNS . It comprised part of Behar and Bhagulpur.
- **Translation**: 

---



--- End of Ramayan_batch_101.md ---


--- Start of Ramayan_batch_102.md ---

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

### Verse 1 (Ramayana 0.66)
- **Original**: 48 The Ramayana But how to bring that wondrous boy His troubled thoughts will long employ, And hopeless to achieve the task He counsel of his lords will ask, And bid his priests and servants bring With honour saintly Rishya[ring. But when they hear the monarch's speech, All these their master will beseech, With trembling hearts and looks of woe, To spare them, for they fear to go. And many a plan will they declare And crafty plots will frame, And promise fair to show him there, Unforced, with none to blame. On every word his lords shall say, The king will meditate, And on the third returning day Recall them to debate. Then this shall be the plan agreed, That damsels shall be sent Attired in holy hermits' weed, And skilled in blandishment, That they the hermit may beguile With every art and amorous wile[016] Whose use they know so well, And by their witcheries seduce The unsuspecting young recluse To leave his father's cell. Then when the boy with willing feet Shall wander from his calm retreat And in that city stand, The troubles of the king shall end, And streams of blessed rain descend Upon the thirsty land.
- **Translation**: 

---

### Verse 2 (Ramayana 0.67)
- **Original**: Canto IX. Rishyasring. 49 Thus shall the holy Rishya[ring To Lomapád, the mighty king, By wedlock be allied; For Zántá, fairest of the fair, In mind and grace beyond compare, Shall be his royal bride. He, at the Offering of the Steed, The flames with holy oil shall feed, And for King Da[aratha gain Sons whom his prayers have begged in vain.” “I have repeated, Sire, thus far, The words of old Sanatkumár, In order as he spoke them then Amid the crowd of holy men.” Then Da[aratha cried with joy, “Say how they brought the hermit boy.” Canto IX. Rishyasring. The wise Sumantra, thus addressed, Unfolded at the king's behest The plan the lords in council laid To draw the hermit from the shade: “The priest, amid the lordly crowd, To Lomapád thus spoke aloud: “Hear, King, the plot our thoughts have framed, A harmless trick by all unblamed. Far from the world that hermit's child Lives lonely in the distant wild: A stranger to the joys of sense, His bliss is pain and abstinence;
- **Translation**: 

---

### Verse 3 (Ramayana 0.68)
- **Original**: 50 The Ramayana And all unknown are women yet To him, a holy anchoret. The gentle passions we will wake That with resistless influence shake The hearts of men; and he Drawn by enchantment strong and sweet Shall follow from his lone retreat, And come and visit thee. Let ships be formed with utmost care That artificial trees may bear, And sweet fruit deftly made; Let goodly raiment, rich and rare, And flowers, and many a bird be there Beneath the leafy shade. Upon the ships thus decked a band Of young and lovely girls shall stand, Rich in each charm that wakes desire, And eyes that burn with amorous fire; Well skilled to sing, and play, and dance And ply their trade with smile and glance Let these, attired in hermits' dress, Betake them to the wilderness, And bring the boy of life austere A voluntary captive here.” He ended; and the king agreed, By the priest's counsel won. And all the ministers took heed To see his bidding done. In ships with wondrous art prepared Away the lovely women fared, And soon beneath the shade they stood Of the wild, lonely, dreary wood. And there the leafy cot they found Where dwelt the devotee,
- **Translation**: 

---

### Verse 4 (Ramayana 0.69)
- **Original**: Canto IX. Rishyasring. 51 And looked with eager eyes around The hermit's son to see. Still, of VibháGdak sore afraid, They hid behind the creepers' shade. But when by careful watch they knew The elder saint was far from view, With bolder steps they ventured nigh To catch the youthful hermit's eye. Then all the damsels, blithe and gay, At various games began to play. They tossed the flying ball about With dance and song and merry shout, And moved, their scented tresses bound With wreaths, in mazy motion round. Some girls as if by love possessed, Sank to the earth in feigned unrest, Up starting quickly to pursue Their intermitted game anew. It was a lovely sight to see Those fair ones, as they played, While fragrant robes were floating free, And bracelets clashing in their glee A pleasant tinkling made. The anklet's chime, the Koïl's82 cry With music filled the place As 'twere some city in the sky Which heavenly minstrels grace. With each voluptuous art they strove To win the tenant of the grove, And with their graceful forms inspire 82 The Koïl orkokila(Cuculus Indicus) as the harbinger of spring and love is a universal favourite with Indian poets. His voice when first heard in a glorious spring morning is not unpleasant, but becomes in the hot season intolerably wearisome to European ears.
- **Translation**: 

---

### Verse 5 (Ramayana 0.70)
- **Original**: 52 The Ramayana His modest soul with soft desire. With arch of brow, with beck and smile, With every passion-waking wile[017] Of glance and lotus hand, With all enticements that excite The longing for unknown delight Which boys in vain withstand. Forth came the hermit's son to view The wondrous sight to him so new, And gazed in rapt surprise, For from his natal hour till then On woman or the sons of men He ne'er had cast his eyes. He saw them with their waists so slim, With fairest shape and faultless limb, In variegated robes arrayed, And sweetly singing as they played. Near and more near the hermit drew, And watched them at their game, And stronger still the impulse grew To question whence they came. They marked the young ascetic gaze With curious eye and wild amaze, And sweet the long-eyed damsels sang, And shrill their merry laughter rang. Then came they nearer to his side, And languishing with passion cried: “Whose son, O youth, and who art thou, Come suddenly to join us now? And why dost thou all lonely dwell In the wild wood? We pray thee, tell, We wish to know thee, gentle youth; Come, tell us, if thou wilt, the truth.” He gazed upon that sight he ne'er
- **Translation**: 

---

### Verse 6 (Ramayana 0.71)
- **Original**: Canto IX. Rishyasring. 53 Had seen before, of girls so fair, And out of love a longing rose His sire and lineage to disclose: “My father,” thus he made reply, “Is Ka[yap's son, a saint most high, VibháGdak styled; from him I came, And Rishya[ring he calls my name. Our hermit cot is near this place: Come thither, O ye fair of face; There be it mine, with honour due, Ye gentle youths, to welcome you.” They heard his speech, and gave consent, And gladly to his cottage went. VibháGdak's son received them well Beneath the shelter of his cell With guest-gift, water for their feet, And woodland fruit and roots to eat, They smiled, and spoke sweet words like these, Delighted with his courtesies: “We too have goodly fruit in store, Grown on the trees that shade our door; Come, if thou wilt, kind Hermit, haste The produce of our grove to taste; And let, O good Ascetic, first This holy water quench thy thirst.” They spoke, and gave him comfits sweet Prepared ripe fruits to counterfeit; And many a dainty cate beside And luscious mead their stores supplied. The seeming fruits, in taste and look, The unsuspecting hermit took, For, strange to him, their form beguiled The dweller in the lonely wild. Then round his neck fair arms were flung,
- **Translation**: 

---

### Verse 7 (Ramayana 0.72)
- **Original**: 54 The Ramayana And there the laughing damsels clung, And pressing nearer and more near With sweet lips whispered at his ear; While rounded limb and swelling breast The youthful hermit softly pressed. The pleasing charm of that strange bowl, The touch of a tender limb, Over his yielding spirit stole And sweetly vanquished him. But vows, they said, must now be paid; They bade the boy farewell, And, of the aged saint afraid, Prepared to leave the dell. With ready guile they told him where Their hermit dwelling lay: Then, lest the sire should find them there, Sped by wild paths away. They fled and left him there alone By longing love possessed; And with a heart no more his own He roamed about distressed. The aged saint came home, to find The hermit boy distraught, Revolving in his troubled mind One solitary thought. “Why dost thou not, my son,” he cried, “Thy due obeisance pay? Why do I see thee in the tide Of whelming thought to-day? A devotee should never wear A mien so sad and strange. Come, quickly, dearest child, declare The reason of the change.” And Rishya[ring, when questioned thus,
- **Translation**: 

---

### Verse 8 (Ramayana 0.73)
- **Original**: Canto IX. Rishyasring. 55 Made answer in this wise: “O sire, there came to visit us Some men with lovely eyes. About my neck soft arms they wound And kept me tightly held To tender breasts so soft and round, That strangely heaved and swelled. They sing more sweetly as they dance Than e'er I heard till now, And play with many a sidelong glance And arching of the brow.” “My son,” said he,“thus giants roam Where holy hermits are, And wander round their peaceful home Their rites austere to mar. I charge thee, thou must never lay Thy trust in them, dear boy: They seek thee only to betray, And woo but to destroy.” Thus having warned him of his foes That night at home he spent. And when the morrow's sun arose [018] Forth to the forest went. But Rishya[ring with eager pace Sped forth and hurried to the place Where he those visitants had seen Of daintly waist and charming mien. When from afar they saw the son Of Saint VibháGdak toward them run, To meet the hermit boy they hied, And hailed him with a smile, and cried: “O come, we pray, dear lord, behold Our lovely home of which we told Due honour there to thee we'll pay,
- **Translation**: 

---

### Verse 9 (Ramayana 0.74)
- **Original**: 56 The Ramayana And speed thee on thy homeward way.” Pleased with the gracious words they said He followed where the damsels led. As with his guides his steps he bent, That Bráhman high of worth, A flood of rain from heaven was sent That gladdened all the earth. VibháGdak took his homeward road, And wearied by the heavy load Of roots and woodland fruit he bore Entered at last his cottage door. Fain for his son he looked around, But desolate the cell he found. He stayed not then to bathe his feet, Though fainting with the toil and heat, But hurried forth and roamed about Calling the boy with cry and shout, He searched the wood, but all in vain; Nor tidings of his son could gain. One day beyond the forest's bound The wandering saint a village found, And asked the swains and neatherds there Who owned the land so rich and fair, With all the hamlets of the plain, And herds of kine and fields of grain. They listened to the hermit's words, And all the guardians of the herds, With suppliant hands together pressed, This answer to the saint addressed: “The Angas' lord who bears the name Of Lomapád, renowned by fame, Bestowed these hamlets with their kine
- **Translation**: 

---

### Verse 10 (Ramayana 0.75)
- **Original**: Canto IX. Rishyasring. 57 And all their riches, as a sign Of grace, on Rishya[ring: and he VibháGdak's son is said to be.” The hermit with exulting breast The mighty will of fate confessed, By meditation's eye discerned; And cheerful to his home returned. A stately ship, at early morn, The hermit's son away had borne. Loud roared the clouds, as on he sped, The sky grew blacker overhead; Till, as he reached the royal town, A mighty flood of rain came down. By the great rain the monarch's mind The coming of his guest divined. To meet the honoured youth he went, And low to earth his head he bent. With his own priest to lead the train, He gave the gift high guests obtain. And sought, with all who dwelt within The city walls, his grace to win. He fed him with the daintiest fare, He served him with unceasing care, And ministered with anxious eyes Lest anger in his breast should rise; And gave to be the Bráhman's bride His own fair daughter, lotus-eyed. Thus loved and honoured by the king, The glorious Bráhman Rishya[ring Passed in that royal town his life With Zántá his beloved wife.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.76)
- **Original**: 58 The Ramayana Canto X. Rishyasring Invited. “Again, O best of kings, give ear: My saving words attentive hear, And listen to the tale of old By that illustrious Bráhman told. “Of famed Ikshváku's line shall spring ('Twas thus he spoke) a pious king, Named Da [aratha, good and great, True to his word and fortunate. He with the Angas' mighty lord Shall ever live in sweet accord, And his a daughter fair shall be, Zántá of happy destiny. But Lomapád, the Angas' chief, Still pining in his childless grief, To Da[aratha thus shall say: “Give me thy daughter, friend, I pray, Thy Zántá of the tranquil mind, The noblest one of womankind.” The father, swift to feel for woe, Shall on his friend his child bestow; And he shall take her and depart To his own town with joyous heart. The maiden home in triumph led, To Rishya[ring the king shall wed. And he with loving joy and pride Shall take her for his honoured bride. And Da [aratha to a rite That best of Bráhmans shall invite With supplicating prayer, To celebrate the sacrifice
- **Translation**: 

---

### Verse 12 (Ramayana 0.77)
- **Original**: Canto X. Rishyasring Invited. 59 To win him sons and Paradise,83 That he will fain prepare. [019] From him the lord of men at length The boon he seeks shall gain, And see four sons of boundless strength His royal line maintain.” “Thus did the godlike saint of old The will of fate declare, And all that should befall unfold Amid the sages there. O Prince supreme of men, go thou, Consult thy holy guide, And win, to aid thee in thy vow, This Bráhman to thy side.” Sumantra's counsel, wise and good, King Da[aratha heard, Then by Va[ishmha's side he stood And thus with him conferred: “Sumantra counsels thus: do thou My priestly guide, the plan allow.” Va [ishmha gave his glad consent, And forth the happy monarch went With lords and servants on the road That led to Rishya[ring's abode. Forests and rivers duly past, He reached the distant town at last Of Lomapád the Angas' king, And entered it with welcoming. On through the crowded streets he came, And, radiant as the kindled flame, 83 “Sons and Paradise are intimately connected in Indian belief. A man desires above every thing to have a son to perpetuate his race, and to assist with sacrifices and funeral rites to make him worthy to obtain a lofty seat in heaven or to preserve that which he has already obtained.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 13 (Ramayana 0.78)
- **Original**: 60 The Ramayana He saw within the monarch's house The hermit's son most glorious. There Lomapád, with joyful breast, To him all honour paid, For friendship for his royal guest His faithful bosom swayed. Thus entertained with utmost care Seven days, or eight, he tarried there, And then that best of men thus broke His purpose to the king, and spoke: “O King of men, mine ancient friend, (Thus Da[aratha prayed) Thy Zántá with her husband send My sacrifice to aid.” Said he who ruled the Angas, Yea, And his consent was won: And then at once he turned away To warn the hermit's son. He told him of their ties beyond Their old affection's faithful bond: “This king,” he said,“from days of old A well beloved friend I hold. To me this pearl of dames he gave From childless woe mine age to save, The daughter whom he loved so much, Moved by compassion's gentle touch. In him thyZántás father see: As I am even so is he. For sons the childless monarch yearns: To thee alone for help he turns. Go thou, the sacred rite ordain To win the sons he prays to gain: Go, with thy wife thy succour lend, And give his vows a blissful end.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.79)
- **Original**: Canto X. Rishyasring Invited. 61 The hermit's son with quick accord Obeyed the Angas' mighty lord, And with fairZántá at his side To Da[aratha's city hied. Each king, with suppliant hands upheld, Gazed on the other's face: And then by mutual love impelled Met in a close embrace. Then Da[aratha's thoughtful care, Before he parted thence, Bade trusty servants homeward bear The glad intelligence: “Let all the town be bright and gay With burning incense sweet; Let banners wave, and water lay The dust in every street.” Glad were the citizens to learn The tidings of their lord's return, And through the city every man Obediently his task began. And fair and bright Ayodhyá showed, As following his guest he rode Through the full streets where shell and drum Proclaimed aloud the king was come. And all the people with delight Kept gazing on their king, Attended by that youth so bright, The glorious Rishya[ring. When to his home the king had brought The hermit's saintly son, He deemed that all his task was wrought, And all he prayed for won. And lords who saw that stranger dame So beautiful to view,
- **Translation**: 

---

### Verse 15 (Ramayana 0.80)
- **Original**: 62 The Ramayana Rejoiced within their hearts, and came And paid her honour too. There Rishya[ring passed blissful days, Graced like the king with love and praise And shone in glorious light with her, Sweet Zántá, for his minister, As Brahmá's son Va[ishmha, he Who wedded Saint Arundhatí.84 Canto XI. The Sacrifice Decreed. The Dewy Season85 came and went; The spring returned again: Then would the king, with mind intent, His sacrifice ordain.[020] He came to Rishya[ring, and bowed To him of look divine, And bade him aid his offering vowed For heirs, to save his line. Nor would the youth his aid deny: He spake the monarch fair, And prayed him for that rite so high All requisites prepare. The king to wise Sumantra cried Who stood aye ready near; “Go summon quick each holy guide, To counsel and to hear.” 84 One of the Pleiades and generally regarded as the model of wifely excel- lence. 85 The Hindu year is divided into six seasons of two months each, spring, summer, rains, autumn, winter, and dews.
- **Translation**: 

---

### Verse 16 (Ramayana 0.81)
- **Original**: Canto XI. The Sacrifice Decreed. 63 Obedient to his lord's behest Away Sumantra sped, And brought Va[ishmha and the rest, In Scripture deeply read. Suyajùa, Vámadeva came, Jávali, Ka[yap's son, And old Va[ishmha, dear to fame, Obedient every one. King Da[aratha met them there And duly honoured each, And spoke in pleasant words his fair And salutary speech: “In childless longing doomed to pine, No happiness, O lords, is mine. So have I for this cause decreed To slay the sacrificial steed. Fain would I pay that offering high Wherein the horse is doomed to die, With Rishya[ring his aid to lend, And with your glory to befriend.” With loud applause each holy man Received his speech, approved the plan, And, by the wise Va[ishmha led, Gave praises to the king, and said: “The sons thou cravest shalt thou see, Of fairest glory, born to thee, Whose holy feelings bid thee take This righteous course for offspring's sake.” Cheered by the ready praise of those Whose aid he sought, his spirits rose, And thus the king his speech renewed With looks of joy and gratitude: “Let what the coming rites require Be ready as the priests desire,
- **Translation**: 

---

### Verse 17 (Ramayana 0.82)
- **Original**: 64 The Ramayana And let the horse, ordained to bleed, With fitting guard and priest, be freed,86 Yonder on Sarjú's northern side The sacrificial ground provide; And let the saving rites, that naught Ill-omened may occur, be wrought. The offering I announce to-day Each lord of earth may claim to pay, Provided that his care can guard The holy rite by flaws unmarred. For wandering fiends, whose watchful spite Waits eagerly to spoil each rite, Hunting with keenest eye detect The slightest slip, the least neglect; And when the sacred work is crossed The workman is that moment lost. Let preparation due be made: Your powers the charge can meet: That so the noble rite be paid In every point complete.” And all the Bráhmans answered, Yea, His mandate honouring, And gladly promised to obey The order of the king. They cried with voices raised aloud: “Success attend thine aim!” Then bade farewell, and lowly bowed, And hastened whence they came. King Da[aratha went within, His well loved wives to see: And said:“Your lustral rites begin, 86 It was essential that the horse should wander free for a year before immo- lation, as a sign that his master's paramount sovereignty was acknowledged by all neighbouring princes.
- **Translation**: 

---

### Verse 18 (Ramayana 0.83)
- **Original**: Canto XII. The Sacrifice Begun. 65 For these shall prosper me. A glorious offering I prepare That precious fruit of sons may bear.” Their lily faces brightened fast Those pleasant words to hear, As lilies, when the winter's past, In lovelier hues appear. Canto XII. The Sacrifice Begun. Again the spring with genial heat Returning made the year complete. To win him sons, without delay His vow the king resolved to pay: And to Va[ishmha, saintly man, In modest words this speech began: “Prepare the rite with all things fit As is ordained in Holy Writ, And keep with utmost care afar Whate'er its sacred forms might mar. Thou art, my lord, my trustiest guide, Kind-hearted, and my friend beside; So is it meet thou undertake This heavy task for duty's sake.” Then he, of twice-born men the best, His glad assent at once expressed: “Fain will I do whate'er may be Desired, O honoured King, by thee.” To ancient priests he spoke, who, trained In holy rites, deep skill had gained: “Here guards be stationed, good and sage
- **Translation**: 

---

### Verse 19 (Ramayana 0.84)
- **Original**: 66 The Ramayana Religious men of trusted age. And various workmen send and call, Who frame the door and build the wall: With men of every art and trade, Who read the stars and ply the spade,[021] And mimes and minstrels hither bring, And damsels trained to dance and sing.” Then to the learned men he said, In many a page of Scripture read: “Be yours each rite performed to see According to the king's decree. And stranger Bráhmans quickly call To this great rite that welcomes all. Pavilions for the princes, decked With art and ornament, erect, And handsome booths by thousands made The Bráhman visitors to shade, Arranged in order side by side, With meat and drink and all supplied. And ample stables we shall need For many an elephant and steed: And chambers where the men may lie, And vast apartments, broad and high, Fit to receive the countless bands Of warriors come from distant lands. For our own people too provide Sufficient tents, extended wide, And stores of meat and drink prepare, And all that can be needed there. And food in plenty must be found For guests from all the country round. Of various viands presents make, For honour, not for pity's sake, That fit regard and worship be
- **Translation**: 

---

### Verse 20 (Ramayana 0.85)
- **Original**: Canto XII. The Sacrifice Begun. 67 Paid to each caste in due degree. And let not wish or wrath excite Your hearts the meanest guest to slight; But still observe with special grace Those who obtain the foremost place, Whether for happier skill in art Or bearing in the rite their part. Do you, I pray, with friendly mind Perform the task to you assigned, And work the rite, as bids the law, Without omission, slip, or flaw” They answered:“As thou seest fit So will we do and naught omit.” The sage Va[icmha then addressed Sumantra called at his behest: “The princes of the earth invite, And famous lords who guard the rite, Priest, Warrior, Merchant, lowly thrall, In countless thousands summon all. Where'er their home be, far or near, Gather the good with honour here, And Janak, whose imperial sway The men of Míthilá87 obey. The firm of vow, the dread of foes, Who all the lore of Scripture knows, Invite him here with honour high, King Da[aratha's old ally. And Ká [i's88 lord of gentle speech, Who finds a pleasant word for each, 87 Called also Vidcha, later Tirabhukti, corrupted into the modern Tirhut, a province bounded on the west and east by the Gaudakí and Kau[ikí rivers, on the south by the Ganges, and on the north by the skirts of the Himálayas. 88 The celebrated city of Benares. See Dr. Hall's learned and exhaustive Monograph in theSacred City of the Hindus, by the Rev. M. A. Sherring.
- **Translation**: 

---



--- End of Ramayan_batch_102.md ---


--- Start of Ramayan_batch_103.md ---

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

### Verse 1 (Ramayana 0.86)
- **Original**: 68 The Ramayana In length of days our monarch's peer, Illustrious king, invite him here. The father of our ruler's bride, Known for his virtues far and wide, The king whom Kekaya's89 realms obey, Him with his son invite, I pray. And Lomapád the Angas' king, True to his vows and godlike, bring. For be thine invitations sent To west and south and orient. Call those who rule Suráshmra's90 land, Suvíra's91 realm and Sindhu's strand, And all the kings of earth beside In friendship's bonds with us allied: Invite them all to hasten in With retinue and kith and kin.” Va [ishmha's speech without delay Sumantra bent him to obey. And sent his trusty envoys forth Eastward and westward, south and north. Obedient to the saint's request Himself he hurried forth, and pressed Each nobler chief and lord and king To hasten to the gathering. Before the saint Va[ishmha stood All those who wrought with stone and wood, And showed the work which every one In furtherance of the rite had done, Rejoiced their ready zeal to see, Thus to the craftsmen all said he: 89 Kekaya is supposed to have been in the Panjáb. The name of the king was A [vapati (Lord of Horses), father of Da[aratha's wife Kaikeyí. 90 Surat. 91 Apparently in the west of India not far from the Indus.
- **Translation**: 

---

### Verse 2 (Ramayana 0.87)
- **Original**: Canto XIII. The Sacrifice Finished. 69 “I charge ye, masters, see to this, That there be nothing done amiss, And this, I pray, in mind be borne, That not one gift ye give in scorn: Whenever scorn a gift attends Great sin is his who thus offends.” And now some days and nights had past, And kings began to gather fast, And precious gems in liberal store As gifts to Da[aratha bore. Then joy thrilled through Va[ishmha's breast As thus the monarch he addressed: “Obedient to thy high decree The kings, my lord, are come to thee. [022] And it has been my care to greet And honour all with reverence meet. Thy servants' task is ended quite, And all is ready for the rite. Come forth then to the sacred ground Where all in order will be found.” Then Rishya[ring confirmed the tale: Nor did their words to move him fail. The stars propitious influence lent When forth the world's great ruler went. Then by the sage Va[ishmha led The priest begun to speed Those glorious rites wherein is shed The lifeblood of the steed. Canto XIII. The Sacrifice Finished.
- **Translation**: 

---

### Verse 3 (Ramayana 0.88)
- **Original**: 70 The Ramayana The circling year had filled its course, And back was brought the wandering horse: Then upon Sarjú's northern strand Began the rite the king had planned. With Rishya[ring the forms to guide, The Bráhmans to their task applied, At that great offering of the steed Their lofty-minded king decreed. The priests, who all the Scripture knew, Performed their part in order due, And circled round in solemn train As precepts of the law ordain. Pravargya rites92 were duly sped: For Upasads93 the flames were fed. Then from the plant94 the juice was squeezed, And those high saints with minds well pleased Performed the mystic rites begun With bathing ere the rise of sun They gave the portion Indra's claim, And hymned the King whom none can blame. The mid-day bathing followed next, Observed as bids the holy text. Then the good priests with utmost care, In form that Scripture's rules declare, 92 “The Pravargya ceremony lasts for three days, and is always performed twice a day, in the forenoon and afternoon. It precedes the animal and Soma sacrifices. For without having undergone it, no one is allowed to take part in the solemn Soma feast prepared for the gods.” Haug'sAitareya BráhmaGam . Vol. II. p. 41. noteq.v. 93 Upasads.“The Gods said, Let us perform the burnt offerings called Upasads (i.e.besieging). For by means of anUpasad, i.e.besieging, they conquer a large (fortified) town.”— Ibid.p. 32. 94 The Soma plant, or Asclepias Acida. Its fermented juice was drunk in sacrifice by the priests and offered to the Gods who enjoyed the intoxicating draught.
- **Translation**: 

---

### Verse 4 (Ramayana 0.89)
- **Original**: Canto XIII. The Sacrifice Finished. 71 For the third time pure water shed On high souled Da[aratha's head. Then Rishya[ring and all the rest To Indra and the Gods addressed Their sweet-toned hymn of praise and prayer, And called them in the rite to share. With sweetest song and hymn entoned They gave the Gods in heaven enthroned, As duty bids, the gifts they claim, The holy oil that feeds the flame. And many an offering there was paid, And not one slip in all was made. For with most careful heed they saw That all was done by Veda law. None, all those days, was seen oppressed By hunger or by toil distressed. Why speak of human kind? No beast Was there that lacked an ample feast. For there was store for all who came, For orphan child and lonely dame; The old and young were well supplied, The poor and hungry satisfied. Throughout the day ascetics fed, And those who roam to beg their bread: While all around the cry was still, “Give forth, give forth,” and “Eat your fill.” “Give forth with liberal hand the meal, And various robes in largess deal.” Urged by these cries on every side Unweariedly their task they plied: And heaps of food like hills in size In boundless plenty met the eyes: And lakes of sauce, each day renewed, Refreshed the weary multitude.
- **Translation**: 

---

### Verse 5 (Ramayana 0.90)
- **Original**: 72 The Ramayana And strangers there from distant lands, And women folk in crowded bands The best of food and drink obtained At the great rite the king ordained. Apart from all, the Bráhmans there, Thousands on thousands, took their share Of various dainties sweet to taste, On plates of gold and silver placed, All ready set, as, when they willed, The twice-born men their places filled. And servants in fair garments dressed Waited upon each Bráhman guest. Of cheerful mind and mien were they, With gold and jewelled earrings gay. The best of Bráhmans praised the fare Of countless sorts, of flavour rare: And thus to Raghu's son they cried: “We bless thee, and are satisfied.” Between the rites some Bráhmans spent The time in learned argument,[023] With ready flow of speech, sedate, And keen to vanquish in debate.95 There day by day the holy train Performed all rites as rules ordain. No priest in all that host was found 95 “Tum in cærimoniarum intervallis Brachmanæ facundi, sollertes, crebros sermones de rerum causis instituebant, alter alterum vincendi cupidi. This public disputation in the assembly of Bráhmans on the nature of things, and the almost fraternal connexion between theology and philosophy deserves some notice; whereas the priests of some religions are generally but little inclined to show favour to philosophers, nay, sometimes persecute them with the most rancorous hatred, as we are taught both by history and experience.… This [loka is found in the MSS. of different recensions of the Rámáyan, and we have, therefore, the most trustworthy testimony to the antiquity of philosophy among the Indians.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 6 (Ramayana 0.91)
- **Original**: Canto XIII. The Sacrifice Finished. 73 But kept the vows that held him bound: None, but the holy Vedas knew, And all their six-fold science96 too. No Bráhman there was found unfit To speak with eloquence and wit. And now the appointed time came near The sacrificial posts to rear. They brought them, and prepared to fix Of Bel97 and Khádir98 six and six; Six, made of the Palá[a99 tree, Of Fig-wood one, apart to be: Of Sleshmát100 and of Devadár101 One column each, the mightiest far: So thick the two, the arms of man Their ample girth would fail to span. All these with utmost care were wrought By hand of priests in Scripture taught, And all with gold were gilded bright To add new splendour to the rite: Twenty-and-one those stakes in all, Each one-and-twenty cubits tall: And one-and-twenty ribbons there Hung on the pillars, bright and fair. 96 The Angas or appendices of the Vedas, pronunciation, prosody, grammar, ritual, astronomy, and explanation of obscurities. 97 In Sanskritvilva, theÆgle Marmelos. “He who desires food and wishes to grow fat, ought to make his Yúpa (sacrificial post) of Bilva wood.” Haug's Aítareya Bráhmanam. Vol. II.p. 73. 98 The Mimosa Catechu.“He who desires heaven ought to make his Yúpa of Khádira wood.”— Ibid. 99 The Butea Frondosa.“He who desires beauty and sacred knowledge ought to make his Yúpa of Palá[a wood.”— Ibid. 100 The Cardia Latifolia. 101 A kind of pine. The word means literally the tree of the Gods. Compare the Hebrew “trees of the Lord.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.92)
- **Original**: 74 The Ramayana Firm in the earth they stood at last, Where cunning craftsmen fixed them fast; And there unshaken each remained, Octagonal and smoothly planed. Then ribbons over all were hung, And flowers and scent around them flung. Thus decked they cast a glory forth Like the great saints who star the north.102 The sacrificial altar then Was raised by skilful twice-born men, In shape and figure to behold An eagle with his wings of gold, With twice nine pits and formed three-fold Each for some special God, beside The pillars were the victims tied; The birds that roam the wood, the air, The water, and the land were there, And snakes and things of reptile birth, And healing herbs that spring from earth: As texts prescribe, in Scripture found, Three hundred victims there were bound. The steed devoted to the host Of Gods, the gem they honour most, Was duly sprinkled. Then the Queen Kau [alyá, with delighted mien, With reverent steps around him paced, And with sweet wreaths the victim graced; Then with three swords in order due She smote the steed with joy, and slew. That night the queen, a son to gain, With calm and steady heart was fain By the dead charger's side to stay 102 The Hindus call the constellation of Ursa Major the Seven Rishis or Saints.
- **Translation**: 

---

### Verse 8 (Ramayana 0.93)
- **Original**: Canto XIII. The Sacrifice Finished. 75 From evening till the break of day. Then came three priests, their care to lead The other queens to touch the steed, Upon Kau [alyá to attend, Their company and aid to lend. As by the horse she still reclined, With happy mien and cheerful mind, With Rishya[ring the twice-born came And praised and blessed the royal dame. The priest who well his duty knew, And every sense could well subdue, From out the bony chambers freed And boiled the marrow of the steed. Above the steam the monarch bent, And, as he smelt the fragrant scent, In time and order drove afar All error that his hopes could mar. Then sixteen priests together came And cast into the sacred flame The severed members of the horse, Made ready all in ordered course. On piles of holy Fig-tree raised [024] The meaner victims' bodies blazed: The steed, of all the creatures slain, Alone required a pile of cane. Three days, as is by law decreed, Lasted that Offering of the Steed. The Chatushmom began the rite, And when the sun renewed his light, The Ukthya followed: after came The Atirátra's holy flame. These were the rites, and many more Arranged by light of holy lore, The Aptoryám of mighty power,
- **Translation**: 

---

### Verse 9 (Ramayana 0.94)
- **Original**: 76 The Ramayana And, each performed in proper hour, The Abhijit and Vi[vajit With every form and service fit; And with the sacrifice at night The Jyotishmom and Áyus rite.103 The Atirátra, literally lasting through the night, is a division of the service of the Jyotishmoma. The Abhijit,the everywhere victorious, is the name of a sub-division of the great sacrifice of the Gavámanaya. The Vi[vajit, orthe all-conquering, is a similar sub-division. Áyus is the name of a service forming a division of the Abhiplava sacrifice. The Aptoryám, is the seventh or last part of the Jyotishmoma, for the performance of which it is not essentially necessary, but a voluntary sacrifice instituted for the attainment of a specific desire. The literal meaning of the word would be in conformity with thePrau hamanoramá ,“a sacrifice which procures the attainment of the desired object.” G OLDSTÜCKER 'S D ICTIONARY {FNS . 103 A minute account of these ancient ceremonies would be out of place here. “Ágnishmoma is the name of a sacrifice, or rather a series of offerings to fire for five days. It is the first and principal part of the Jyotishmoma, one of the great sacrifices in which especially the juice of the Soma plant is offered for the pur- pose of obtaining Swarga or heaven.” G OLDSTÜCKER 'S D ICTIONARY {FNS . “The Ágnishmoma is Agni. It is called so because they (the gods) praised him with this Stoma. They called it so to hide the proper meaning of the word: for the gods like to hide the proper meaning of words.” “On account of four classes of gods having praised Agni with four Stomas, the whole was calledChatushmoma (containing four Stomas).” “It (the Ágnishmoma) is calledJyotishmoma , for they praised Agni when he had risen up (to the sky) in the shape of a light (jyotis).” “This (Ágnishmoma) is a sacrificial performance which has no beginning and no end.” H AUG 'S{FNS Aitareya BráhmaGam .
- **Translation**: 

---

### Verse 10 (Ramayana 0.95)
- **Original**: Canto XIII. The Sacrifice Finished. 77 “The Ukthya is a slight modification of the Ágnishmoma sac- rifice. The noun to be supplied to it iskratu. It is a Soma sacrifice also, and one of the seven SaGsthas or component parts of the Jyotishmoma. Its name indicates its nature. ForUkthya means ‘what refers to the Uktha,’which is an older name for Shástra,i.e.recitation of one of the Hotri priests at the time of the Soma libations. Thus this sacrifice is only a kind of supplement to the Ágnishmoma.” H AUG {FNS .Ai. B. The task was done, as laws prescribe: The monarch, glory of his tribe, Bestowed the land in liberal grants Upon the sacred ministrants. He gave the region of the east, His conquest, to the Hotri priest. The west, the celebrant obtained: The south, the priest presiding gained: The northern region was the share Of him who chanted forth the prayer,104 Thus did each priest obtain his meed At the great Slaughter of the Steed, Ordained, the best of all to be, 104 “Four classes of priests were required in India at the most solemn sacrifices. 1. The officiating priests, manual labourers, and acolytes, who had chiefly to prepare the sacrificial ground, to dress the altar, slay the victims, and pour out the libations. 2. The choristers, who chant the sacred hymns. 3. The reciters or readers, who repeat certain hymns. 4. The overseers or bishops, who watch and superintend the proceedings of the other priests, and ought to be familiar with all the Vedas. The formulas and verses to be muttered by the first class are contained in the Yajur-veda-sanhitá. The hymns to be sung by the second class are in the Sama-veda-sanhitá. The Atharva-veda is said to be intended for the Brahman or overseer, who is to watch the proceedings of the sacrifice, and to remedy any mistake that may occur. The hymns to be recited by the third class are contained in the Rigveda,” Chips from a German Workshop.
- **Translation**: 

---

### Verse 11 (Ramayana 0.96)
- **Original**: 78 The Ramayana By self-existent deity. Ikshváku's son with joyful mind This noble fee to each assigned, But all the priests with one accord Addressed that unpolluted lord: “Tis thine alone to keep the whole Of this broad earth in firm control.[025] No gift of lands from thee we seek: To guard these realms our hands were weak. On sacred lore our days are spent: Let other gifts our wants content.” The chief of old Ikshváku's line Gave them ten hundred thousand kine, A hundred millions of fine gold, The same in silver four times told. But every priest in presence there With one accord resigned his share. To Saint Va[ishmha, high of soul, And Rishya[ring they gave the whole. That largess pleased those Bráhmans well, Who bade the prince his wishes tell. Then Da[aratha, mighty king, Made answer thus to Rishya[ring: “O holy Hermit, of thy grace, Vouchsafe the increase of my race.” He spoke; nor was his prayer denied: The best of Bráhmans thus replied: “Four sons, O Monarch, shall be thine, Upholders of thy royal line.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.97)
- **Original**: Canto XIV. Rávan Doomed. 79 Canto XIV. Rávan Doomed. The saint, well read in holy lore, Pondered awhile his answer o'er, And thus again addressed the king, His wandering thoughts regathering: “Another rite will I begin Which shall the sons thou cravest win, Where all things shall be duly sped And first Atharva texts be read.” Then by VibháGdak's gentle son Was that high sacrifice begun, The king's advantage seeking still And zealous to perform his will. Now all the Gods had gathered there, Each one for his allotted share: Brahmá, the ruler of the sky, StháGu, NáráyaG, Lord most high, And holy Indra men might view With Maruts105 for his retinue; The heavenly chorister, and saint, And spirit pure from earthly taint, With one accord had sought the place The high-souled monarch's rite to grace. Then to the Gods who came to take Their proper share the hermit spake: “For you has Da[aratha slain The votive steed, a son to gain; Stern penance-rites the king has tried, And in firm faith on you relied, 105 The Maruts are the winds, deified in the religion of the Veda like other mighty powers and phenomena of nature.
- **Translation**: 

---

### Verse 13 (Ramayana 0.98)
- **Original**: 80 The Ramayana And now with undiminished care A second rite would fain prepare. But, O ye Gods, consent to grant The longing of your supplicant. For him beseeching hands I lift, And pray you all to grant the gift, That four fair sons of high renown The offerings of the king may crown.” They to the hermit's son replied: “His longing shall be gratified. For, Bráhman, in most high degree We love the king and honour thee.” These words the Gods in answer said, And vanished thence by Indra led. Thus to the Lord, the worlds who made, The Immortals all assembled prayed: “O Brahmá, mighty by thy grace, RávaG, who rules the giant race, Torments us in his senseless pride, And penance-loving saints beside. For thou well pleased in days of old Gavest the boon that makes him bold, That God nor demon e'er should kill His charmed life, for so thy will. We, honouring that high behest, Bear all his rage though sore distressed. That lord of giants fierce and fell Scourges the earth and heaven and hell. Mad with thy boon, his impious rage Smites saint and bard and God and sage. The sun himself withholds his glow, The wind in fear forbears to blow; The fire restrains his wonted heat
- **Translation**: 

---

### Verse 14 (Ramayana 0.99)
- **Original**: Canto XIV. Rávan Doomed. 81 Where stand the dreaded RávaG's feet, And, necklaced with the wandering wave, The sea before him fears to rave. Kuvera's self in sad defeat Is driven from his blissful seat. We see, we feel the giant's might, And woe comes o'er us and affright. To thee, O Lord, thy suppliants pray To find some cure this plague to stay.” Thus by the gathered Gods addressed He pondered in his secret breast, And said:“One only way I find To slay this fiend of evil mind. He prayed me once his life to guard From demon, God, and heavenly bard, And spirits of the earth and air, And I consenting heard his prayer. But the proud giant in his scorn Recked not of man of woman born. None else may take his life away, But only man the fiend may slay.” The Gods, with Indra at their head, Rejoiced to hear the words he said. Then crowned with glory like a flame, Lord VishGu to the council came; His hands shell, mace, and discus bore, And saffron were the robes he wore. [026] Riding his eagle through the crowd, As the sun rides upon a cloud, With bracelets of fine gold, he came Loud welcomed by the Gods' acclaim. His praise they sang with one consent, And cried, in lowly reverence bent:
- **Translation**: 

---

### Verse 15 (Ramayana 0.100)
- **Original**: 82 The Ramayana “O Lord whose hand fierce Madhu106 slew, Be thou our refuge, firm and true; Friend of the suffering worlds art thou, We pray thee help thy suppliants now.” Then VishGu spake:“Ye Gods, declare, What may I do to grant your prayer?” “King Da[aratha,” thus cried they, “Fervent in penance many a day, The sacrificial steed has slain, Longing for sons, but all in vain. Now, at the cry of us forlorn, Incarnate as his seed be born. Three queens has he: each lovely dame Like Beauty, Modesty, or Fame. Divide thyself in four, and be His offspring by these noble three. Man's nature take, and slay in fight RávaG who laughs at heavenly might: This common scourge, this rankling thorn Whom the three worlds too long have borne For RávaG in the senseless pride Of might unequalled has defied The host of heaven, and plagues with woe Angel and bard and saint below, Crushing each spirit and each maid Who plays in Nandan's107 heavenly shade. O conquering Lord, to thee we bow; Our surest hope and trust art thou. Regard the world of men below, And slay the Gods' tremendous foe.” 106 A Titan or fiend whose destruction has given VishGu one of his well-known titles, Mádhava. 107 The garden of Indra.
- **Translation**: 

---

### Verse 16 (Ramayana 0.101)
- **Original**: Canto XIV. Rávan Doomed. 83 When thus the suppliant Gods had prayed, His wise reply NáráyaG108 made: “What task demands my presence there, And whence this dread, ye Gods declare.” The Gods replied:“We fear, O Lord, Fierce RávaG, ravener abhorred. Be thine the glorious task, we pray, In human form this fiend to slay. By thee of all the Blest alone This sinner may be overthrown. He gained by penance long and dire The favour of the mighty Sire. Then He who every gift bestows Guarded the fiend from heavenly foes, And gave a pledge his life that kept From all things living, man except. On him thus armed no other foe Than man may deal the deadly blow. Assume, O King, a mortal birth, And strike the demon to the earth.” Then VishGu, God of Gods, the Lord Supreme by all the worlds adored, To Brahmá and the suppliants spake: “Dismiss your fear: for your dear sake In battle will I smite him dead, The cruel fiend, the Immortal's dread. And lords and ministers and all His kith and kin with him shall fall. Then, in the world of mortal men, 108 One of the most ancient and popular of the numerous names of VishGu. The word has been derived in several ways, and may meanhe who moved on the (primordial) waters, orhe who pervades or influences men or their thoughts.
- **Translation**: 

---

### Verse 17 (Ramayana 0.102)
- **Original**: 84 The Ramayana Ten thousand years and hundreds ten I as a human king will reign, And guard the earth as my domain.” God, saint, and nymph, and minstrel throng With heavenly voices raised their song In hymns of triumph to the God Whose conquering feet on Madhu trod: “Champion of Gods, as man appear, This cruel RávaG slay, The thorn that saints and hermits fear, The plague that none can stay. In savage fury uncontrolled His pride for ever grows: He dares the Lord of Gods to hold Among his deadly foes.” Canto XV. The Nectar. When wisest VishGu thus had given His promise to the Gods of heaven, He pondered in his secret mind A suited place of birth to find, Then he decreed, the lotus-eyed, In four his being to divide, And Da [aratha, gracious king, He chose as sire from whom to spring. That childless prince of high renown, Who smote in war his foemen down, At that same time with utmost care
- **Translation**: 

---

### Verse 18 (Ramayana 0.103)
- **Original**: Canto XV. The Nectar. 85 Prepared the rite that wins an heir.109 Then VishGu, fain on earth to dwell, Bade the Almighty Sire farewell, And vanished while a reverent crowd Of Gods and saints in worship bowed. The monarch watched the sacred rite, When a vast form of awful might, Of matchless splendour, strength, and size Was manifest before his eyes. [027] From forth the sacrificial flame, Dark, robed in red, the being came. His voice was drumlike, loud and low, His face suffused with rosy glow. Like a huge lion's mane appeared The long locks of his hair and beard. He shone with many a lucky sign, And many an ornament divine; A towering mountain in his height, A tiger in his gait and might. No precious mine more rich could be, No burning flame more bright than he. His arms embraced in loving hold, Like a dear wife, a vase of gold Whose silver lining held a draught Of nectar as in heaven is quaffed: A vase so vast, so bright to view, They scarce could count the vision true. Upon the king his eyes he bent, And said:“The Lord of life has sent His servant down, O Prince, to be A messenger from heaven to thee.” The king with all his nobles by 109 The Horse-Sacrifice, just described.
- **Translation**: 

---

### Verse 19 (Ramayana 0.104)
- **Original**: 86 The Ramayana Raised reverent hands and made reply: “Welcome, O glorious being! Say How can my care thy grace repay.” Envoy of Him whom all adore Thus to the king he spake once more: “The Gods accept thy worship: they Give thee the blessed fruit to-day. Approach and take, O glorious King, This heavenly nectar which I bring, For it shall give thee sons and wealth, And bless thee with a store of health. Give it to those fair queens of thine, And bid them quaff the drink divine: And they the princely sons shall bear Long sought by sacrifice and prayer.” “Yea, O my lord,” the monarch said, And took the vase upon his head, The gift of Gods, of fine gold wrought, With store of heavenly liquor fraught. He honoured, filled with transport new, That wondrous being, fair to view, As round the envoy of the God With reverential steps he trod.110 His errand done, that form of light 110 To walk round an object keeping the right side towards it is a mark of great respect. The Sanskrit word for the observance ispradakshiGá, from pra pro, anddaksha right, Greek´µ¾w¿Â, Latin dexter, Gaelic deas-il. A similar ceremony is observed by the Gaels. “In the meantime she traced around him, with wavering steps, the propitia- tion, which some have thought has been derived from the Druidical mythology. It consists, as is well known, in the person who makes thedeasilwalking three times round the person who is the object of the ceremony, taking care to move according to the course of the sun.” SCOTT {FNS .The Two Drovers.
- **Translation**: 

---

### Verse 20 (Ramayana 0.105)
- **Original**: Canto XV. The Nectar. 87 Arose and vanished from the sight. High rapture filled the monarch's soul, Possessed of that celestial bowl, As when a man by want distressed With unexpected wealth is blest. And rays of transport seemed to fall Illuminating bower and hall, As when the autumn moon rides high, And floods with lovely light the sky. Quick to the ladies' bower he sped, And thus to Queen Kau[alyá said: “This genial nectar take and quaff,” He spoke, and gave the lady half. Part of the nectar that remained Sumitrá from his hand obtained. He gave, to make her fruitful too, Kaikeyí half the residue. A portion yet remaining there, He paused awhile to think. Then gave Sumitrá, with her share. The remnant of the drink. Thus on each queen of those fair three A part the king bestowed, And with sweet hope a child to see Their yearning bosoms glowed. The heavenly bowl the king supplied Their longing souls relieved, And soon, with rapture and with pride, Each royal dame conceived. He gazed upon each lady's face, And triumphed as he gazed, As Indra in his royal place By Gods and spirits praised.
- **Translation**: 

---



--- End of Ramayan_batch_103.md ---


--- Start of Ramayan_batch_104.md ---

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

### Verse 1 (Ramayana 0.106)
- **Original**: 88 The Ramayana Canto XVI. The Vánars. When VishGu thus had gone on earth, From the great king to take his birth, The self-existent Lord of all Addressed the Gods who heard his call: “For VishGu's sake, the strong and true, Who seeks the good of all of you, Make helps, in war to lend him aid, In forms that change at will, arrayed, Of wizard skill and hero might, Outstrippers of the wind in flight, Skilled in the arts of counsel, wise, And VishGu's peers in bold emprise; With heavenly arts and prudence fraught, By no devices to be caught; Skilled in all weapon's lore and use As they who drink the immortal juice.111[028] And let the nymphs supreme in grace, And maidens of the minstrel race, Monkeys and snakes, and those who rove Free spirits of the hill and grove, And wandering Daughters of the Air, In monkey form brave children bear. So erst the lord of bears I shaped, Born from my mouth as wide I gaped.” 111 The Amrit, the nectar of the Indian Gods.
- **Translation**: 

---

### Verse 2 (Ramayana 0.107)
- **Original**: Canto XVI. The Vánars. 89 Thus by the mighty Sire addressed They all obeyed his high behest, And thus begot in countless swarms Brave sons disguised in sylvan forms. Each God, each sage became a sire, Each minstrel of the heavenly quire,112 Each faun,113 of children strong and good Whose feet should roam the hill and wood. Snakes, bards,114 and spirits,115 serpents bold Had sons too numerous to be told. Báli, the woodland hosts who led, High as Mahendra's116 lofty head, Was Indra's child. That noblest fire, The Sun, was great Sugríva's sire, Tára, the mighty monkey, he Was offspring of V[ihaspati:117 Tára the matchless chieftain, boast For wisdom of the Vánar host. Of Gandhamádan brave and bold The father was the Lord of Gold. 112 Gandharvas (Southey's Glendoveers) are celestial musicians inhabiting In- dra's heaven and forming the orchestra at all the banquets of the principal deities. 113 Yakshas, demigods attendant especially on Kuvera, and employed by him in the care of his garden and treasures. 114 Kimpurushas, demigods attached also to the service of Kuvera, celestial musicians, represented like centaurs reversed with human figures and horses' heads. 115 Siddhas, demigods or spirits of undefined attributes, occupying with the Vidyádharasthe middle air or region between the earth and the sun. Schlegel translates:“Divi, Sapientes, Fidicines, Præpetes, illustres Genii, Præconesque procrearunt natos, masculos, silvicolas; angues porro, Hip- pocephali Beati, Aligeri, Serpentesque frequentes alacriter generavere prolem innumerabilem.” 116 A mountain in the south of India. 117 The preceptor of the Gods and regent of the planet Jupiter.
- **Translation**: 

---

### Verse 3 (Ramayana 0.108)
- **Original**: 90 The Ramayana Nala the mighty, dear to fame, Of skilful Vi[vakarmá118 came. From Agni,119 Nila bright as flame, Who in his splendour, might, and worth, Surpassed the sire who gave him birth. The heavenly A[vins,120 swift and fair, Were fathers of a noble pair, Who, Dwivida and Mainda named, For beauty like their sires were famed, VaruG121 was father of SusheG, Of Sarabh, he who sends the rain,122 Hanúmán, best of monkey kind, Was son of him who breathes the wind: Like thunderbolt in frame was he, And swift as Garu 's123 self could flee. These thousands did the Gods create Endowed with might that none could mate, In monkey forms that changed at will; So strong their wish the fiend to kill. In mountain size, like lions thewed, Up sprang the wondrous multitude, Auxiliar hosts in every shape, Monkey and bear and highland ape. In each the strength, the might, the mien Of his own parent God were seen. 118 The celestial architect, the Indian Hephæstus, Mulciber, or Vulcan. 119 The God of Fire. 120 Twin children of the Sun, the physicians of Swarga or Indra's heaven. 121 The deity of the waters. 122 Parjanya, sometimes confounded with Indra. 123 The bird and vehicle of VishGu. He is generally represented as a being something between a man and a bird and considered as the sovereign of the feathered race. He may be compared with the Simurgh of the Persians, the 'Anká of the Arabs, the Griffin of chivalry, the Phœ nix of Egypt, and the bird that sits upon the ash Yggdrasil of the Edda.
- **Translation**: 

---

### Verse 4 (Ramayana 0.109)
- **Original**: Canto XVI. The Vánars. 91 Some chiefs of Vánar mothers came, Some of she-bear and minstrel dame, Skilled in all arms in battle's shock; The brandished tree, the loosened rock; And prompt, should other weapons fail, To fight and slay with tooth and nail. Their strength could shake the hills amain, And rend the rooted trees in twain, Disturb with their impetuous sweep The Rivers' Lord, the Ocean deep, Rend with their feet the seated ground, And pass wide floods with airy bound, Or forcing through the sky their way The very clouds by force could stay. Mad elephants that wander through The forest wilds, could they subdue, And with their furious shout could scare Dead upon earth the birds of air. So were the sylvan chieftains formed; Thousands on thousands still they swarmed. These were the leaders honoured most, The captains of the Vánar host, And to each lord and chief and guide Was monkey offspring born beside. Then by the bears' great monarch stood The other roamers of the wood, [029] And turned, their pathless homes to seek, To forest and to mountain peak. The leaders of the monkey band By the two brothers took their stand, Sugríva, offspring of the Sun And Báli, Indra's mighty one. They both endowed with Garu 's might, And skilled in all the arts of fight,
- **Translation**: 

---

### Verse 5 (Ramayana 0.110)
- **Original**: 92 The Ramayana Wandered in arms the forest through, And lions, snakes, and tigers, slew. But every monkey, ape, and bear Ever was Báli's special care; With his vast strength and mighty arm He kept them from all scathe and harm. And so the earth with hill, wood, seas, Was filled with mighty ones like these, Of various shape and race and kind, With proper homes to each assigned, With Ráma's champions fierce and strong The earth was overspread, High as the hills and clouds, a throng With bodies vast and dread.124 Canto XVII. Rishyasring's Return. Now when the high-souled monarch's rite, The A[vamedh, was finished quite, Their sacrificial dues obtained, The Gods their heavenly homes regained. The lofty-minded saints withdrew, Each to his place, with honour due, And kings and chieftains, one and all, 124 This Canto will appear ridiculous to the European reader. But it should be remembered that the monkeys of an Indian forest, the“bough-deer” as the poets call them, are very different animals from the“turpissima bestia” that accompanies the itinerant organ-grinder or grins in the Zoological Gardens of London. Milton has made his hero, Satan, assume the forms of a cormorant, a toad, and a serpent, and I cannot see that this creation of semi-divine Vánars, or monkeys, is more ridiculous or undignified.
- **Translation**: 

---

### Verse 6 (Ramayana 0.111)
- **Original**: Canto XVII. Rishyasring's Return. 93 Who came to grace the festival. And Da [aratha, ere they went, Addressed them thus benevolent: “Now may you, each with joyful heart, To your own realms, O Kings, depart. Peace and good luck attend you there, And blessing, is my friendly prayer; Let cares of state each mind engage To guard his royal heritage. A monarch from his throne expelled No better than the dead is held. So he who cares for power and might Must guard his realm and royal right. Such care a meed in heaven will bring Better than rites and offering. Such care a king his country owes As man upon himself bestows, When for his body he provides Raiment and every need besides. For future days should kings foresee, And keep the present error-free.” Thus did the king the kings exhort: They heard, and turned them from the court And, each to each in friendship bound, Went forth to all the realms around. The rites were o'er, the guests were sped: The train the best of Bráhmans led, In which the king with joyful soul, With his dear wives, and with the whole Of his imperial host and train Of cars and servants turned again, And, as a monarch dear to fame, Within his royal city came.
- **Translation**: 

---

### Verse 7 (Ramayana 0.112)
- **Original**: 94 The Ramayana Next, Rishya[ring, well-honoured sage, And Zántá, sought their hermitage. The king himself, of prudent mind, Attended him, with troops behind. And all her men the town outpoured With Saint Va[ishmha and their lord. High mounted on a car of state, O'er canopied fairZántá sate. Drawn by white oxen, while a band Of servants marched on either hand. Great gifts of countless price she bore, With sheep and goats and gems in store. Like Beauty's self the lady shone With all the jewels she had on, As, happy in her sweet content, Peerless amid the fair she went. Not Queen Paulomí's125 self could be More loving to her lord than she. She who had lived in happy ease, Honoured with all her heart could please, While dames and kinsfolk ever vied To see her wishes gratified, Soon as she knew her husband's will Again to seek the forest, still Was ready for the hermit's cot, Nor murmured at her altered lot. The king attended to the wild That hermit and his own dear child, And in the centre of a throng Of noble courtiers rode along. The sage's son had let prepare A lodge within the wood, and there 125 The consort of Indra, called alsoZachí and IndráGí.
- **Translation**: 

---

### Verse 8 (Ramayana 0.113)
- **Original**: Canto XVII. Rishyasring's Return. 95 While they lingered blithe and gay. Then, duly honoured, went their way. The glorious hermit Rishya[ring Drew near and thus besought the king: [030] “Return, my honoured lord, I pray, Return, upon thy homeward way.” The monarch, with the waiting crowd, Lifted his voice and wept aloud, And with eyes dripping still to each Of his good queens he spake this speech: “Kau [alyá and Sumitrá dear, And thou, my sweet Kaikeyí, hear. All uponZántá feast your gaze, The last time for a length of days.” To Zántá's arms the ladies leapt, And hung about her neck and wept, And cried,“O, happy be the life Of this great Bráhman and his wife. The Wind, the Fire, the Moon on high, The Earth, the Streams, the circling Sky, Preserve thee in the wood, true spouse, Devoted to thy husband's vows. And O dearZántá, ne'er neglect To pay the dues of meek respect To the great saint, thy husband's sire, With all observance and with fire. And, sweet one, pure of spot and blame, Forget not thou thy husband's claim; In every change, in good and ill, Let thy sweet words delight him still, And let thy worship constant be: Her lord is woman's deity.
- **Translation**: 

---

### Verse 9 (Ramayana 0.114)
- **Original**: 96 The Ramayana To learn thy welfare, dearest friend, The king will many a Bráhman send. Let happy thoughts thy spirit cheer, And be not troubled, daughter dear.” These soothing words the ladies said. And pressed their lips upon her head. Each gave with sighs her last adieu, Then at the king's command withdrew. The king around the hermit went With circling footsteps reverent, And placed at Rishya[ring's command Some soldiers of his royal band. The Bráhman bowed in turn and cried, “May fortune never leave thy side. O mighty King, with justice reign, And still thy people's love retain.” He spoke, and turned away his face, And, as the hermit went, The monarch, rooted to the place, Pursued with eyes intent. But when the sage had past from view King Da[aratha turned him too, Still fixing on his friend each thought. With such deep love his breast was fraught. Amid his people's loud acclaim Home to his royal seat he came, And lived delighted there, Expecting when each queenly dame, Upholder of his ancient fame, Her promised son should bear. The glorious sage his way pursued Till close before his eyes he viewed Sweet Champá, Lomapád's fair town,
- **Translation**: 

---

### Verse 10 (Ramayana 0.115)
- **Original**: Canto XVIII. Rishyasring's Departure. 97 Wreathed with her Champacs'126 leafy crown. Soon as the saint's approach he knew, The king, to yield him honour due, Went forth to meet him with a band Of priests and nobles of the land: “Hail, Sage,” he cried,“O joy to me! What bliss it is, my lord, to see Thee with thy wife and all thy train Returning to my town again. Thy father, honoured Sage, is well, Who hither from his woodland cell Has sent full many a messenger For tidings both of thee and her.” Then joyfully, for due respect, The monarch bade the town be decked. The king and Rishya[ring elate Entered the royal city's gate: In front the chaplain rode. Then, loved and honoured with all care By monarch and by courtier, there The glorious saint abode. Canto XVIII. Rishyasring's Departure. 126 The Michelia champaca. It bears a scented yellow blossom: “The maid of India blest again to hold In her full lap the Champac's leaves of gold.” Lallah Rookh.
- **Translation**: 

---

### Verse 11 (Ramayana 0.116)
- **Original**: 98 The Ramayana The monarch called a Bráhman near And said,“Now speed away To Ka[yap's son,127 the mighty seer, And with all reverence say The holy child he holds so dear, The hermit of the noble mind, Whose equal it were hard to find, Returned, is dwelling here. Go, and instead of me do thou Before that best of hermits bow, That still he may, for his dear son, Show me the favour I have won.” Soon as the king these words had said, To Ka[yap's son the Bráhman sped. Before the hermit low he bent And did obeisance, reverent; Then with meek words his grace to crave The message of his lord he gave: “The high-souled father of his bride Had called thy son his rites to guide: Those rites are o'er, the steed is slain; Thy noble child is come again.” Soon as the saint that speech had heard His spirit with desire was stirred To seek the city of the king And to his cot his son to bring.[031] With young disciples at his side Forth on his way the hermit hied, While peasants from their hamlets ran To reverence the holy man. Each with his little gift of food, Forth came the village multitude, 127 VibháGdak, the father of Rishya[ring
- **Translation**: 

---

### Verse 12 (Ramayana 0.117)
- **Original**: Canto XVIII. Rishyasring's Departure. 99 And, as they humbly bowed the head, “What may we do for thee?” they said. Then he, of Bráhmans first and best, The gathered people thus addressed: “Now tell me for I fain would know, Why is it I am honoured so?” They to the high-souled saint replied: “Our ruler is with thee allied. Our master's order we fulfil; O Bráhman, let thy mind be still.” With joy the saintly hermit heard Each pleasant and delightful word, And poured a benediction down On king and ministers and town. Glad at the words of that high saint Some servants hastened to acquaint Their king, rejoicing to impart The tidings that would cheer his heart. Soon as the joyful tale he knew To meet the saint the monarch flew, The guest-gift in his hand he brought, And bowed before him and besought: “This day by seeing thee I gain Not to have lived my life in vain, Now be not wroth with me, I pray, “Because I wiled thy son away.128 128 A hemi[loka is wanting in Schlegel's text, which he thus fills up in his Latin translation.
- **Translation**: 

---

### Verse 13 (Ramayana 0.118)
- **Original**: 100 The Ramayana The best of Bráhmans answer made: “Be not, great lord of kings, afraid. Thy virtues have not failed to win My favour, O thou pure of sin.” Then in the front the saint was placed, The king came next in joyous haste, And with him entered his abode, Mid glad acclaim as on they rode. To greet the sage the reverent crowd Raised suppliant hands and humbly bowed. Then from the palace many a dame Following well-dressedZántá came, Stood by the mighty saint and cried: “See, honour's source, thy son's dear bride.” The saint, who every virtue knew, His arms around his daughter threw, And with a father's rapture pressed The lady to his wondering breast. Arising from the saint's embrace She bowed her low before his face, And then, with palm to palm applied, Stood by her hermit father's side. He for his son, as laws ordain, Performed the rite that frees from stain,129 And, honoured by the wise and good, With him departed to the wood. Canto XIX. The Birth Of The Princes. 129 Rishya[ring, a Bráhman, had marriedZántá who was of the Kshatriya or Warrior caste and an expiatory ceremony was necessary on account of this violation of the law.
- **Translation**: 

---

### Verse 14 (Ramayana 0.119)
- **Original**: Canto XIX. The Birth Of The Princes. 101 The seasons six in rapid flight Had circled since that glorious rite. Eleven months had passed away; 'Twas Chaitra's ninth returning day.130 The moon within that mansion shone Which Aditi looks kindly on. Raised to their apex in the sky Five brilliant planets beamed on high. Shone with the moon, in Cancer's sign, V [ihaspati131 with light divine. Kau [alyá bore an infant blest With heavenly marks of grace impressed; Ráma, the universe's lord, A prince by all the worlds adored. New glory Queen Kau[alyá won Reflected from her splendid son. So Aditi shone more and more, The Mother of the Gods, when she The King of the Immortals132 bore, The thunder-wielding deity. [032] 130 “The poet no doubt intended to indicate the vernal equinox as the birthday of Ráma. For the monthChaitrais the first of the two months assigned to the spring; it corresponds with the latter half of March and the former half of April in our division of the year.Aditi, the mother of the Gods, is lady of the seventh lunar mansion which is calledPunarvasu. The five planets and their positions in the Zodiac are thus enumerated by both commentators: the Sun in Aries, Mars in Capricorn, Saturn in Libra, Jupiter in Cancer, Venus in Pisces.… I leave to astronomers to examine whether the parts of the description agree with one another, and, if this be the case, thence to deduce the date. The Indians place the nativity of Ráma in the confines of the second age (tretá) and the third (dwápara): but it seems that this should be taken in an allegorical sense.… We may consider that the poet had an eye to the time in which, immediately before his own age, the aspects of the heavenly bodies were such as he has described.” SCHLEGEL {FNS . 131 The regent of the planet Jupiter. 132 Indra = Jupiter Tonans.
- **Translation**: 

---

### Verse 15 (Ramayana 0.120)
- **Original**: 102 The Ramayana The lotus-eyed, the beauteous boy, He came fierce RávaG to destroy; From half of VishGu's vigour born, He came to help the worlds forlorn. And Queen Kaikeyí bore a child Of truest valour, Bharat styled, With every princely virtue blest, One fourth of VishGu manifest. Sumitrá too a noble pair, Called LakshmaG and Zatrughna, bare, Of high emprise, devoted, true, Sharers in VishGu's essence too. 'Neath Pushya's133 mansion, Mina's134 sign, Was Bharat born, of soul benign. The sun had reached the Crab at morn When Queen Sumitrá's babes were born, What time the moon had gone to make His nightly dwelling with the Snake. The high-souled monarch's consorts bore At different times those glorious four, Like to himself and virtuous, bright As Proshmhapadá's135 four-fold light. Then danced the nymphs' celestial throng, The minstrels raised their strain; The drums of heaven pealed loud and long, And flowers came down in rain. Within Ayodhyá, blithe and gay, All kept the joyous holiday. 133 “Pushya is the name of a month; but here it means the eighth mansion. The ninth is calledAsleshá, or the snake. It is evident from this that Bharat, though his birth is mentioned before that of the twins, was the youngest of the four brothers and Ráma's junior by eleven months.” SCHLEGEL {FNS . 134 A fish, the Zodiacal signPisces. 135 One of the constellations, containing stars in the wing of Pegasus.
- **Translation**: 

---

### Verse 16 (Ramayana 0.121)
- **Original**: Canto XIX. The Birth Of The Princes. 103 The spacious square, the ample road With mimes and dancers overflowed, And with the voice of music rang Where minstrels played and singers sang, And shone, a wonder to behold, With dazzling show of gems and gold. Nor did the king his largess spare, For minstrel, driver, bard, to share; Much wealth the Bráhmans bore away, And many thousand dine that day. Soon as each babe was twelve days old 'Twas time the naming rite to hold. When Saint Va[ishmha, rapt with joy, Assigned a name to every boy. Ráma, to him the high-souled heir, Bharat, to him Kaikeyí bare: Of Queen Sumitrá one fair son Was Lakshma G, andZatrughna136 one Ráma, his sire's supreme delight, Like some proud banner cheered his sight, And to all creatures seemed to be The self-existent deity. All heroes, versed in holy lore, To all mankind great love they bore. Fair stores of wisdom all possessed, With princely graces all were blest. But mid those youths of high descent, With lordly light preëminent. Like the full moon unclouded, shone Ráma, the world's dear paragon. 136 Ráma means the Delight (of the World); Bharat, the Supporter; LakshmaG, the Auspicious;Zatrughna, the Slayer of Foes.
- **Translation**: 

---

### Verse 17 (Ramayana 0.122)
- **Original**: 104 The Ramayana He best the elephant could guide.137 Urge the fleet car, the charger ride: A master he of bowman's skill, Joying to do his father's will. The world's delight and darling, he Loved LakshmaG best from infancy And Lakshma G, lord of lofty fate, Upon his elder joyed to wait, Striving his second self to please With friendship's sweet observances. His limbs the hero ne'er would rest Unless the couch his brother pressed; Except beloved Ráma shared He could not taste the meal prepared. When Ráma, pride of Reghu's race, Sprang on his steed to urge the chase, Behind him LakshmaG loved to go And guard him with his trusty bow. As Ráma was to LakshmaG dear More than his life and ever near, So fondZatrughna prized above His very life his Bharat's love. Illustrious heroes, nobly kind In mutual love they all combined, And gave their royal sire delight With modest grace and warrior might: Supported by the glorious four Shone Da[aratha more and more, As though, with every guardian God 137 Schlegel, in theIndische Bibliothek, remarks that the proficiency of the Indians in this art early attracted the attention of Alexander's successors, and natives of India were so long exclusively employed in this service that the name Indian was applied to any elephant-driver, to whatever country he might belong.
- **Translation**: 

---

### Verse 18 (Ramayana 0.123)
- **Original**: Canto XX. Visvámitra's Visit. 105 Who keeps the land and skies, The Father of all creatures trod The earth before men's eyes. Canto XX. Visvámitra's Visit. Now Da [aratha's pious mind Meet wedlock for his sons designed; [033] With priests and friends the king began To counsel and prepare his plan. Such thoughts engaged his bosom, when, To see Ayodhyá's lord of men, A mighty saint of glorious fame, The hermit Vi[vámitra138 came. For evil fiends that roam by night Disturbed him in each holy rite, And in their strength and frantic rage Assailed with witcheries the sage. He came to seek the monarch's aid To guard the rites the demons stayed, Unable to a close to bring One unpolluted offering. Seeking the king in this dire strait He said to those who kept the gate: “Haste, warders, to your master run, And say that here stands Gádhi's son.” 138 The story of this famous saint is given at sufficient length in Cantos LI-LV. This saint has given his name to the district and city to the east of Benares. The original name, preserved in a land-grant on copper now in the Museum of the Benares College, has been Moslemized into Ghazeepore (the City of the Soldier-martyr).
- **Translation**: 

---

### Verse 19 (Ramayana 0.124)
- **Original**: 106 The Ramayana Soon as they heard the holy man, To the king's chamber swift they ran With minds disordered all, and spurred To wildest zeal by what they heard. On to the royal hall they sped, There stood and lowly bowed the head, And made the lord of men aware That the great saint was waiting there. The king with priest and peer arose And ran the sage to meet, As Indra from his palace goes Lord Brahmá's self to greet. When glowing with celestial light The pious hermit was in sight, The king, whose mien his transport showed, The honoured gift for guests bestowed. Nor did the saint that gift despise, Offered as holy texts advise; He kindly asked the earth's great king How all with him was prospering. The son of Ku[ik139 bade him tell If all in town and field were well, All well with friends, and kith and kin, And royal treasure stored within: “Do all thy neighbours own thy sway? Thy foes confess thee yet? Dost thou continue still to pay To Gods and men each debt?” Then he, of hermits first and best, Va [ishmha with a smile140 addressed, And asked him of his welfare too, Showing him honour as was due. 139 The son of Ku[ik is Vi[vámitra. 140 At the recollection of their former enmity, to be described hereafter.
- **Translation**: 

---

### Verse 20 (Ramayana 0.125)
- **Original**: Canto XX. Visvámitra's Visit. 107 Then with the sainted hermit all Went joyous to the monarch's hall, And sate them down by due degree, Each one, of rank and dignity. Joy filled the noble prince's breast Who thus bespoke the honoured guest: “As amrit141 by a mortal found, As rain upon the thirsty ground, As to an heirless man a son Born to him of his precious one, As gain of what we sorely miss, As sudden dawn of mighty bliss, So is thy coming here to me: All welcome, mighty Saint, to thee. What wish within thy heart hast thou? If I can please thee, tell me how. Hail, Saint, from whom all honours flow, Worthy of all I can bestow. Blest is my birth with fruit to-day, Nor has my life been thrown away. I see the best of Bráhman race And night to glorious morn gives place. Thou, holy Sage, in days of old Among the royal saints enrolled, Didst, penance-glorified, within The Bráhman caste high station win. 'Tis meet and right in many a way That I to thee should honour pay. This seems a marvel to mine eyes: All sin thy visit purifies; And I by seeing thee, O Sage, Have reaped the fruit of pilgrimage. 141 The Indian nectar or drink of the Gods.
- **Translation**: 

---



--- End of Ramayan_batch_104.md ---


--- Start of Ramayan_batch_105.md ---

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

### Verse 1 (Ramayana 0.126)
- **Original**: 108 The Ramayana Then say what thou wouldst have me do, That thou hast sought this interview. Favoured by thee, my wish is still, O Hermit, to perform thy will. Nor needest thou at length explain The object that thy heart would gain. Without reserve I grant it now: My deity, O Lord, art thou.” The glorious hermit, far renowned, With highest fame and virtue crowned, Rejoiced these modest words to hear Delightful to the mind and ear. Canto XXI. Visvámitra's Speech. The hermit heard with high content That speech so wondrous eloquent, And while each hair with joy arose,142[034] 142 Great joy, according to the Hindu belief, has this effect, not causing each particular hair to stand on end, but gently raising all the down upon the body.
- **Translation**: 

---

### Verse 2 (Ramayana 0.127)
- **Original**: Canto XXI. Visvámitra's Speech. 109 He thus made answer at the close: “Good is thy speech O noble King, And like thyself in everything. So should their lips be wisdom-fraught Whom kings begot, Va[ishmha taught. The favour which I came to seek Thou grantest ere my tongue can speak. But let my tale attention claim, And hear the need for which I came. O King, as Scripture texts allow, A holy rite employs me now. Two fiends who change their forms at will Impede that rite with cursed skill.143 Oft when the task is nigh complete, These worst of fiends my toil defeat, Throw bits of bleeding flesh, and o'er The altar shed a stream of gore. When thus the rite is mocked and stayed, And all my pious hopes delayed, Cast down in heart the spot I leave, And spent with fruitless labour grieve. Nor can I, checked by prudence, dare Let loose my fury on them there: The muttered curse, the threatening word, In such a rite must ne'er be heard. Thy grace the rite from check can free. And yield the fruit I long to see. Thy duty bids thee, King, defend The suffering guest, the suppliant friend. Give me thy son, thine eldest born, Whom locks like raven's wings adorn. 143 The Rákshasas, giants, or fiends who are represented as disturbing the sacrifice, signify here, as often elsewhere, merely the savage tribes which placed themselves in hostile opposition to Bráhmanical institutions.
- **Translation**: 

---

### Verse 3 (Ramayana 0.128)
- **Original**: 110 The Ramayana That hero youth, the truly brave, Of thee, O glorious King, I crave. For he can lay those demons low Who mar my rites and work me woe: My power shall shield the youth from harm, And heavenly might shall nerve his arm. And on my champion will I shower Unnumbered gifts of varied power, Such gifts as shall ensure his fame And spread through all the worlds his name. Be sure those fiends can never stand Before the might of Ráma's hand, And mid the best and bravest none Can slay that pair but Raghu's son. Entangled in the toils of Fate Those sinners, proud and obstinate, Are, in their fury overbold, No match for Ráma mighty-souled. Nor let a father's breast give way Too far to fond affection's sway. Count thou the fiends already slain: My word is pledged, nor pledged in vain. I know the hero Ráma well In whom high thoughts and valour dwell; So does Va[ishmha, so do these Engaged in long austerities. If thou would do the righteous deed, And win high fame, thy virtue's meed, Fame that on earth shall last and live, To me, great King, thy Ráma give. If to the words that I have said, With Saint Va[ishmha at their head Thy holy men, O King, agree, Then let thy Ráma go with me.
- **Translation**: 

---

### Verse 4 (Ramayana 0.129)
- **Original**: Canto XXII. Dasaratha's Speech. 111 Ten nights my sacrifice will last, And ere the stated time be past Those wicked fiends, those impious twain, Must fall by wondrous Ráma slain. Let not the hours, I warn thee, fly, Fixt for the rite, unheeded by; Good luck have thou, O royal Chief, Nor give thy heart to needless grief.” Thus in fair words with virtue fraught The pious glorious saint besought. But the good speech with poignant sting Pierced ear and bosom of the king, Who, stabbed with pangs too sharp to bear, Fell prostrate and lay fainting there. Canto XXII. Dasaratha's Speech. His tortured senses all astray, While the hapless monarch lay, Then slowly gathering thought and strength To Vi[vámitra spoke at length: “My son is but a child, I ween; This year he will be just sixteen. How is he fit for such emprise, My darling with the lotus eyes? A mighty army will I bring That calls me master, lord, and king, And with its countless squadrons fight Against these rovers of the night. My faithful heroes skilled to wield
- **Translation**: 

---

### Verse 5 (Ramayana 0.130)
- **Original**: 112 The Ramayana The arms of war will take the field; Their skill the demons' might may break: Ráma, my child, thou must not take. I, even I, my bow in hand, Will in the van of battle stand, And, while my soul is left alive, With the night-roaming demons strive. Thy guarded sacrifice shall be Completed, from all hindrance free. Thither will I my journey make: Ráma, my child, thou must not take. A boy unskilled, he knows not yet The bounds to strength and weakness set. No match is he for demon foes Who magic arts to arms oppose.[035] O chief of saints, I have no power, Of Ráma reft, to live one hour: Mine aged heart at once would break: Ráma, my child, thou must not take. Nine thousand circling years have fled With all their seasons o'er my head, And as a hard-won boon, O sage, These sons have come to cheer mine age. My dearest love amid the four Is he whom first his mother bore, Still dearer for his virtues' sake: Ráma, my child, thou must not take. But if, unmoved by all I say, Thou needs must bear my son away, Let me lead with him, I entreat, A four-fold army144 all complete. What is the demons' might, O Sage? 144 Consisting of horse, foot, chariots, and elephants.
- **Translation**: 

---

### Verse 6 (Ramayana 0.131)
- **Original**: Canto XXII. Dasaratha's Speech. 113 Who are they? What their parentage? What is their size? What beings lend Their power to guard them and befriend? How can my son their arts withstand? Or I or all my armed band? Tell me the whole that I may know To meet in war each evil foe Whom conscious might inspires with pride.” And Vi[vámitra thus replied: “Sprung from Pulastya's race there came A giant known by RávaG's name. Once favoured by the Eternal Sire He plagues the worlds in ceaseless ire, For peerless power and might renowned, By giant bands encompassed round. Vi[ravas for his sire they hold, His brother is the Lord of Gold. King of the giant hosts is he, And worst of all in cruelty. This RávaG's dread commands impel Two demons who in might excel, Márícha and Suváhu hight, To trouble and impede the rite.” Then thus the king addressed the sage: “No power have I, my lord, to wage War with this evil-minded foe; Now pity on my darling show, And upon me of hapless fate, For thee as God I venerate. Gods, spirits, bards of heavenly birth,145 145 “The Gandharvas, or heavenly bards, had originally a warlike character but were afterwards reduced to the office of celestial musicians cheering the
- **Translation**: 

---

### Verse 7 (Ramayana 0.132)
- **Original**: 114 The Ramayana The birds of air, the snakes of earth Before the might of RávaG quail, Much less can mortal man avail. He draws, I hear, from out the breast The valour of the mightiest. No, ne'er can I with him contend, Or with the forces he may send. How can I then my darling lend, Godlike, unskilled in battle? No, I will not let my young child go. Foes of thy rite, those mighty ones, Sunda and Upasunda's sons, Are fierce as Fate to overthrow: I will not let my young child go. Márícha and Suváhu fell Are valiant and instructed well. One of the twain I might attack. With all my friends their lord to back.” Canto XXIII. Vasishtha's Speech. banquets of the Gods. Dr. Kuhn has shown their identity with the Centaurs in name, origin and attributes.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 8 (Ramayana 0.133)
- **Original**: Canto XXIII. Vasishtha's Speech. 115 While thus the hapless monarch spoke, Paternal love his utterance broke. Then words like these the saint returned, And fury in his bosom burned: “Didst thou, O King, a promise make, And wishest now thy word to break? A son of Raghu's line should scorn To fail in faith, a man forsworn. But if thy soul can bear the shame I will return e'en as I came. Live with thy sons, and joy be thine, False scion of Kakutstha's line.” As Vi[vámitra, mighty sage, Was moved with this tempestuous rage, Earth rocked and reeled throughout her frame, And fear upon the Immortals came. But Saint Va[ishmha, wisest seer, Observant of his vows austere, Saw the whole world convulsed with dread, And thus unto the monarch said: “Thou, born of old Ikshváku's seed, Art Justice' self in mortal weed. Constant and pious, blest by fate, The right thou must not violate. Thou, Raghu's son, so famous through The triple world as just and true, Perform thy bounden duty still, Nor stain thy race by deed of ill. If thou have sworn and now refuse Thou must thy store of merit lose. Then, Monarch, let thy Ráma go, Nor fear for him the demon foe. The fiends shall have no power to hurt
- **Translation**: 

---

### Verse 9 (Ramayana 0.134)
- **Original**: 116 The Ramayana Him trained to war or inexpert, Nor vanquish him in battle field, For Ku[ik's son the youth will shield. He is incarnate Justice, he The best of men for bravery. Embodied love of penance drear, Among the wise without a peer.[036] Full well he knows, great Ku[ik's son, The arms celestial, every one, Arms from the Gods themselves concealed, Far less to other men revealed. These arms to him, when earth he swayed, Mighty Kri[á[va, pleased, conveyed. Kri[á[va's sons they are indeed, Brought forth by Daksha's lovely seed,146 Heralds of conquest, strong and bold, Brilliant, of semblance manifold. Jayá and Vijayá, most fair, And hundred splendid weapons bare. Of Jayá, glorious as the morn, First fifty noble sons were born, Boundless in size yet viewless too, They came the demons to subdue. And fifty children also came Of Vijayá the beauteous dame, Sanháras named, of mighty force, Hard to assail or check in course. Of these the hermit knows the use, And weapons new can he produce. All these the mighty saint will yield To Ráma's hand, to own and wield; 146 These mysterious animated weapons are enumerated in Cantos XXIX and XXX. Daksha was the son of Brahmá and one of the Prajápatis, Demiurgi, or secondary authors of creation.
- **Translation**: 

---

### Verse 10 (Ramayana 0.135)
- **Original**: Canto XXIV. The Spells. 117 And armed with these, beyond a doubt Shall Ráma put those fiends to rout. For Ráma and the people's sake, For thine own good my counsel take, Nor seek, O King, with fond delay, The parting of thy son to stay.” Canto XXIV. The Spells. Va [ishmha thus was speaking still: The monarch, of his own free will, Bade with quick zeal and joyful cheer Ráma and LakshmaG hasten near. Mother and sire in loving care Sped their dear son with rite and prayer: Va [ishmha blessed him ere he went; O'er his loved head the father bent, And then to Ku[ik's son resigned Ráma with LakshmaG close behind. Standing by Vi[vámitra's side, The youthful hero, lotus-eyed, The Wind-God saw, and sent a breeze Whose sweet pure touch just waved the trees. There fell from heaven a flowery rain, And with the song and dance the strain Of shell and tambour sweetly blent As forth the son of Raghu went. The hermit led: behind him came The bow-armed Ráma, dear to fame,
- **Translation**: 

---

### Verse 11 (Ramayana 0.136)
- **Original**: 118 The Ramayana Whose locks were like the raven's wing:147 Then LakshmaG, closely following. The Gods and Indra, filled with joy, Looked down upon the royal boy, And much they longed the death to see Of their ten-headed enemy.148 Ráma and LakshmaG paced behind That hermit of the lofty mind, As the young A[vins,149 heavenly pair, Follow Lord Indra through the air. On arm and hand the guard they wore, Quiver and bow and sword they bore; Two fire-born Gods of War seemed they.150 He, Ziva's self who led the way. Upon fair Sarjú's southern shore They now had walked a league and more, When thus the sage in accents mild To Ráma said:“Beloved child, This lustral water duly touch: My counsel will avail thee much. Forget not all the words I say, 147 Youths of the Kshatriya class used to leave unshorn the side locks of their hair. These were calledKáka-paksha, or raven's wings. 148 The Rákshas or giant RávaG, king of Lanká. 149 “The meaning of A[vins (froma[va a horse, Persian asp, Greek5ÀÀ¿Â, Latin equus, Welsh ech) is Horsemen. They were twin deities of whom frequent mention is made in the Vedas and the Indian myths. The A[vins have much in common with the Dioscuri of Greece, and their mythical genealogy seems to indicate that their origin was astronomical. They were, perhaps, at first the morning star and evening star. They are said to be the children of the sun and the nymph A[viní, who is one of the lunar asterisms personified. In the popular mythology they are regarded as the physicians of the Gods.” G ORRESIO {FNS . 150 The word Kumára (a young prince, a Childe) is also a proper name of Skanda or Kártikeya God of War, the son ofZiva and Umá. The babe was matured in the fire.
- **Translation**: 

---

### Verse 12 (Ramayana 0.137)
- **Original**: Canto XXIV. The Spells. 119 Nor let the occasion slip away. Lo, with two spells I thee invest, The mighty and the mightiest. O'er thee fatigue shall ne'er prevail, Nor age or change thy limbs assail. Thee powers of darkness ne'er shall smite In tranquil sleep or wild delight. No one is there in all the land Thine equal for the vigorous hand. [037] Thou, when thy lips pronounce the spell, Shalt have no peer in heaven or hell. None in the world with thee shall vie, O sinless one, in apt reply, In fortune, knowledge, wit, and tact, Wisdom to plan and skill to act. This double science take, and gain Glory that shall for aye remain. Wisdom and judgment spring from each Of these fair spells whose use I teach. Hunger and thirst unknown to thee, High in the worlds thy rank shall be. For these two spells with might endued, Are the Great Father's heavenly brood, And thee, O Chief, may fitly grace, Thou glory of Kakutstha's race. Virtues which none can match are thine, Lord, from thy birth, of gifts divine, And now these spells of might shall cast Fresh radiance o'er the gifts thou hast.” Then Ráma duly touched the wave, Raised suppliant hands, bowed low his head, And took the spells the hermit gave, Whose soul on contemplation fed. From him whose might these gifts enhanced,
- **Translation**: 

---

### Verse 13 (Ramayana 0.138)
- **Original**: 120 The Ramayana A brighter beam of glory glanced: So shines in all his autumn blaze The Day-God of the thousand rays. The hermit's wants those youths supplied, As pupils use to holy guide. And then the night in sweet content On Sarjú's pleasant bank they spent. Canto XXV. The Hermitage Of Love. Soon as appeared the morning light Up rose the mighty anchorite, And thus to youthful Ráma said, Who lay upon his leafy bed: “High fate is hers who calls thee son: Arise, 'tis break of day; Rise, Chief, and let those rites be done Due at the morning's ray.”151 At that great sage's high behest Up sprang the princely pair, To bathing rites themselves addressed, And breathed the holiest prayer. Their morning task completed, they To Vi[vámitra came That store of holy works, to pay The worship saints may claim. Then to the hallowed spot they went 151 “At the rising of the sun as well as at noon certain observances, invocations, and prayers were prescribed which might under no circumstances be omitted. One of these observances was the recitation of the Sávitrí, a Vedic hymn to the Sun of wonderful beauty.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 14 (Ramayana 0.139)
- **Original**: Canto XXV. The Hermitage Of Love. 121 Along fair Sarjú's side Where mix her waters confluent With three-pathed Gangá's tide.152 There was a sacred hermitage Where saints devout of mind Their lives through many a lengthened age To penance had resigned. That pure abode the princes eyed With unrestrained delight, And thus unto the saint they cried, Rejoicing at the sight: “Whose is that hermitage we see? Who makes his dwelling there? Full of desire to hear are we: O Saint, the truth declare.” The hermit smiling made reply To the two boys' request: “Hear, Ráma, who in days gone by This calm retreat possessed. Kandarpa in apparent form, Called Káma153 by the wise, Dared Umá's154 new-wed lord to storm And make the God his prize. 'Gainst StháGu's155 self, on rites austere 152 Tripathaga, Three-path-go,flowing in heaven, on earth, and under the earth. See Canto XLV. 153 Tennyson's“Indian Cama,” the God of Love, known also by many other names. 154 Umá , orParvatí, was daughter of Himálaya, Monarch of mountains, and wife ofZiva. See Kálidasa'sKumára Sambhava , orBirth of the War-God. 155 StháGu. The Unmoving one, a name ofZiva.
- **Translation**: 

---

### Verse 15 (Ramayana 0.140)
- **Original**: 122 The Ramayana And vows intent,156 they say, His bold rash hand he dared to rear, Though StháGu cried, Away! But the God's eye with scornful glare Fell terrible on him. Dissolved the shape that was so fair[038] And burnt up every limb. Since the great God's terrific rage Destroyed his form and frame, Káma in each succeeding age Has borne Ananga's157 name. So, where his lovely form decayed, This land is Anga styled: Sacred to him of old this shade, And hermits undefiled. Here Scripture-talking elders sway Each sense with firm control, And penance-rites have washed away All sin from every soul. One night, fair boy, we here will spend, A pure stream on each hand, And with to-morrow's light will bend Our steps to yonder strand. Here let us bathe, and free from stain To that pure grove repair, 156 “The practice of austerities, voluntary tortures, and mortifications was anciently universal in India, and was held by the Indians to be of immense efficacy. Hence they mortified themselves to expiate sins, to acquire merits, and to obtain superhuman gifts and powers; the Gods themselves sometimes exercised themselves in such austerities, either to raise themselves to greater power and grandeur, or to counteract the austerities of man which threatened to prevail over them and to deprive them of heaven.… Such austerities were called in Indiatapas(burning ardour, fervent devotion) and he who practised them tapasvin.” G ORRESIO {FNS . 157 The Bodiless one.
- **Translation**: 

---

### Verse 16 (Ramayana 0.141)
- **Original**: Canto XXVI. The Forest Of Tádaká. 123 Sacred to Káma, and remain One night in comfort there.” With penance' far-discerning eye The saintly men beheld Their coming, and with transport high Each holy bosom swelled. To Ku[ik's son the gift they gave That honoured guest should greet, Water they brought his feet to lave, And showed him honor meet. Ráma and LakshmaG next obtained In due degree their share. Then with sweet talk the guests remained, And charmed each listener there. The evening prayers were duly said With voices calm and low: Then on the ground each laid his head And slept till morning's glow. Canto XXVI. The Forest Of Tádaká. When the fair light of morning rose The princely tamers of their foes Followed, his morning worship o'er, The hermit to the river's shore. The high-souled men with thoughtful care A pretty barge had stationed there. All cried,“O lord, this barge ascend, And with thy princely followers bend To yonder side thy prosperous way With naught to check thee or delay.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.142)
- **Original**: 124 The Ramayana Nor did the saint their rede reject: He bade farewell with due respect, And crossed, attended by the twain, That river rushing to the main. When now the bark was half way o'er, Ráma and LakshmaG heard the roar, That louder grew and louder yet, Of waves by dashing waters met. Then Ráma asked the mighty seer: “What is the tumult that I hear Of waters cleft in mid career?” Soon as the speech of Ráma, stirred By deep desire to know, he heard, The pious saint began to tell What paused the waters' roar and swell: “On high Kailása's distant hill There lies a noble lake Whose waters, born from Brahmá's will, The name of Mánas158 take. Thence, hallowing where'er they flow, The streams of Sarjú fall, And wandering through the plains below Embrace Ayodhyá's wall. Still, still preserved in Sarjú's name Sarovar's159 fame we trace. The flood of Brahma whence she came 158 “A celebrated lake regarded in India as sacred. It lies in the lofty region between the northern highlands of the Himálayas and mount Kailása, the region of the sacred lakes. The poem, following the popular Indian belief, makes the river Sarayú (now Sarjú) flow from the Mánasa lake; the sources of the river are a little to the south about a day's journey from the lake. See Lassen, Indische Alterthumshunde, page 34.” G ORRESIO {FNS . Manas means mind; mánasa, mental, mind-born. 159 Sarovarmeans best of lakes. This is another of the poet's fanciful etymolo- gies.
- **Translation**: 

---

### Verse 18 (Ramayana 0.143)
- **Original**: Canto XXVI. The Forest Of Tádaká. 125 To run her holy race. To meet great Gangá here she hies With tributary wave: Hence the loud roar ye hear arise, Of floods that swell and rave. Here, pride of Raghu's line, do thou In humble adoration bow.” He spoke. The princes both obeyed, And reverence to each river paid.160 They reached the southern shore at last, And gaily on their journey passed. A little space beyond there stood A gloomy awe-inspiring wood. The monarch's noble son began To question thus the holy man: “Whose gloomy forest meets mine eye Like some vast cloud that fills the sky? Pathless and dark it seems to be, Where birds in thousands wander free; Where shrill cicadas' cries resound, [039] And fowl of dismal note abound. Lion, rhinoceros, and bear, Boar, tiger, elephant, are there, There shrubs and thorns run wild: Dháo, Sál, Bignonia, Bel,161 are found, And every tree that grows on ground. How is the forest styled?” 160 The confluence of two or more rivers is often a venerated and holy place. The most famous is Prayág or Allahabad, where the Sarasvatí by an underground course is believed to join the Jumna and the Ganges. 161 The botanical names of the trees mentioned in the text are Grislea Tormen- tosa, Shorea Robusta, Echites Antidysenterica, Bignonia Suaveolens,Œ gle Marmelos, and Diospyrus Glutinosa. I have omitted theKutaja(Echites) and theTiG uka (Diospyrus).
- **Translation**: 

---

### Verse 19 (Ramayana 0.144)
- **Original**: 126 The Ramayana The glorious saint this answer made: “Dear child of Raghu, hear Who dwells within the horrid shade That looks so dark and drear. Where now is wood, long ere this day Two broad and fertile lands, Malaja and Karúsha lay, Adorned by heavenly hands. Here, mourning friendship's broken ties, Lord Indra of the thousand eyes Hungered and sorrowed many a day, His brightness soiled with mud and clay, When in a storm of passion he Had slain his dear friend Namuchi. Then came the Gods and saints who bore Their golden pitchers brimming o'er With holy streams that banish stain, And bathed Lord Indra pure again. When in this land the God was freed From spot and stain of impious deed For that his own dear friend he slew, High transport thrilled his bosom through. Then in his joy the lands he blessed, And gave a boon they long possessed: “Because these fertile lands retain The washings of the blot and stain,” 'Twas thus Lord Indra sware, “Malaja and Karúsha's name Shall celebrate with deathless fame My malady and care.”162 162 Here we meet with a fresh myth to account for the name of these regions. Malaja is probably a non-Aryan word signifying a hilly country: taken as a Sanskrit compound it meanssprung from defilement. The word Karúsha appears to have a somewhat similar meaning.
- **Translation**: 

---

### Verse 20 (Ramayana 0.145)
- **Original**: Canto XXVI. The Forest Of Tádaká. 127 “So be it,” all the Immortals cried, When Indra's speech they heard, And with acclaim they ratified The names his lips conferred. Long time, O victor of thy foes, These happy lands had sweet repose, And higher still in fortune rose. At length a spirit, loving ill, Tá aká, wearing shapes at will, Whose mighty strength, exceeding vast, A thousand elephants, surpassed, Was to fierce Sunda, lord and head Of all the demon armies, wed. From her, Lord Indra's peer in might Giant Márícha sprang to light: And she, a constant plague and pest, These two fair realms has long distressed. Now dwelling in her dark abode A league away she bars the road: And we, O Ráma, hence must go Where lies the forest of the foe. Now on thine own right arm rely, And my command obey: Smite the foul monster that she die, And take the plague away. To reach this country none may dare Fallen from its old estate, Which she, whose fury naught can bear, Has left so desolate. And now my truthful tale is told How with accursed sway The spirit plagued this wood of old, And ceases not to-day.”
- **Translation**: 

---



--- End of Ramayan_batch_105.md ---


--- Start of Ramayan_batch_106.md ---

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

### Verse 1 (Ramayana 0.146)
- **Original**: 128 The Ramayana Canto XXVII. The Birth Of Tádaká. When thus the sage without a peer Had closed that story strange to hear, Ráma again the saint addressed To set one lingering doubt at rest: “O holy man, 'tis said by all That spirits' strength is weak and small: How can she match, of power so slight, A thousand elephants in might?” And Vi[vámitra thus replied To Raghu's son the glorified: “Listen, and I will tell thee how She gained the strength that arms her now. A mighty spirit lived of yore; Suketu was the name he bore. Childless was he, and free from crime In rites austere he passed his time. The mighty Sire was pleased to show His favour, and a child bestow. Tá aká named, most fair to see, A pearl among the maids was she, And matched, for such was Brahmá's dower, A thousand elephants in power. Nor would the Eternal Sire, although The spirit longed, a son bestow That maid in beauty's youthful pride Was given to Sunda for a bride. Her son, Márícha was his name, A giant, through a curse, became. She, widowed, dared with him molest[040]
- **Translation**: 

---

### Verse 2 (Ramayana 0.147)
- **Original**: Canto XXVII. The Birth Of Tádaká. 129 Agastya,163 of all saints the best. Inflamed with hunger's wildest rage, Roaring she rushed upon the sage. When the great hermit saw her near, On speeding in her fierce career, He thus pronounced Márícha's doom: “A giant's form and shape assume.” And then, by mighty anger swayed, On Tá aká this curse he laid: “Thy present form and semblance quit, And wear a shape thy mood to fit; Changed form and feature by my ban, A fearful thing that feeds on man.” She, by his awful curse possessed, And mad with rage that fills her breast, Has on this land her fury dealt Where once the saint Agastya dwelt. Go, Ráma, smite this monster dead, The wicked plague, of power so dread, And further by this deed of thine The good of Bráhmans and of kine. Thy hand alone can overthrow, In all the worlds, this impious foe. Nor let compassion lead thy mind To shrink from blood of womankind; A monarch's son must ever count The people's welfare paramount, And whether pain or joy he deal 163 “This is one of those indefinable mythic personages who are found in the ancient traditions of many nations, and in whom cosmogonical or astronomical notions are generally figured. Thus it is related of Agastya that the Vindhyan mountains prostrated themselves before him; and yet the same Agastya is believed to be regent of the star Canopus.” G ORRESIO {FNS . He will appear as the friend and helper of Ráma farther on in the poem.
- **Translation**: 

---

### Verse 3 (Ramayana 0.148)
- **Original**: 130 The Ramayana Dare all things for his subjects' weal; Yea, if the deed bring praise or guilt, If life be saved or blood be spilt: Such, through all time, should be the care Of those a kingdom's weight who bear. Slay, Ráma, slay this impious fiend, For by no law her life is screened. So Manthará, as bards have told, Virochan's child, was slain of old By Indra, when in furious hate She longed the earth to devastate. So Kávya's mother, Bhrigu's wife, Who loved her husband as her life, When Indra's throne she sought to gain, By VishGu's hand of yore was slain. By these and high-souled kings beside, Struck down, have lawless women died.” Canto XXVIII. The Death Of Tádaká. Thus spoke the saint. Each vigorous word The noble monarch's offspring heard, And, reverent hands together laid, His answer to the hermit made: “My sire and mother bade me aye Thy word, O mighty Saint, obey So will I, O most glorious, kill This Tá aká who joys in ill, For such my sire's, and such thy will. To aid with mine avenging hand The Bráhmans, kine, and all the land,
- **Translation**: 

---

### Verse 4 (Ramayana 0.149)
- **Original**: Canto XXVIII. The Death Of Tádaká. 131 Obedient, heart and soul, I stand.” Thus spoke the tamer of the foe, And by the middle grasped his bow. Strongly he drew the sounding string That made the distant welkin ring. Scared by the mighty clang the deer That roamed the forest shook with fear, And Tá aká the echo heard, And rose in haste from slumber stirred. In wild amaze, her soul aflame With fury toward the spot she came. When that foul shape of evil mien And stature vast as e'er was seen The wrathful son of Raghu eyed, He thus unto his brother cried: “Her dreadful shape, O LakshmaG, see, A form to shudder at and flee. The hideous monster's very view Would cleave a timid heart in two. Behold the demon hard to smite, Defended by her magic might. My hand shall stay her course to-day, And shear her nose and ears away. No heart have I her life to take: I spare it for her sex's sake. My will is but, with minished force, To check her in her evil course.” While thus he spoke, by rage impelled Roaring as she came nigh, The fiend her course at Ráma held With huge arms tossed on high. Her, rushing on, the seer assailed With a loud cry of hate;
- **Translation**: 

---

### Verse 5 (Ramayana 0.150)
- **Original**: 132 The Ramayana And thus the sons of Raghu hailed: “Fight, and be fortunate.” Then from the earth a horrid cloud Of dust the demon raised, And for awhile in darkling shroud Wrapt Raghu's sons amazed. Then calling on her magic power The fearful fight to wage, She smote him with a stony shower, Till Ráma burned with rage. Then pouring forth his arrowy rain That stony flood to stay,[041] With winged darts, as she charged amain, He shore her hands away. As Tá aká still thundered near Thus maimed by Ráma's blows, Lakshma G in fury severed sheer The monster's ears and nose. Assuming by her magic skill A fresh and fresh disguise, She tried a thousand shapes at will, Then vanished from their eyes. When Gádhi's son of high renown Still saw the stony rain pour down Upon each princely warrior's head, With words of wisdom thus he said: “Enough of mercy, Ráma, lest This sinful evil-working pest, Disturber of each holy rite, Repair by magic arts her might. Without delay the fiend should die, For, see, the twilight hour is nigh. And at the joints of night and day Such giant foes are hard to slay.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.151)
- **Original**: Canto XXVIII. The Death Of Tádaká. 133 Then Ráma, skilful to direct His arrow to the sound, With shafts the mighty demon checked Who rained her stones around. She sore impeded and beset By Ráma and his arrowy net, Though skilled in guile and magic lore, Rushed on the brothers with a roar. Deformed, terrific, murderous, dread, Swift as the levin on she sped, Like cloudy pile in autumn's sky, Lifting her two vast arms on high, When Ráma smote her with a dart, Shaped like a crescent, to the heart. Sore wounded by the shaft that came With lightning speed and surest aim, Blood spouting from her mouth and side, She fell upon the earth and died. Soon as the Lord who rules the sky Saw the dread monster lifeless lie, He called aloud, Well done! well done! And the Gods honoured Raghu's son. Standing in heaven the Thousand-eyed, With all the Immortals, joying cried: “Lift up thine eyes, O Saint, and see The Gods and Indra nigh to thee. This deed of Ráma's boundless might Has filled our bosoms with delight, Now, for our will would have it so, To Raghu's son some favour show. Invest him with the power which naught But penance gains and holy thought, Those heavenly arms on him bestow To thee entrusted long ago
- **Translation**: 

---

### Verse 7 (Ramayana 0.152)
- **Original**: 134 The Ramayana By great Kri[á[va best of kings, Son of the Lord of living things. More fit recipient none can be Than he who joys it following thee; And for our sakes the monarch's seed Has yet to do a mighty deed.” He spoke; and all the heavenly train Rejoicing sought their homes again, While honour to the saint they paid. Then came the evening's twilight shade, The best of hermits overjoyed To know the monstrous fiend destroyed, His lips on Ráma's forehead pressed, And thus the conquering chief addressed: “O Ráma gracious to the sight. Here will we pass the present night, And with the morrow's earliest ray Bend to my hermitage our way.” The son of Da[aratha heard, Delighted, Vi[vámitra's word, And as he bade, that night he spent In Tá aká's wild wood, content. And the grove shone that happy day, Freed from the curse that on it lay, Like Chaitraratha164 fair and gay. Canto XXIX. The Celestial Arms. 164 The famous pleasure-garden of Kuvera the God of Wealth.
- **Translation**: 

---

### Verse 8 (Ramayana 0.153)
- **Original**: Canto XXIX. The Celestial Arms. 135 That night they slept and took their rest; And then the mighty saint addressed, With pleasant smile and accents mild These words to Raghu's princely child: “Well pleased am I. High fate be thine, Thou scion of a royal line. Now will I, for I love thee so, All heavenly arms on thee bestow. Victor with these, whoe'er oppose, Thy hand shall conquer all thy foes, Though Gods and spirits of the air, Serpents and fiends, the conflict dare. I'll give thee as a pledge of love The mystic arms they use above, For worthy thou to have revealed The weapons I have learnt to wield.165 [042] First, son of Raghu, shall be thine The arm of Vengeance, strong, divine: The arm of Fate, the arm of Right, And VishGu's arm of awful might: That, before which no foe can stand, The thunderbolt of Indra's hand; And Ziva's trident, sharp and dread, And that dire weapon Brahmá's Head. And two fair clubs, O royal child, One Charmer and one Pointed styled With flame of lambent fire aglow, 165 “The whole of this Canto together with the following one, regards the belief, formerly prevalent in India, that by virtue of certain spells, to be learnt and muttered, secret knowledge and superhuman powers might be acquired. To this the poet has already alluded in Canto xxiii. These incorporeal weapons are partly represented according to the fashion of those ascribed to the Gods and the different orders of demi-gods, partly are the mere creations of fancy; and it would not be easy to say what idea the poet had of them in his own mind, or what powers he meant to assign to each.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 9 (Ramayana 0.154)
- **Original**: 136 The Ramayana On thee, O Chieftain, I bestow. And Fate's dread net and Justice' noose That none may conquer, for thy use: And the great cord, renowned of old, Which VaruG ever loves to hold. Take these two thunderbolts, which I Have got for thee, the Moist and Dry. Here Ziva's dart to thee I yield, And that which VishGu wont to wield. I give to thee the arm of Fire, Desired by all and named the Spire. To thee I grant the Wind-God's dart, Named Crusher, O thou pure of heart, This arm, the Horse's Head, accept, And this, the Curlew's Bill yclept, And these two spears, the best e'er flew, Named the Invincible and True. And arms of fiends I make thine own, Skull-wreath and mace that smashes bone. And Joyous, which the spirits bear, Great weapon of the sons of air. Brave offspring of the best of lords, I give thee now the Gem of swords, And offer next, thine hand to arm, The heavenly bards' beloved charm. Now with two arms I thee invest Of never-ending Sleep and Rest, With weapons of the Sun and Rain, And those that dry and burn amain; And strong Desire with conquering touch, The dart that Káma prizes much. I give the arm of shadowy powers That bleeding flesh of men devours. I give the arms the God of Gold
- **Translation**: 

---

### Verse 10 (Ramayana 0.155)
- **Original**: Canto XXIX. The Celestial Arms. 137 And giant fiends exult to hold. This smites the foe in battle-strife, And takes his fortune, strength, and life. I give the arms called False and True, And great Illusion give I too; The hero's arm called Strong and Bright That spoils the foeman's strength in fight. I give thee as a priceless boon The Dew, the weapon of the Moon, And add the weapon, deftly planned, That strengthens Vi[vakarmá's hand. The Mortal dart whose point is chill, And Slaughter, ever sure to kill; All these and other arms, for thou Art very dear, I give thee now. Receive these weapons from my hand, Son of the noblest in the land.” Facing the east, the glorious saint Pure from all spot of earthly taint, To Ráma, with delighted mind, That noble host of spells consigned. He taught the arms, whose lore is won Hardly by Gods, to Raghu's son. He muttered low the spell whose call Summons those arms and rules them all And, each in visible form and frame, Before the monarch's son they came. They stood and spoke in reverent guise To Ráma with exulting cries: “O noblest child of Raghu, see, Thy ministers and thralls are we.” With joyful heart and eager hand Ráma received the wondrous band,
- **Translation**: 

---

### Verse 11 (Ramayana 0.156)
- **Original**: 138 The Ramayana And thus with words of welcome cried: “Aye present to my will abide.” Then hasted to the saint to pay Due reverence, and pursued his way. Canto XXX. The Mysterious Powers.166 Pure, with glad cheer and joyful breast, Of those mysterious arms possessed, Ráma, now passing on his way, Thus to the saint began to say: “Lord of these mighty weapons, I Can scarce be harmed by Gods on high; Now, best of saints, I long to gain The powers that can these arms restrain.” Thus spoke the prince. The sage austere, True to his vows, from evil clear, Called forth the names of those great charms Whose powers restrain the deadly arms. “Receive thou True and Truly famed, And Bold and Fleet: the weapons named[043] 166 “In SanskritSankára, a word which has various significations but the primary meaning of which isthe act of seizing. A magical power seems to be implied of employing the weapons when and where required. The remarks I have made on the preceding Canto apply with still greater force to this. The MSS. greatly vary in the enumeration of theseSankáras, and it is not surprising that copyists have incorrectly written the names which they did not well understand. The commentators throw no light upon the subject.” SCHLEGEL {FNS . I have taken the liberty of omitting four of these which Schlegel translates“Scleromphalum, Euomphalum, Centiventrem, and Chrysomphalum.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.157)
- **Original**: Canto XXX. The Mysterious Powers. 139 Warder and Progress, swift of pace, Averted-head and Drooping-face; The Seen, and that which Secret flies; The weapon of the thousand eyes; Ten-headed, and the Hundred-faced, Star-gazer and the Layer-waste: The Omen-bird, the Pure-from-spot, The pair that wake and slumber not: The Fiendish, that which shakes amain, The Strong-of-Hand, the Rich-in-Gain: The Guardian, and the Close-allied, The Gaper, Love, and Golden-side: O Raghu's son receive all these, Bright ones that wear what forms they please; Kri[á[va's mystic sons are they, And worthy thou their might to sway.” With joy the pride of Raghu's race Received the hermit's proffered grace, Mysterious arms, to check and stay, Or smite the foeman in the fray. Then, all with heavenly forms endued, Nigh came the wondrous multitude. Celestial in their bright attire Some shone like coals of burning fire; Some were like clouds of dusky smoke; And suppliant thus they sweetly spoke: “Thy thralls, O Ráma, here we stand: Command, we pray, thy faithful band” “Depart,” he cried,“where each may list, But when I call you to assist, Be present to my mind with speed, And aid me in the hour of need.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.158)
- **Original**: 140 The Ramayana To Ráma then they lowly bent, And round him in due reverence went, To his command, they answered, Yea, And as they came so went away. When thus the arms had homeward flown, With pleasant words and modest tone, E'en as he walked, the prince began To question thus the holy man: “What cloudlike wood is that which near The mountain's side I see appear? O tell me, for I long to know; Its pleasant aspect charms me so. Its glades are full of deer at play, And sweet birds sing on every spray, Past is the hideous wild; I feel So sweet a tremor o'er me steal, And hail with transport fresh and new A land that is so fair to view. Then tell me all, thou holy Sage, And whose this pleasant hermitage In which those wicked ones delight To mar and kill each holy rite. And with foul heart and evil deed Thy sacrifice, great Saint, impede. To whom, O Sage, belongs this land In which thine altars ready stand! 'Tis mine to guard them, and to slay The giants who the rites would stay. All this, O best of saints, I burn From thine own lips, my lord, to learn.” Canto XXXI. The Perfect Hermitage.
- **Translation**: 

---

### Verse 14 (Ramayana 0.159)
- **Original**: Canto XXXI. The Perfect Hermitage. 141 Thus spoke the prince of boundless might, And thus replied the anchorite: “Chief of the mighty arm, of yore Lord VishGu whom the Gods adore, For holy thought and rites austere Of penance made his dwelling here. This ancient wood was called of old Grove of the Dwarf, the mighty-souled, And when perfection he attained The grove the name of Perfect gained. Bali of yore, Virochan's son, Dominion over Indra won, And when with power his proud heart swelled, O'er the three worlds his empire held. When Bali then began a rite, The Gods and Indra in affright Sought VishGu in this place of rest, And thus with prayers the God addressed: “Bali. Virochan's mighty son, His sacrifice has now begun: Of boundless wealth, that demon king Is bounteous to each living thing. Though suppliants flock from every side The suit of none is e'er denied. Whate'er, where'er howe'er the call, He hears the suit and gives to all. Now with thine own illusive art Perform, O Lord, the helper's part: Assume a dwarfish form, and thus From fear and danger rescue us.”167 167 I omit, after this line, eight[lokeswhich, as Schlegel allows, are quite out of place.
- **Translation**: 

---

### Verse 15 (Ramayana 0.160)
- **Original**: 142 The Ramayana Thus in their dread the Immortals sued: The God a dwarflike shape indued:168 Before Virochan's son he came, Three steps of land his only claim. The boon obtained, in wondrous wise Lord VishGu's form increased in size; Through all the worlds, tremendous, vast, God of the Triple Step, he passed.169 The whole broad earth from side to side He measured with one mighty stride, Spanned with the next the firmament, And with the third through heaven he went.[044] Thus was the king of demons hurled By VishGu to the nether world, And thus the universe restored To Indra's rule, its ancient lord. And now because the immortal God This spot in dwarflike semblance trod, The grove has aye been loved by me For reverence of the devotee. But demons haunt it, prompt to stay Each holy offering I would pay. Be thine, O lion-lord, to kill These giants that delight in ill. This day, beloved child, our feet Shall rest within the calm retreat: And know, thou chief of Raghu's line, My hermitage is also thine.” 168 This is the fifth of theavatárs, descents or incarnations of VishGu. 169 This is a solar allegory. VishGu is the sun, the three steps being his rising, culmination, and setting.
- **Translation**: 

---

### Verse 16 (Ramayana 0.161)
- **Original**: Canto XXXI. The Perfect Hermitage. 143 He spoke; and soon the anchorite, With joyous looks that beamed delight, With Ráma and his brother stood Within the consecrated wood. Soon as they saw the holy man, With one accord together ran The dwellers in the sacred shade, And to the saint their reverence paid, And offered water for his feet, The gift of honour and a seat; And next with hospitable care They entertained the princely pair. The royal tamers of their foes Rested awhile in sweet repose: Then to the chief of hermits sued Standing in suppliant attitude: “Begin, O best of saints, we pray, Initiatory rites to-day. This Perfect Grove shall be anew Made perfect, and thy words be true.” Then, thus addressed, the holy man, The very glorious sage, began The high preliminary rite. Restraining sense and appetite. Calmly the youths that night reposed, And rose when morn her light disclosed, Their morning worship paid, and took Of lustral water from the brook. Thus purified they breathed the prayer, Then greeted Vi[vámitra where As celebrant he sate beside The flame with sacred oil supplied.
- **Translation**: 

---

### Verse 17 (Ramayana 0.162)
- **Original**: 144 The Ramayana Canto XXXII. Visvámitra's Sacrifice. That conquering pair, of royal race, Skilled to observe due time and place, To Ku[ik's hermit son addressed, In timely words, their meet request: “When must we, lord, we pray thee tell, Those Rovers of the Night repel? Speak, lest we let the moment fly, And pass the due occasion by.” Thus longing for the strife, they prayed, And thus the hermits answer made: “Till the fifth day be come and past, O Raghu's sons, your watch must last. The saint his Dikshá170 has begun, And all that time will speak to none.” Soon as the steadfast devotees Had made reply in words like these, The youths began, disdaining sleep, Six days and nights their watch to keep. The warrior pair who tamed the foe, Unrivalled benders of the bow, Kept watch and ward unwearied still To guard the saint from scathe and ill. 'Twas now the sixth returning day, The hour foretold had past away. Then Ráma cried:“O Lakshma G, now Firm, watchful, resolute be thou. The fiends as yet have kept afar From the pure grove in which we are: Yet waits us, ere the day shall close, Dire battle with the demon foes.” 170 Certain ceremonies preliminary to a sacrifice.
- **Translation**: 

---

### Verse 18 (Ramayana 0.163)
- **Original**: Canto XXXII. Visvámitra's Sacrifice. 145 While thus spoke Ráma borne away By longing for the deadly fray, See! bursting from the altar came The sudden glory of the flame. Round priest and deacon, and upon Grass, ladles, flowers, the splendour shone, And the high rite, in order due, With sacred texts began anew. But then a loud and fearful roar Re-echoed through the sky; And like vast clouds that shadow o'er The heavens in dark July, Involved in gloom of magic might Two fiends rushed on amain, Márícha, Rover of the Night, Suváhu, and their train. As on they came in wild career Thick blood in rain they shed; And Ráma saw those things of fear Impending overhead. Then soon as those accursed two Who showered down blood be spied, Thus to his brother brave and true Spoke Ráma lotus-eyed: “Now, LakshmaG, thou these fiends shalt see, Man-eaters, foul of mind, Before my mortal weapon flee Like clouds before the wind.” He spoke. An arrow, swift as thought, Upon his bow he pressed, And smote, to utmost fury wrought, Márícha on the breast. Deep in his flesh the weapon lay Winged by the mystic spell, [045]
- **Translation**: 

---

### Verse 19 (Ramayana 0.164)
- **Original**: 146 The Ramayana And, hurled a hundred leagues away, In ocean's flood he fell. Then Ráma, when he saw the foe Convulsed and mad with pain Neath the chill-pointed weapon's blow, To LakshmaG spoke again: “See, LakshmaG, see! this mortal dart That strikes a numbing chill, Hath struck him senseless with the smart, But left him breathing still. But these who love the evil way, And drink the blood they spill, Rejoicing holy rites to stay, Fierce plagues, my hand shall kill.” He seized another shaft, the best, Aglow with living flame; It struck Suváhu on the chest, And dead to earth he came. Again a dart, the Wind-God's own, Upon his string he laid, And all the demons were o'erthrown, The saints no more afraid. When thus the fiends were slain in fight, Disturbers of each holy rite, Due honour by the saints was paid To Ráma for his wondrous aid: So Indra is adored when he Has won some glorious victory. Success at last the rite had crowned, And Vi[vámitra gazed around, And seeing every side at rest, The son of Raghu thus addressed: “My joy, O Prince, is now complete: Thou hast obeyed my will:
- **Translation**: 

---

### Verse 20 (Ramayana 0.165)
- **Original**: Canto XXXIII. The Sone. 147 Perfect before, this calm retreat Is now more perfect still.” Canto XXXIII. The Sone. Their task achieved, the princes spent That night with joy and full content. Ere yet the dawn was well displayed Their morning rites they duly paid, And sought, while yet the light was faint, The hermits and the mighty saint. They greeted first that holy sire Resplendent like the burning fire, And then with noble words began Their sweet speech to the sainted man: “Here stand, O Lord, thy servants true: Command what thou wouldst have us do.” The saints, by Vi[vámitra led, To Ráma thus in answer said: “Janak the king who rules the land Of fertile Míthilá has planned A noble sacrifice, and we Will thither go the rite to see. Thou, Prince of men, with us shalt go, And there behold the wondrous bow, Terrific, vast, of matchless might, Which, splendid at the famous rite, The Gods assembled gave the king. No giant, fiend, or God can string That gem of bows, no heavenly bard:
- **Translation**: 

---



--- End of Ramayan_batch_106.md ---


--- Start of Ramayan_batch_107.md ---

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

### Verse 1 (Ramayana 0.166)
- **Original**: 148 The Ramayana Then, sure, for man the task were hard. When lords of earth have longed to know The virtue of that wondrous bow, The strongest sons of kings in vain Have tried the mighty cord to strain. This famous bow thou there shalt view, And wondrous rites shalt witness too. The high-souled king who lords it o'er The realm of Míthilá of yore Gained from the Gods this bow, the price Of his imperial sacrifice. Won by the rite the glorious prize Still in the royal palace lies, Laid up in oil of precious scent With aloe-wood and incense blent.” Then Ráma answering, Be it so, Made ready with the rest to go. The saint himself was now prepared, But ere beyond the grove he fared, He turned him and in words like these Addressed the sylvan deities: “Farewell! each holy rite complete, I leave the hermits' perfect seat: To Gangá's northern shore I go Beneath Himálaya's peaks of snow.” With reverent steps he paced around The limits of the holy ground, And then the mighty saint set forth And took his journey to the north. His pupils, deep in Scripture's page, Followed behind the holy sage, And servants from the sacred grove A hundred wains for convoy drove.
- **Translation**: 

---

### Verse 2 (Ramayana 0.167)
- **Original**: Canto XXXIV. Brahmadatta. 149 The very birds that winged that air, The very deer that harboured there, Forsook the glade and leafy brake And followed for the hermit's sake. They travelled far, till in the west The sun was speeding to his rest, And made, their portioned journey o'er, Their halt onZona's171 distant shore. The hermits bathed when sank the sun, And every rite was duly done, Oblations paid to Fire, and then Sate round their chief the holy men. Ráma and LakshmaG lowly bowed In reverence to the hermit crowd, And Ráma, having sate him down Before the saint of pure renown, [046] With humble palms together laid His eager supplication made: “What country, O my lord, is this, Fair-smiling in her wealth and bliss? Deign fully, O thou mighty Seer, To tell me, for I long to hear.” Moved by the prayer of Ráma, he Told forth the country's history. Canto XXXIV. Brahmadatta. 171 A river which rises in Budelcund and falls into the Ganges near Patna. It is called alsoHiraGyaráhu, Golden-armed, andHiraGyaráha, Auriferous.
- **Translation**: 

---

### Verse 3 (Ramayana 0.168)
- **Original**: 150 The Ramayana “A king of Brahmá's seed who bore The name of Ku[a reigned of yore. Just, faithful to his vows, and true, He held the good in honour due. His bride, a queen of noble name, Of old Vidarbha's172 monarchs came. Like their own father, children four, All valiant boys, the lady bore. In glorious deeds each nerve they strained, And well their Warrior part sustained. To them most just, and true, and brave, Their father thus his counsel gave: “Beloved children, ne'er forget Protection is a prince's debt: The noble work at once begin, High virtue and her fruits to win.” The youths, to all the people dear, Received his speech with willing ear; And each went forth his several way, Foundations of a town to lay. Ku [ámba, prince of high renown, Was builder of Kau[ámbí's town, And Ku [anábha, just and wise, Bade high Mahodaya's towers arise. Amúrtarajas chose to dwell In DharmáraGya's citadel, And Vasu bade his city fair The name of Girivraja bear.173 172 The modern Berar. 173 According to the Bengal recension the first (Ku[ámba) is called Ku[á[va, and his city Kau[á[ví. This name does not occur elsewhere. The reading of the northern recension is confirmed by Foê Kouê Ki; p. 385, where the cityKiaoshangmi is mentioned. It lay 500listo the south-west ofPrayága, on the south bank of the Jumna.Mahodaya is another name of Kanyakubja: Dharmára Gya, the wood to which the God of Justice is said to have fled
- **Translation**: 

---

### Verse 4 (Ramayana 0.169)
- **Original**: Canto XXXIV. Brahmadatta. 151 This fertile spot whereon we stand Was once the high-souled Vasu's land. Behold! as round we turn our eyes, Five lofty mountain peaks arise. See! bursting from her parent hill, Sumágadhí, a lovely rill, Bright gleaming as she flows between The mountains, like a wreath is seen, And then through Magadh's plains and groves With many a fair mæander roves. And this was Vasu's old domain, The fertile Magadh's broad champaign, Which smiling fields of tilth adorn And diadem with golden corn. The queen Ghritáchí, nymph most fair, Married to Ku[anábha, bare A hundred daughters, lovely-faced, With every charm and beauty graced. It chanced the maidens, bright and gay As lightning-flashes on a day Of rain time, to the garden went With song and play and merriment, And there in gay attire they strayed, And danced, and laughed, and sang, and played. The God of Wind who roves at will All places, as he lists, to fill, Saw the young maidens dancing there, Of faultless shape and mien most fair. “I love you all, sweet girls,” he cried, “And each shall be my darling bride. Forsake, forsake your mortal lot, through fear of Soma the Moon-God was in Magadh. Girivraja was in the same neighbourhood. See Lasson's I, A. Vol. I. p. 604.
- **Translation**: 

---

### Verse 5 (Ramayana 0.170)
- **Original**: 152 The Ramayana And gain a life that withers not. A fickle thing is youth's brief span, And more than all in mortal man. Receive unending youth, and be Immortal, O my loves, with me.” The hundred girls, to wonder stirred, The wooing of the Wind-God heard, Laughed, as a jest, his suit aside, And with one voice they thus replied: “O mighty Wind, free spirit who All life pervadest, through and through, Thy wondrous power we maidens know; Then wherefore wilt thou mock us so? Our sire is Ku[anábha, King; And we, forsooth, have charms to bring A God to woo us from the skies; But honour first we maidens prize. Far may the hour, we pray, be hence, When we, O thou of little sense, Our truthful father's choice refuse, And for ourselves our husbands choose. Our honoured sire our lord we deem, He is to us a God supreme, And they to whom his high decree May give us shall our husbands be.” He heard the answer they returned, And mighty rage within him burned. On each fair maid a blast he sent: Each stately form he bowed and bent. Bent double by the Wind-God's ire They sought the palace of their sire,[047]
- **Translation**: 

---

### Verse 6 (Ramayana 0.171)
- **Original**: Canto XXXIV. Brahmadatta. 153 There fell upon the ground with sighs, While tears and shame were in their eyes. The king himself, with troubled brow, Saw his dear girls so fair but now, A mournful sight all bent and bowed, And grieving thus he cried aloud: “What fate is this, and what the cause? What wretch has scorned all heavenly laws? Who thus your forms could curve and break? You struggle, but no answer make.” They heard the speech of that wise king Of their misfortune questioning. Again the hundred maidens sighed, Touched with their heads his feet, and cried: “The God of Wind, pervading space, Would bring on us a foul disgrace, And choosing folly's evil way From virtue's path in scorn would stray. But we in words like these reproved The God of Wind whom passion moved: “Farewell, O Lord! A sire have we, No women uncontrolled and free. Go, and our sire's consent obtain If thou our maiden hands wouldst gain. No self-dependent life we live: If we offend, our fault forgive.” But led by folly as a slave, He would not hear the rede we gave, And even as we gently spoke We felt the Wind-God's crushing stroke.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.172)
- **Original**: 154 The Ramayana The pious king, with grief distressed, The noble hundred thus addressed: “With patience, daughters, bear your fate, Yours was a deed supremely great When with one mind you kept from shame The honour of your father's name. Patience, when men their anger vent, Is woman's praise and ornament; Yet when the Gods inflict the blow Hard is it to support the woe. Patience, my girls, exceeds all price: 'Tis alms, and truth, and sacrifice. Patience is virtue, patience fame: Patience upholds this earthly frame. And now, I think, is come the time To wed you in your maiden prime. Now, daughters, go where'er you will: Thoughts for your good my mind shall fill.” The maidens went, consoled, away: The best of kings, that very day, Summoned his ministers of state About their marriage to debate. Since then, because the Wind-God bent The damsels' forms for punishment, That royal town is known to fame By Kanyákubja's174 borrowed name. 174 That is, the City of the Bent Virgins, the modern Kanauj or Canouge.
- **Translation**: 

---

### Verse 8 (Ramayana 0.173)
- **Original**: Canto XXXIV. Brahmadatta. 155 There lived a sage called Chúli then, Devoutest of the sons of men; His days in penance rites he spent, A glorious saint, most continent. To him absorbed in tasks austere The child of Urmilá drew near, Sweet Somadá, the heavenly maid And lent the saint her pious aid. Long time near him the maiden spent, And served him meek and reverent, Till the great hermit, pleased with her, Thus spoke unto his minister: “Grateful am I for all thy care: Blest maiden, speak, thy wish declare.” The sweet-voiced nymph rejoiced to see The favour of the devotee, And to that eloquent old man, Most eloquent she thus began: “Thou hast, by heavenly grace sustained, Close union with the Godhead gained. I long, O Saint, to see a son By force of holy penance won. Unwed, a maiden life I live: A son to me, thy suppliant, give.” The saint with favour heard her prayer, And gave a son exceeding fair. Him, Chúli's spiritual child, His mother Brahmadatta175 styled. King Brahmadatta, rich and great, In Kámpilí maintained his state, Ruling, like Indra in his bliss, His fortunate metropolis. 175 Literally, Given byBrahma or devout contemplation.
- **Translation**: 

---

### Verse 9 (Ramayana 0.174)
- **Original**: 156 The Ramayana King Ku[anábha planned that he His hundred daughters' lord should be. To him, obedient to his call, The happy monarch gave them all. Like Indra then he took the hand Of every maiden of the band. Soon as the hand of each young maid In Brahmadatta's palm was laid, Deformity and cares away, She shone in beauty bright and gay. Their freedom from the Wind-God's might Saw Ku [anábha with delight. Each glance that on their forms he threw Filled him with raptures ever new. Then when the rites were all complete, With highest marks of honour meet The bridegroom with his brides he sent To his great seat of government. The nymph received with pleasant speech Her daughters; and, embracing each, Upon their forms she fondly gazed, And royal Ku[anábha praised. [048] Canto XXXV. Visvámitra's Lineage.
- **Translation**: 

---

### Verse 10 (Ramayana 0.175)
- **Original**: Canto XXXV. Visvámitra's Lineage. 157 “The rites were o'er, the maids were wed, The bridegroom to his home was sped. The sonless monarch bade prepare A sacrifice to gain an heir. Then Ku[a, Brahmá's son, appeared, And thus King Ku[anábha cheered: “Thou shalt, my child, obtain a son Like thine own self, O holy one. Through him for ever, Gádhi named, Shalt thou in all the worlds be famed.” He spoke, and vanished from the sight To Brahmá's world of endless light. Time fled, and, as the saint foretold, Gádhi was born, the holy-souled. My sire was he; through him I trace My line from royal Ku[a's race. My sister— elder-born was she— The pure and good Satyavatí,176 Was to the great Richíka wed. Still faithful to her husband dead, She followed him, most noble dame, And, raised to heaven in human frame, A pure celestial stream became. Down from Himálaya's snowy height, In floods for ever fair and bright, My sister's holy waves are hurled To purify and glad the world. Now on Himálaya's side I dwell Because I love my sister well. 176 Now called Ko[í (Cosy) corrupted from Kau[ikí, daughter of Ku[]a. “This is one of those personifications of rivers so frequent in the Grecian mythology, but in the similar myths is seen the impress of the genius of each people, austere and profoundly religious in India, graceful and devoted to the worship of external beauty in Greece.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 11 (Ramayana 0.176)
- **Original**: 158 The Ramayana She, for her faith and truth renowned, Most loving to her husband found, High-fated, firm in each pure vow, Is queen of all the rivers now. Bound by a vow I left her side And to the Perfect convent hied. There, by the aid 'twas thine to lend, Made perfect, all my labours end. Thus, mighty Prince, I now have told My race and lineage, high and old, And local tales of long ago Which thou, O Ráma, fain wouldst know. As I have sate rehearsing thus The midnight hour is come on us. Now, Ráma, sleep, that nothing may Our journey of to-morrow stay. No leaf on any tree is stirred: Hushed in repose are beast and bird: Where'er you turn, on every side, Dense shades of night the landscape hide, The light of eve is fled: the skies, Thick-studded with their host of eyes, Seem a star-forest overhead, Where signs and constellations spread. Now rises, with his pure cold ray, The moon that drives the shades away, And with his gentle influence brings Joy to the hearts of living things. Now, stealing from their lairs, appear The beasts to whom the night is dear. Now spirits walk, and every power That revels in the midnight hour.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.177)
- **Original**: Canto XXXVI. The Birth Of Gangá. 159 The mighty hermit's tale was o'er, He closed his lips and spoke no more. The holy men on every side, “Well done! well done,” with reverence cried; “The mighty men of Ku[a's seed Were ever famed for righteous deed. Like Brahmá's self in glory shine The high-souled lords of Ku[a's line, And thy great name is sounded most, O Saint, amid the noble host. And thy dear sister— fairest she Of streams, the high-born Kau[ikí— Diffusing virtue where she flows, New splendour on thy lineage throws.” Thus by the chief of saints addressed The son of Gádhi turned to rest; So, when his daily course is done, Sinks to his rest the beaming sun. Ráma with LakshmaG, somewhat stirred To marvel by the tales they heard, Turned also to his couch, to close His eyelids in desired repose. Canto XXXVI. The Birth Of Gangá. The hours of night now waning fast On Zona's pleasant shore they passed. Then, when the dawn began to break, To Ráma thus the hermit spake: “The light of dawn is breaking clear, The hour of morning rites is near.
- **Translation**: 

---

### Verse 13 (Ramayana 0.178)
- **Original**: 160 The Ramayana Rise, Ráma, rise, dear son, I pray, And make thee ready for the way.” Then Ráma rose, and finished all His duties at the hermit's call, Prepared with joy the road to take, And thus again in question spake: “Here fair and deep theZona flows, And many an isle its bosom shows: What way, O Saint, will lead us o'er And land us on the farther shore?” The saint replied:“The way I choose Is that which pious hermits use.”[049] For many a league they journeyed on Till, when the sun of mid-day shone, The hermit-haunted flood was seen Of Jáhnaví,177 the Rivers' Queen. Soon as the holy stream they viewed, Thronged with a white-winged multitude Of sárases178 and swans,179 delight Possessed them at the lovely sight; And then prepared the hermit band To halt upon that holy strand. They bathed as Scripture bids, and paid Oblations due to God and shade. To Fire they burnt the offerings meet, And sipped the oil, like Amrit sweet. Then pure and pleased they sate around Saint Vi[vámitra on the ground. The holy men of lesser note, 177 One of the names of the Ganges considered as the daughter of Jahnu. See Canto XLIV. 178 The Indian Crane. 179 Or, rather, geese.
- **Translation**: 

---

### Verse 14 (Ramayana 0.179)
- **Original**: Canto XXXVI. The Birth Of Gangá. 161 In due degree, sate more remote, While Raghu's sons took nearer place By virtue of their rank and race. Then Ráma said:“O Saint, I yearn The three-pathed Gangá's tale to learn.” Thus urged, the sage recounted both The birth of Gangá and her growth: “The mighty hill with metals stored, Himálaya, is the mountains' lord, The father of a lovely pair Of daughters fairest of the fair: Their mother, offspring of the will Of Meru, everlasting hill, Mená, Himálaya's darling, graced With beauty of her dainty waist. Gangá was elder-born: then came The fair one known by Umá's name. Then all the Gods of heaven, in need Of Gangá's help their vows to speed, To great Himálaya came and prayed The mountain King to yield the maid. He, not regardless of the weal Of the three worlds, with holy zeal His daughter to the Immortals gave, Gangá whose waters cleanse and save, Who roams at pleasure, fair and free, Purging all sinners, to the sea. The three-pathed Gangá thus obtained, The Gods their heavenly homes regained. Long time the sister Umá passed In vows austere and rigid fast, And the king gave the devotee
- **Translation**: 

---

### Verse 15 (Ramayana 0.180)
- **Original**: 162 The Ramayana Immortal Rudra's180 bride to be, Matching with that unequalled Lord His Umá through the worlds adored. So now a glorious station fills Each daughter of the King of Hills: One honoured as the noblest stream, One mid the Goddesses supreme. Thus Gangá, King Himálaya's child, The heavenly river, undefiled, Rose bearing with her to the sky Her waves that bless and purify.” [I am compelled to omit Cantos XXXVII and XXXVIII, THE G LORY OF U MÁ , andTHE B IRTH OF K ÁRTIKEYA , as both in subject and language offensive to modern taste. They will be found in Schlegel's Latin translation.] Canto XXXIX. The Sons Of Sagar. The saint in accents sweet and clear Thus told his tale for Ráma's ear, And thus anew the holy man A legend to the prince began: “There reigned a pious monarch o'er Ayodhyá in the days of yore: Sagar his name: no child had he, And children much he longed to see. His honoured consort, fair of face, Sprang from Vidarbha's royal race, Ke [ini, famed from early youth 180 A name of the GodZiva.
- **Translation**: 

---

### Verse 16 (Ramayana 0.181)
- **Original**: Canto XXXIX. The Sons Of Sagar. 163 For piety and love of truth. Aríshmanemi's daughter fair, With whom no maiden might compare In beauty, though the earth is wide, Sumati, was his second bride. With his two queens afar he went, And weary days in penance spent, Fervent, upon Himálaya's hill Where springs the stream called Bhrigu' rill. Nor did he fail that saint to please With his devout austerities. And, when a hundred years had fled, Thus the most truthful Bhrigu said: “From thee, O Sagar, blameless King, A mighty host of sons shall spring, And thou shalt win a glorious name Which none, O Chief, but thou shall claim. One of thy queens a son shall bear, Maintainer of thy race and heir; And of the other there shall be Sons sixty thousand born to thee.” Thus as he spake, with one accord, To win the grace of that high lord, The queens, with palms together laid, In humble supplication prayed: “Which queen, O Bráhman, of the pair, The many, or the one shall bear? Most eager, Lord, are we to know, And as thou sayest be it so.” [050] With his sweet speech the saint replied: “Yourselves, O Queens, the choice decide. Your own discretion freely use Which shall the one or many choose:
- **Translation**: 

---

### Verse 17 (Ramayana 0.182)
- **Original**: 164 The Ramayana One shall the race and name uphold, The host be famous, strong, and bold. Which will have which?” Then Ke[ini The mother of one heir would be. Sumati, sister of the king181 Of all the birds that ply the wing, To that illustrious Bráhman sued That she might bear the multitude Whose fame throughout the world should sound For mighty enterprise renowned. Around the saint the monarch went, Bowing his head, most reverent. Then with his wives, with willing feet, Resought his own imperial seat. Time passed. The elder consort bare A son called Asamanj, the heir. Then Sumati, the younger, gave Birth to a gourd,182 O hero brave, Whose rind, when burst and cleft in two, Gave sixty thousand babes to view. All these with care the nurses laid In jars of oil; and there they stayed, Till, youthful age and strength complete, Forth speeding from each dark retreat, All peers in valour, years, and might, The sixty thousand came to light. Prince Asamanj, brought up with care, Scourge of his foes, was made the heir. But liegemen's boys he used to cast To Sarjú's waves that hurried past, Laughing the while in cruel glee 181 Garu a. 182 Ikshváku, the name of a king of Ayodhyá who is regarded as the founder of the Solar race, means also agourd. Hence, perhaps, the myth.
- **Translation**: 

---

### Verse 18 (Ramayana 0.183)
- **Original**: Canto XL. The Cleaving Of The Earth. 165 Their dying agonies to see. This wicked prince who aye withstood The counsel of the wise and good, Who plagued the people in his hate, His father banished from the state. His son, kind-spoken, brave, and tall, Was An [umán, beloved of all. Long years flew by. The king decreed To slay a sacrificial steed. Consulting with his priestly band He vowed the rite his soul had planned, And, Veda skilled, by their advice Made ready for the sacrifice. Canto XL. The Cleaving Of The Earth. The hermit ceased: the tale was done: Then in a transport Raghu's son Again addressed the ancient sire Resplendent as a burning fire: “O holy man, I fain would hear The tale repeated full and clear How he from whom my sires descend Brought the great rite to happy end.” The hermit answered with a smile: “Then listen, son of Raghu, while My legendary tale proceeds To tell of high-souled Sagar's deeds. Within the spacious plain that lies From where Himálaya's heights arise
- **Translation**: 

---

### Verse 19 (Ramayana 0.184)
- **Original**: 166 The Ramayana To where proud Vindhya's rival chain Looks down upon the subject plain— A land the best for rites declared183. — His sacrifice the king prepared. And An [umán the prince— for so Sagar advised— with ready bow Was borne upon a mighty car To watch the steed who roamed afar. But Indra, monarch of the skies, Veiling his form in demon guise, Came down upon the appointed day And drove the victim horse away. Reft of the steed the priests, distressed, The master of the rite addressed: “Upon the sacred day by force A robber takes the victim horse. Haste, King! now let the thief be slain; Bring thou the charger back again: The sacred rite prevented thus Brings scathe and woe to all of us. Rise, monarch, and provide with speed That naught its happy course impede.” 183 “The region here spoken of is called in the Laws of ManuMadhyade [a or the middle region.‘The region situated between the Himálaya and the Vindhya Mountains… is calledMadhyade [a, or the middle region; the space comprised between these two mountains from the eastern to the western sea is called by sages Áryávartta,the seat of honourable men.’(M ANU {FNS , II, 21, 22.) The Sanskrit Indians called themselves Áryans, which meanshonourable,noble, to distinguish themselves from the surrounding nations of different origin.” G ORRESIO {FNS
- **Translation**: 

---

### Verse 20 (Ramayana 0.185)
- **Original**: Canto XL. The Cleaving Of The Earth. 167 King Sagar in his crowded court Gave ear unto the priests' report. He summoned straightway to his side His sixty thousand sons, and cried: “Brave sons of mine, I knew not how These demons are so mighty now: The priests began the rite so well All sanctified with prayer and spell. If in the depths of earth he hide, Or lurk beneath the ocean's tide, [051] Pursue, dear sons, the robber's track; Slay him and bring the charger back. The whole of this broad earth explore, Sea-garlanded, from shore to shore: Yea, dig her up with might and main Until you see the horse again. Deep let your searching labour reach, A league in depth dug out by each. The robber of our horse pursue, And please your sire who orders you. My grandson, I, this priestly train, Till the steed comes, will here remain.” Their eager hearts with transport burned As to their task the heroes turned. Obedient to their father, they Through earth's recesses forced their way. With iron arms' unflinching toil Each dug a league beneath the soil. Earth, cleft asunder, groaned in pain, As emulous they plied amain Sharp-pointed coulter, pick, and bar, Hard as the bolts of Indra are. Then loud the horrid clamour rose
- **Translation**: 

---



--- End of Ramayan_batch_107.md ---


--- Start of Ramayan_batch_108.md ---

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

### Verse 1 (Ramayana 0.186)
- **Original**: 168 The Ramayana Of monsters dying neath their blows, Giant and demon, fiend and snake, That in earth's core their dwelling make. They dug, in ire that naught could stay, Through sixty thousand leagues their way, Cleaving the earth with matchless strength Till hell itself they reached at length. Thus digging searched they Jambudvip184 With all its hills and mountains steep. Then a great fear began to shake The heart of God, bard, fiend, and snake, And all distressed in spirit went Before the Sire Omnipotent. With signs of woe in every face They sought the mighty Father's grace, And trembling still and ill at ease Addressed their Lord in words like these: “The sons of Sagar, Sire benign, Pierce the whole earth with mine on mine, And as their ruthless work they ply Innumerable creatures die. “This is the thief,” the princes say, “Who stole our victim steed away. This marred the rite, and caused us ill, And so their guiltless blood they spill.” Canto XLI. Kapil. 184 Said to be so called from the Jambu, or Rose Apple, abounding in it, and signifying according to the Puránas the central division of the world, the known world.
- **Translation**: 

---

### Verse 2 (Ramayana 0.187)
- **Original**: Canto XLI. Kapil. 169 The father lent a gracious ear And listened to their tale of fear, And kindly to the Gods replied Whom woe and death had terrified: “The wisest Vásudeva,185 who The Immortals' foe, fierce Madhu, slew, Regards broad Earth with love and pride And guards, in Kapil's form, his bride.186 His kindled wrath will quickly fall On the king's sons and burn them all. This cleaving of the earth his eye Foresaw in ages long gone by: He knew with prescient soul the fate That Sagar's children should await.” The Three-and-thirty,187 freed from fear, Sought their bright homes with hopeful cheer. Still rose the great tempestuous sound As Sagar's children pierced the ground. When thus the whole broad earth was cleft, And not a spot unsearched was left, 185 Here used as a name of VishGu. 186 Kings are called the husbands of their kingdoms or of the earth;“She and his kingdom were his only brides.” RaghuvaE[a. “Doubly divorced! Bad men, you violate A double marriage, 'twixt my crown and me, And then between me and my married wife.” King Richard II. Act V. Sc. I. 187 The thirty-three Gods are said in theAitareya BráhmaGa, Book I. ch. II. 10. to be the eight Vasus, the eleven Rudras, the twelve Ádityas, Prajápati, either Brahmá or Daksha, and Vashatkára or deified oblation. This must have been the actual number at the beginning of the Vedic religion gradually increased by successive mythical and religious creations till the Indian Pantheon was crowded with abstractions of every kind. Through the reverence with which the words of the Veda were regarded, the immense host of multiplied divinities, in later times, still bore the name of the Thirty-three Gods.
- **Translation**: 

---

### Verse 3 (Ramayana 0.188)
- **Original**: 170 The Ramayana Back to their home the princes sped, And thus unto their father said: “We searched the earth from side to side, While countless hosts of creatures died. Our conquering feet in triumph trod On snake and demon, fiend and God; But yet we failed, with all our toil, To find the robber and the spoil. What can we more? If more we can, Devise, O King, and tell thy plan.” His children's speech King Sagar heard, And answered thus, to anger stirred: “Dig on, and ne'er your labour stay Till through earth's depths you force your way. Then smite the robber dead, and bring The charger back with triumphing.”[052] The sixty thousand chiefs obeyed: Deep through the earth their way they made. Deep as they dug and deeper yet The immortal elephant they met, Famed Vírúpáksha188 vast of size, Upon whose head the broad earth lies: The mighty beast who earth sustains 188 “One of the elephants which, according to an ancient belief popular in India, supported the earth with their enormous backs; when one of these elephants shook his wearied head the earth trembled with its woods and hills. An idea, or rather a mythical fancy, similar to this, but reduced to proportions less grand, is found in Virgil when he speaks of Enceladus buried under Ætna:” “adi semiustum fulmine corpus Urgeri mole hac, ingentemque insuper Ætnam Impositam, ruptis flammam expirare caminis; Et fessum quoties mutat latus, intre mere omnem iam, et cœ lum subtexere fumo.” Æneid. Lib. III. GORRESIO {FNS .
- **Translation**: 

---

### Verse 4 (Ramayana 0.189)
- **Original**: Canto XLI. Kapil. 171 With shaggy hills and wooded plains. When, with the changing moon, distressed, And longing for a moment's rest, His mighty head the monster shakes, Earth to the bottom reels and quakes. Around that warder strong and vast With reverential steps they passed. Nor, when the honour due was paid, Their downward search through earth delayed. But turning from the east aside Southward again their task they plied. There Mahápadma held his place, The best of all his mighty race, Like some huge hill, of monstrous girth, Upholding on his head the earth. When the vast beast the princes saw, They marvelled and were filled with awe. The sons of high-souled Sagar round That elephant in reverence wound. Then in the western region they With might unwearied cleft their way. There saw they with astonisht eyes Saumanas, beast of mountain size. Round him with circling steps they went With greetings kind and reverent.
- **Translation**: 

---

### Verse 5 (Ramayana 0.190)
- **Original**: 172 The Ramayana On, on— no thought of rest or stay— They reached the seat of Soma's sway. There saw they Bhadra, white as snow, With lucky marks that fortune show, Bearing the earth upon his head. Round him they paced with solemn tread, And honoured him with greetings kind, Then downward yet their way they mined. They gained the tract 'twixt east and north Whose fame is ever blazoned forth,189 And by a storm of rage impelled, Digging through earth their course they held. Then all the princes, lofty-souled, Of wondrous vigour, strong and bold, Saw Vásudeva190 standing there In Kapil's form he loved to wear, And near the everlasting God The victim charger cropped the sod. They saw with joy and eager eyes The fancied robber and the prize, And on him rushed the furious band Crying aloud, Stand, villain! stand! “Avaunt! avaunt!” great Kapil cried, His bosom flusht with passion's tide; 189 “The Devas and Asuras (Gods and Titans) fought in the east, the south, the west, and the north, and the Devas were defeated by the Asuras in all these directions. They then fought in the north-eastern direction; there the Devas did not sustain defeat. This direction isaparájitá,i.e.unconquerable. Thence one should do work in this direction, and have it done there; for such a one (alone) is able to clear off his debts.” H AUG 'S{FNS Aitareya Bráhmanam, Vol. II, p. 33. The debts here spoken of are a man's religious obligations to the Gods, the Pitaras or Manes, and men. 190 VishGu.
- **Translation**: 

---

### Verse 6 (Ramayana 0.191)
- **Original**: Canto XLII. Sagar's Sacrifice. 173 Then by his might that proud array All scorcht to heaps of ashes lay.191 Canto XLII. Sagar's Sacrifice. Then to the prince his grandson, bright With his own fame's unborrowed light, King Sagar thus began to say, Marvelling at his sons' delay: “Thou art a warrior skilled and bold, Match for the mighty men of old. Now follow on thine uncles' course And track the robber of the horse. [053] To guard thee take thy sword and bow, for huge and strong are beasts below. There to the reverend reverence pay, And kill the foes who check thy way; Then turn successful home and see My sacrifice complete through thee.” 191 “It appears to me that this mythical story has reference to the volcanic phenomena of nature. Kapil may very possibly be that hidden fiery force which suddenly unprisons itself and bursts forth in volcanic effects. Kapil is, moreover, one of the names of Agni the God of Fire.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 7 (Ramayana 0.192)
- **Original**: 174 The Ramayana Obedient to the high-souled lord Grasped An[umán his bow and sword, And hurried forth the way to trace With youth and valour's eager pace. On sped he by the path he found Dug by his uncles underground. The warder elephant he saw Whose size and strength pass Nature's law, Who bears the world's tremendous weight, Whom God, fiend, giant venerate, Bird, serpent, and each flitting shade, To him the honour meet he paid With circling steps and greeting due, And further prayed him, if he knew, To tell him of his uncles' weal, And who had dared the horse to steal. To him in war and council tried The warder elephant replied: “Thou, son of Asamanj, shalt lead In triumph back the rescued steed.” As to each warder beast he came And questioned all, his words the same, The honoured youth with gentle speech Drew eloquent reply from each, That fortune should his steps attend, And with the horse he home should wend. Cheered with the grateful answer, he Passed on with step more light and free, And reached with careless heart the place Where lay in ashes Sagar's race. Then sank the spirit of the chief Beneath that shock of sudden grief, And with a bitter cry of woe
- **Translation**: 

---

### Verse 8 (Ramayana 0.193)
- **Original**: Canto XLII. Sagar's Sacrifice. 175 He mourned his kinsmen fallen so. He saw, weighed down by woe and care, The victim charger roaming there. Yet would the pious chieftain fain Oblations offer to the slain: But, needing water for the rite, He looked and there was none in sight His quick eye searching all around The uncle of his kinsmen found, King Garu , best beyond compare Of birds who wing the fields of air. Then thus unto the weeping man The son of Vinatá192 began: “Grieve not, O hero, for their fall Who died a death approved of all. Of mighty strength, they met their fate By Kapil's hand whom none can mate. Pour forth for them no earthly wave, A holier flood their spirits crave. If, daughter of the Lord of Snow, Gangá would turn her stream below, Her waves that cleanse all mortal stain Would wash their ashes pure again. Yea, when her flood whom all revere Rolls o'er the dust that moulders here, The sixty thousand, freed from sin, A home in Indra's heaven shall win. Go, and with ceaseless labour try To draw the Goddess from the sky. Return, and with thee take the steed; So shall thy grandsire's rite succeed.” 192 Garu was the son of Ka[yap and Vinatá.
- **Translation**: 

---

### Verse 9 (Ramayana 0.194)
- **Original**: 176 The Ramayana Prince An[umán the strong and brave Followed the rede SuparGa193 gave. The glorious hero took the horse, And homeward quickly bent his course. Straight to the anxious king he hied, Whom lustral rites had purified, The mournful story to unfold And all the king of birds had told. The tale of woe the monarch heard, Nor longer was the rite deferred: With care and just observance he Accomplished all, as texts decree. The rites performed, with brighter fame, Mighty in counsel, home he came. He longed to bring the river down, But found no plan his wish to crown. He pondered long with anxious thought But saw no way to what he sought. Thus thirty thousand years he spent, And then to heaven the monarch went. Canto XLIII. Bhagírath. When Sagar thus had bowed to fate, The lords and commons of the state Approved with ready heart and will Prince An[umán his throne to fill. He ruled, a mighty king, unblamed, Sire of Dilípa justly famed. 193 Garu .
- **Translation**: 

---

### Verse 10 (Ramayana 0.195)
- **Original**: Canto XLIII. Bhagírath. 177 To him, his child and worthy heir, The king resigned his kingdom's care, And on Himálaya's pleasant side His task austere of penance plied. Bright as a God in clear renown He planned to bring pure Gangá down. There on his fruitless hope intent Twice sixteen thousand years he spent, And in the grove of hermits stayed Till bliss in heaven his rites repaid. Dilípa then, the good and great, Soon as he learnt his kinsmen's fate, Bowed down by woe, with troubled mind, [054] Pondering long no cure could find. “How can I bring,” the mourner sighed, “To cleanse their dust, the heavenly tide? How can I give them rest, and save Their spirits with the offered wave?” Long with this thought his bosom skilled In holy discipline was filled. A son was born, Bhagírath named, Above all men for virtue famed. Dilípa many a rite ordained, And thirty thousand seasons reigned. But when no hope the king could see His kinsmen from their woe to free, The lord of men, by sickness tried, Obeyed the law of fate, and died; He left the kingdom to his son, And gained the heaven his deeds had won. The good Bhagírath, royal sage, Had no fair son to cheer his age. He, great in glory, pure in will, Longing for sons was childless still.
- **Translation**: 

---

### Verse 11 (Ramayana 0.196)
- **Original**: 178 The Ramayana Then on one wish, one thought intent, Planning the heavenly stream's descent, Leaving his ministers the care And burden of his state to bear, Dwelling in far Gokarna194 he Engaged in long austerity. With senses checked, with arms upraised, Five fires195 around and o'er him blazed. Each weary month the hermit passed Breaking but once his awful fast. In winter's chill the brook his bed, In rain, the clouds to screen his head. Thousands of years he thus endured Till Brahmá's favour was assured, And the high Lord of living things Looked kindly on his sufferings. With trooping Gods the Sire came near The king who plied his task austere: “Blest Monarch, of a glorious race, Thy fervent rites have won my grace. Well hast thou wrought thine awful task: Some boon in turn, O Hermit, ask.” Bhagírath, rich in glory's light, The hero with the arm of might, Thus to the Lord of earth and sky Raised suppliant hands and made reply: “If the great God his favour deigns, And my long toil its fruit obtains, Let Sagar's sons receive from me Libations that they long to see. Let Gangá with her holy wave 194 A famous and venerated region near the Malabar coast. 195 That is four fires and the sun.
- **Translation**: 

---

### Verse 12 (Ramayana 0.197)
- **Original**: Canto XLIV. The Descent Of Gangá. 179 The ashes of the heroes lave, That so my kinsmen may ascend To heavenly bliss that ne'er shall end. And give, I pray, O God, a son, Nor let my house be all undone. Sire of the worlds! be this the grace Bestowed upon Ikshváku's race.” The Sire, when thus the king had prayed, In sweet kind words his answer made. “High, high thy thought and wishes are, Bhagírath of the mighty car! Ikshváku's line is blest in thee, And as thou prayest it shall be. Gangá, whose waves in Swarga196 flow, Is daughter of the Lord of Snow. Win Ziva that his aid be lent To hold her in her mid descent, For earth alone will never bear Those torrents hurled from upper air; And none may hold her weight but He, The Trident wielding deity.” Thus having said, the Lord supreme Addressed him to the heavenly stream; And then with Gods and Maruts197 went To heaven above the firmament. Canto XLIV. The Descent Of Gangá. 196 Heaven. 197 Wind-Gods.
- **Translation**: 

---

### Verse 13 (Ramayana 0.198)
- **Original**: 180 The Ramayana The Lord of life the skies regained: The fervent king a year remained With arms upraised, refusing rest While with one toe the earth he pressed, Still as a post, with sleepless eye, The air his food, his roof the sky. The year had past. Then Umá's lord,198 King of creation, world adored, Thus spoke to great Bhagírath:“I, Well pleased thy wish will gratify, And on my head her waves shall fling The daughter of the Mountains' King!” He stood upon the lofty crest That crowns the Lord of Snow, And bade the river of the Blest Descend on earth below. Himálaya's child, adored of all, The haughty mandate heard, And her proud bosom, at the call, With furious wrath was stirred. Down from her channel in the skies With awful might she sped With a giant's rush, in a giant's size, On Ziva's holy head. “He calls me,” in her wrath she cried, “And all my flood shall sweep And whirl him in its whelming tide To hell's profoundest deep.” He held the river on his head, And kept her wandering, where, Dense as Himálaya's woods, were spread The tangles of his hair.[055] 198 Ziva.
- **Translation**: 

---

### Verse 14 (Ramayana 0.199)
- **Original**: Canto XLIV. The Descent Of Gangá. 181 No way to earth she found, ashamed, Though long and sore she strove, Condemned, until her pride were tamed, Amid his locks to rove. There, many lengthening seasons through, The wildered river ran: Bhagírath saw it, and anew His penance dire began. Then Ziva, for the hermit's sake, Bade her long wanderings end, And sinking into Vindu's lake Her weary waves descend. From Gangá, by the God set free, Seven noble rivers came; Hládiní, Pávaní, and she Called Naliní by name: These rolled their lucid waves along And sought the eastern side. Suchakshu, Sítá fair and strong, And Sindhu's mighty tide— 199 These to the region of the west With joyful waters sped: The seventh, the brightest and the best, Flowed where Bhagírath led. On Ziva's head descending first A rest the torrents found: Then down in all their might they burst And roared along the ground. On countless glittering scales the beam Of rosy morning flashed, 199 The lake Vindu does not exist. Of the seven rivers here mentioned two only, the Ganges and the Sindhu or Indus, are known to geographers. Hládiní means the Gladdener, Pávaní the Purifier, Naliní the Lotus-Clad, and Suchakshu the Fair-eyed.
- **Translation**: 

---

### Verse 15 (Ramayana 0.200)
- **Original**: 182 The Ramayana Where fish and dolphins through the stream Fallen and falling dashed. Then bards who chant celestial lays And nymphs of heavenly birth Flocked round upon that flood to gaze That streamed from sky to earth. The Gods themselves from every sphere, Incomparably bright, Borne in their golden cars drew near To see the wondrous sight. The cloudless sky was all aflame With the light of a hundred suns Where'er the shining chariots came That bore those holy ones. So flashed the air with crested snakes And fish of every hue As when the lightning's glory breaks Through fields of summer blue. And white foam-clouds and silver spray Were wildly tossed on high, Like swans that urge their homeward way Across the autumn sky. Now ran the river calm and clear With current strong and deep: Now slowly broadened to a mere, Or scarcely seemed to creep. Now o'er a length of sandy plain Her tranquil course she held; Now rose her waves and sank again, By refluent waves repelled. So falling first onZiva's head, Thence rushing to their earthly bed, In ceaseless fall the waters streamed, And pure with holy lustre gleamed.
- **Translation**: 

---

### Verse 16 (Ramayana 0.201)
- **Original**: Canto XLIV. The Descent Of Gangá. 183 Then every spirit, sage, and bard, Condemned to earth by sentence hard, Pressed eagerly around the tide ThatZiva's touch had sanctified. Then they whom heavenly doom had hurled, Accursed, to this lower world, Touched the pure wave, and freed from sin Resought the skies and entered in. And all the world was glad, whereon The glorious water flowed and shone, For sin and stain were banished thence By the sweet river's influence. First, in a car of heavenly frame, The royal saint of deathless name, Bhagírath, very glorious rode, And after him fair Gangá flowed. God, sage, and bard, the chief in place Of spirits and the Nága race, Nymph, giant, fiend, in long array Sped where Bhagírath led the way; And all the hosts the flood that swim Followed the stream that followed him. Where'er the great Bhagírath led, There ever glorious Gangá fled, The best of floods, the rivers' queen, Whose waters wash the wicked clean. It chanced that Jahnu, great and good, Engaged with holy offerings stood; The river spread her waves around Flooding his sacrificial ground. The saint in anger marked her pride, And at one draught her stream he dried. Then God, and sage, and bard, afraid,
- **Translation**: 

---

### Verse 17 (Ramayana 0.202)
- **Original**: 184 The Ramayana To noble high-souled Jahnu prayed, And begged that he would kindly deem His own dear child that holy stream. Moved by their suit, he soothed their fears And loosed her waters from his ears. Hence Gangá through the world is styled Both Jáhnavi and Jahnu's child. Then onward still she followed fast, And reached the great sea bank at last. Thence deep below her way she made To end those rites so long delayed. The monarch reached the Ocean's side, And still behind him Gangá hied. He sought the depths which open lay Where Sagar's sons had dug their way. So leading through earth's nether caves The river's purifying waves,[056] Over his kinsmen's dust the lord His funeral libation poured. Soon as the flood their dust bedewed, Their spirits gained beatitude, And all in heavenly bodies dressed Rose to the skies' eternal rest. Then thus to King Bhagírath said Brahmá, when, coming at the head Of all his bright celestial train, He saw those spirits freed from stain: “Well done! great Prince of men, well done! Thy kinsmen bliss and heaven have won. The sons of Sagar mighty-souled, Are with the Blest, as Gods, enrolled, Long as the Ocean's flood shall stand Upon the border of the land,
- **Translation**: 

---

### Verse 18 (Ramayana 0.203)
- **Original**: Canto XLIV. The Descent Of Gangá. 185 So long shall Sagar's sons remain, And, godlike, rank in heaven retain. Gangá thine eldest child shall be, Called from thy name Bhágirathí; Named also— for her waters fell From heaven and flow through earth and hell— Tripathagá, stream of the skies, Because three paths she glorifies. And, mighty King, 'tis given thee now To free thee and perform thy vow. No longer, happy Prince, delay Drink-offerings to thy kin to pay. For this the holiest Sagar sighed, But mourned the boon he sought denied. Then An[umán, dear Prince! although No brighter name the world could show, Strove long the heavenly flood to gain To visit earth, but strove in vain. Nor was she by the sages' peer, Blest with all virtues, most austere, Thy sire Dilípa, hither brought, Though with fierce prayers the boon he sought. But thou, O King, earned success, And won high fame which God will bless. Through thee, O victor of thy foes, On earth this heavenly Gangá flows, And thou hast gained the meed divine That waits on virtue such as thine. Now in her ever holy wave Thyself, O best of heroes, lave: So shalt thou, pure from every sin, The blessed fruit of merit win. Now for thy kin who died of yore The meet libations duly pour.
- **Translation**: 

---

### Verse 19 (Ramayana 0.204)
- **Original**: 186 The Ramayana Above the heavens I now ascend: Depart, and bliss thy steps attend.” Thus to the mighty king who broke His foemens' might, Lord Brahmá spoke, And with his Gods around him rose To his own heaven of blest repose. The royal sage no more delayed, But, the libation duly paid, Home to his regal city hied With water cleansed and purified. There ruled he his ancestral state, Best of all men, most fortunate. And all the people joyed again In good Bhagírath's gentle reign. Rich, prosperous, and blest were they, And grief and sickness fled away. Thus, Ráma, I at length have told How Gangá came from heaven of old. Now, for the evening passes swift, I wish thee each auspicious gift. This story of the flood's descent Will give— for 'tis most excellent— Wealth, purity, fame, length of days, And to the skies its hearers raise” Canto XLV. The Quest Of The Amrit.
- **Translation**: 

---

### Verse 20 (Ramayana 0.205)
- **Original**: Canto XLV. The Quest Of The Amrit. 187 High and more high their wonder rose As the strange story reached its close, And thus, with LakshmaG, Ráma, best Of Raghu's sons, the saint addressed: “Most wondrous is the tale which thou Hast told of heavenly Gangá, how From realms above descending she Flowed through the land and filled the sea. In thinking o'er what thou hast said The night has like a moment fled, Whose hours in musing have been spent Upon thy words most excellent: So much, O holy Sage, thy lore Has charmed us with this tale of yore.” Day dawned. The morning rites were done And the victorious Raghu's son Addressed the sage in words like these, Rich in his long austerities: “The night is past: the morn is clear; Told is the tale so good to hear: Now o'er that river let us go, Three-pathed, the best of all that flow. This boat stands ready on the shore To bear the holy hermits o'er, Who of thy coming warned, in haste, The barge upon the bank have placed.” And Ku [ik's son approved his speech, And moving to the sandy beach, Placed in the boat the hermit band, And reached the river's further strand. On the north bank their feet they set, And greeted all the saints they met.
- **Translation**: 

---



--- End of Ramayan_batch_108.md ---


--- Start of Ramayan_batch_109.md ---

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

### Verse 1 (Ramayana 0.206)
- **Original**: 188 The Ramayana On Gangá's shore they lighted down, And saw Vi[álá's lovely town. Thither, the princes by his side, The best of holy hermits hied. It was a town exceeding fair[057] That might with heaven itself compare. Then, suppliant palm to palm applied, Famed Ráma asked his holy guide: “O best of hermits, say what race Of monarchs rules this lovely place. Dear master, let my prayer prevail, For much I long to hear the tale.” Moved by his words, the saintly man Vi[álá's ancient tale began: “List, Ráma, list, with closest heed The tale of Indra's wondrous deed, And mark me as I truly tell What here in ancient days befell. Ere Krita's famous Age200 had fled, Strong were the sons of Diti201 bred; And Aditi's brave children too Were very mighty, good, and true. The rival brothers fierce and bold Were sons of Ka[yap lofty-souled. Of sister mothers born, they vied, Brood against brood, in jealous pride. Once, as they say, band met with band, And, joined in awful council, planned To live, unharmed by age and time, Immortal in their youthful prime. Then this was, after due debate, 200 The First or Golden Age. 201 Diti and Aditi were wives of Ka[yap, and mothers respectively of Titans and Gods.
- **Translation**: 

---

### Verse 2 (Ramayana 0.207)
- **Original**: Canto XLV. The Quest Of The Amrit. 189 The counsel of the wise and great, To churn with might the milky sea202 The life-bestowing drink to free. This planned, they seized the Serpent King, Vásuki, for their churning-string, And Mandar's mountain for their pole, And churned with all their heart and soul. As thus, a thousand seasons through, This way and that the snake they drew, Biting the rocks, each tortured head, A very deadly venom shed. Thence, bursting like a mighty flame, A pestilential poison came, Consuming, as it onward ran, The home of God, and fiend, and man. Then all the suppliant Gods in fear To Zankar,203 mighty lord, drew near. To Rudra, King of Herds, dismayed, “Save us, O save us, Lord!” they prayed. Then VishGu, bearing shell, and mace, And discus, showed his radiant face, And thus addressed in smiling glee The Trident wielding deity: “What treasure first the Gods upturn From troubled Ocean, as they churn, Should— for thou art the eldest— be Conferred, O best of Gods, on thee. Then come, and for thy birthright's sake, This venom as thy first fruits take.” He spoke, and vanished from their sight, When Ziva saw their wild affright, And heard his speech by whom is borne 202 One of the seven seas surrounding as many worlds in concentric rings. 203 Zankar and Rudra are names ofZiva.
- **Translation**: 

---

### Verse 3 (Ramayana 0.208)
- **Original**: 190 The Ramayana The mighty bow of bending horn,204 The poisoned flood at once he quaffed As 'twere the Amrit's heavenly draught. Then from the Gods departing went Ziva, the Lord pre-eminent. The host of Gods and Asurs still Kept churning with one heart and will. But Mandar's mountain, whirling round, Pierced to the depths below the ground. Then Gods and bards in terror flew To him who mighty Madhu slew. “Help of all beings! more than all, The Gods on thee for aid may call. Ward off, O mighty-armed! our fate, And bear up Mandar's threatening weight.” Then VishGu, as their need was sore, The semblance of a tortoise wore, And in the bed of Ocean lay The mountain on his back to stay. Then he, the soul pervading all, Whose locks in radiant tresses fall, One mighty arm extended still, And grasped the summit of the hill. So ranged among the Immortals, he Joined in the churning of the sea. 204 “ZárEgin, literallycarrying a bow of horn, is a constantly recurring name of VishGu. The Indians also, therefore, knew the art of making bows out of the hons of antelopes or wild goats, which Homer ascribes to the Trojans of the heroic age.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 4 (Ramayana 0.209)
- **Original**: Canto XLV. The Quest Of The Amrit. 191 A thousand years had reached their close, When calmly from the ocean rose The gentle sage205 with staff and can, Lord of the art of healing man. Then as the waters foamed and boiled, As churning still the Immortals toiled, Of winning face and lovely frame, Forth sixty million fair ones came. Born of the foam and water, these Were aptly named Apsarases.206 [058] Each had her maids. The tongue would fail— So vast the throng— to count the tale. But when no God or Titan wooed A wife from all that multitude, Refused by all, they gave their love In common to the Gods above. Then from the sea still vext and wild Rose Surá,207 VaruG's maiden child. A fitting match she sought to find: But Diti's sons her love declined, 205 Dhanvantari, the physician of the Gods. 206 The poet plays upon the word and fancifully derives it fromapsu, the locative case plural ofap, water, andrasa, taste.… The word is probably derived fromap, water, andsri, to go, and seems to signifyinhabitants of the water, nymphs of the stream; or, as Goldstücker thinks (Dict. s.v.) these divinities were originally personifications of the vapours which are attracted by the sun and form into mist or clouds. 207 “Surá, in the feminine comprehends all sorts of intoxicating liquors, many kinds of which the Indians from the earliest times distilled and prepared from rice, sugar-cane, the palm tree, and various flowers and plants. Nothing is considered more disgraceful among orthodox Hindus than drunkenness, and the use of wine is forbidden not only to Bráhmans but the two other orders as well.… So it clearly appears derogatory to the dignity of the Gods to have received a nymph so pernicious, who ought rather to have been made over to the Titans. However the etymological fancy has prevailed. The wordSura, a God, is derived from the indeclinableSwar heaven.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 5 (Ramayana 0.210)
- **Original**: 192 The Ramayana Their kinsmen of the rival brood To the pure maid in honour sued. Hence those who loved that nymph so fair The hallowed name of Suras bear. And Asurs are the Titan crowd Her gentle claims who disallowed. Then from the foamy sea was freed Uchchaih[ravas,208 the generous steed, And Kaustubha, of gems the gem,209 And Soma, Moon God, after them. At length when many a year had fled, Up floated, on her lotus bed, A maiden fair and tender-eyed, In the young flush of beauty's pride. She shone with pearl and golden sheen, And seals of glory stamped her queen, On each round arm glowed many a gem, On her smooth brows, a diadem. Rolling in waves beneath her crown The glory of her hair flowed down, Pearls on her neck of price untold, The lady shone like burnisht gold. Queen of the Gods, she leapt to land, A lotus in her perfect hand, And fondly, of the lotus-sprung, To lotus-bearing VishGu clung. 208 Literally, high-eared, the horse of Indra. Compare the production of the horse from the sea by Neptune. 209 “And Kaustubha the best Of gems that burns with living light Upon Lord VishGu's breast.” Churning of the Ocean.
- **Translation**: 

---

### Verse 6 (Ramayana 0.211)
- **Original**: Canto XLV. The Quest Of The Amrit. 193 Her Gods above and men below As Beauty's Queen and Fortune know.210 Gods, Titans, and the minstrel train Still churned and wrought the troubled main. At length the prize so madly sought, The Amrit, to their sight was brought. For the rich spoil, 'twixt these and those A fratricidal war arose, And, host 'gainst host in battle, set, Aditi's sons and Diti's met. United, with the giants' aid, Their fierce attack the Titans made, And wildly raged for many a day That universe-astounding fray. When wearied arms were faint to strike, And ruin threatened all alike, VishGu, with art's illusive aid, The Amrit from their sight conveyed. That Best of Beings smote his foes Who dared his deathless arm oppose: Yea, VishGu, all-pervading God, Beneath his feet the Titans trod Aditi's race, the sons of light, slew Diti's brood in cruel fight. 210 “That this story of the birth of Lakshmí is of considerable antiquity is evident from one of her namesKshírábdhi-tanayá, daughter of the Milky Sea, which is found inAmarasinha the most ancient of Indian lexicographers. The similarity to the Greek myth of Venus being born from the foam of the sea is remarkable.” “In this description of Lakshmí one thing only offends me, that she is said to have four arms. Each of VishGu's arms, single, as far as the elbow, there branches into two; but Lakshmí in all the brass seals that I possess or remember to have seen has two arms only. Nor does this deformity of redundant limbs suit the pattern of perfect beauty.” SCHLEGEL {FNS . I have omitted the offensive epithet.
- **Translation**: 

---

### Verse 7 (Ramayana 0.212)
- **Original**: 194 The Ramayana Then town-destroying211 Indra gained His empire, and in glory reigned O'er the three worlds with bard and sage Rejoicing in his heritage. Canto XLVI. Diti's Hope. But Diti, when her sons were slain, Wild with a childless mother's pain, To Ka[yap spake, Marícha's son, Her husband:“O thou glorious one![059] Dead are the children, mine no more, The mighty sons to thee I bore. Long fervour's meed, I crave a boy Whose arm may Indra's life destroy. The toil and pain my care shall be: To bless my hope depends on thee. Give me a mighty son to slay Fierce Indra, gracious lord! I pray.” 211 Purandhar, a common title of Indra.
- **Translation**: 

---

### Verse 8 (Ramayana 0.213)
- **Original**: Canto XLVI. Diti's Hope. 195 Then glorious Ka[yap thus replied To Diti, as she wept and sighed: “Thy prayer is heard, dear saint! Remain Pure from all spot, and thou shalt gain A son whose arm shall take the life Of Indra in the battle strife. For full a thousand years endure Free from all stain, supremely pure; Then shall thy son and mine appear, Whom the three worlds shall serve with fear.” These words the glorious Ka[yap said, Then gently stroked his consort's head, Blessed her, and bade a kind adieu, And turned him to his rites anew. Soon as her lord had left her side, Her bosom swelled with joy and pride. She sought the shade of holy boughs, And there began her awful vows. While yet she wrought her rites austere, Indra, unbidden, hastened near, With sweet observance tending her, A reverential minister. Wood, water, fire, and grass he brought, Sweet roots and woodland fruit he sought, And all her wants, the Thousand-eyed, With never-failing care, supplied, With tender love and soft caress Removing pain and weariness. When, of the thousand years ordained, Ten only unfulfilled remained, Thus to her son, the Thousand-eyed, The Goddess in her triumph cried: “Best of the mighty! there remain
- **Translation**: 

---

### Verse 9 (Ramayana 0.214)
- **Original**: 196 The Ramayana But ten short years of toil and pain; These years of penance soon will flee, And a new brother thou shalt see. Him for thy sake I'll nobly breed, And lust of war his soul shall feed; Then free from care and sorrow thou Shalt see the worlds before him bow.”212 Canto XLVII. Sumati. Thus to Lord Indra, Thousand-eyed, Softly beseeching Diti sighed. When but a blighted bud was left, Which Indra's hand in seven had cleft:213 “No fault, O Lord of Gods, is thine; The blame herein is only mine. But for one grace I fain would pray, As thou hast reft this hope away. This bud, O Indra, which a blight Has withered ere it saw the light— From this may seven fair spirits rise To rule the regions of the skies. Be theirs through heaven's unbounded space 212 A few verses are here left untranslated on account of the subject and language being offensive to modern taste. 213 “In this myth of Indra destroying the unborn fruit of Diti with his thun- derbolt, from which afterwards came the Maruts or Gods of Wind and Storm, geological phenomena are, it seems, represented under mythical images. In the great Mother of the Gods is, perhaps, figured the dry earth: Indra the God of thunder rends it open, and there issue from its rent bosom the Maruts or exhalations of the earth. But such ancient myths are difficult to interpret with absolute certainty.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 10 (Ramayana 0.215)
- **Original**: Canto XLVII. Sumati. 197 On shoulders of the winds to race, My children, drest in heavenly forms, Far-famed as Maruts, Gods of storms. One God to Brahmá's sphere assign, Let one, O Indra, watch o'er thine; And ranging through the lower air, The third the name of Váyu214 bear. Gods let the four remaining be, And roam through space, obeying thee.” The Town-destroyer, Thousand-eyed, Who smote fierce Bali till he died, Joined suppliant hands, and thus replied: “Thy children heavenly forms shall wear; The names devised by thee shall bear, And, Maruts called by my decree, Shall Amrit drink and wait on me. From fear and age and sickness freed, Through the three worlds their wings shall speed.” Thus in the hermits' holy shade Mother and son their compact made, And then, as fame relates, content, Home to the happy skies they went. This is the spot— so men have told— Where Lord Mahendra215 dwelt of old, This is the blessed region where His votaress mother claimed his care. Here gentle Alambúshá bare To old Ikshváku, king and sage, Vi[ála, glory of his age, By whom, a monarch void of guilt, Was this fair town Vi[álá built. [060] 214 Wind. 215 Indra, withmahá , great, prefixed.
- **Translation**: 

---

### Verse 11 (Ramayana 0.216)
- **Original**: 198 The Ramayana His son was Hemachandra, still Renowned for might and warlike skill. From him the great Suchandra came; His son, Dhúmrá[va, dear to fame. Next followed royal Srinjay; then Famed Sahadeva, lord of men. Next came Ku[á[va, good and mild, Whose son was Somadatta styled, And Sumati, his heir, the peer Of Gods above, now governs here. And ever through Ikshváku's grace, Vi[álá's kings, his noble race, Are lofty-souled, and blest with length Of days, with virtue, and with strength. This night, O prince, we here will sleep; And when the day begins to peep, Our onward way will take with thee, The king of Míthilá to see.” Then Sumati, the king, aware Of Vi[vámitra's advent there, Came quickly forth with honour meet The lofty-minded sage to greet. Girt with his priest and lords the king Did low obeisance, worshipping, With suppliant hands, with head inclined, Thus spoke he after question kind; “Since thou hast deigned to bless my sight, And grace awhile thy servant's seat, High fate is mine, great Anchorite, And none may with my bliss compete.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.217)
- **Original**: Canto XLVIII. Indra And Ahalyá 199 Canto XLVIII. Indra And Ahalyá When mutual courtesies had past, Vi[álá's ruler spoke at last: “These princely youths, O Sage, who vie In might with children of the sky, Heroic, born for happy fate, With elephants' or lions' gait, Bold as the tiger or the bull, With lotus eyes so large and full, Armed with the quiver, sword, and bow, Whose figures like the A[vins216 show, Like children of the deathless Powers, Come freely to these shades of ours,217— How have they reached on foot this place? What do they seek, and what their race? As sun and moon adorn the sky, This spot the heroes glorify. Alike in stature, port, and mien, The same fair form in each is seen,” He spoke; and at the monarch's call The best of hermits told him all, How in the grove with him they dwelt, And slaughter to the demons dealt. Then wonder filled the monarch's breast, Who tended well each royal guest. Thus entertained, the princely pair Remained that night and rested there, And with the morn's returning ray To Mithilá pursued their way. 216 The Heavenly Twins. 217 Not banished from heaven as the inferior Gods and demigods sometimes were.
- **Translation**: 

---

### Verse 13 (Ramayana 0.218)
- **Original**: 200 The Ramayana When Janak's lovely city first Upon their sight, yet distant, burst, The hermits all with joyful cries Hailed the fair town that met their eyes. Then Ráma saw a holy wood, Close, in the city's neighbourhood, O'ergrown, deserted, marked by age, And thus addressed the mighty sage: “O reverend lord. I long to know What hermit dwelt here long ago.” Then to the prince his holy guide, Most eloquent of men, replied: “O Ráma, listen while I tell Whose was this grove, and what befell When in the fury of his rage The high saint cursed the hermitage. This was the grove— most lovely then— Of Gautam, O thou best of men, Like heaven itself, most honoured by The Gods who dwell above the sky. Here with Ahalyá at his side His fervid task the ascetic plied. Years fled in thousands. On a day It chanced the saint had gone away, When Town-destroying Indra came, And saw the beauty of the dame. The sage's form the God endued, And thus the fair Ahalyá wooed: “Love, sweet! should brook no dull delay But snatch the moments when he may.” She knew him in the saint's disguise, Lord Indra of the Thousand Eyes, But touched by love's unholy fire, She yielded to the God's desire.
- **Translation**: 

---

### Verse 14 (Ramayana 0.219)
- **Original**: Canto XLVIII. Indra And Ahalyá 201 “Now, Lord of Gods!” she whispered,“flee, From Gautam save thyself and me.” Trembling with doubt and wild with dread Lord Indra from the cottage fled; But fleeing in the grove he met The home-returning anchoret, Whose wrath the Gods and fiends would shun, Such power his fervent rites had won. Fresh from the lustral flood he came, In splendour like the burning flame, With fuel for his sacred rites, And grass, the best of eremites. The Lord of Gods was sad of cheer To see the mighty saint so near, And when the holy hermit spied In hermit's garb the Thousand-eyed, [061] He knew the whole, his fury broke Forth on the sinner as he spoke: “Because my form thou hast assumed, And wrought this folly, thou art doomed, For this my curse to thee shall cling, Henceforth a sad and sexless thing.” No empty threat that sentence came, It chilled his soul and marred his frame, His might and godlike vigour fled, And every nerve was cold and dead. Then on his wife his fury burst, And thus the guilty dame he cursed: “For countless years, disloyal spouse, Devoted to severest vows, Thy bed the ashes, air thy food, Here shalt thou live in solitude.
- **Translation**: 

---

### Verse 15 (Ramayana 0.220)
- **Original**: 202 The Ramayana This lonely grove thy home shall be, And not an eye thy form shall see. When Ráma, Da [aratha's child, Shall seek these shades then drear and wild, His coming shall remove thy stain, And make the sinner pure again. Due honour paid to him, thy guest, Shall cleanse thy fond and erring breast, Thee to my side in bliss restore, And give thy proper shape once more.”218 Thus to his guilty wife he said, Then far the holy Gautam fled, And on Himálaya's lovely heights Spent the long years in sternest rites.” Canto XLIX. Ahalyá Freed. Then Ráma, following still his guide, Within the grove, with LakshmaG, hied, Her vows a wondrous light had lent To that illustrious penitent. He saw the glorious lady, screened From eye of man, and God, and fiend, Like some bright portent which the care 218 Kumárila says:“In the same manner, if it is said that Indra was the seducer of Ahalyá this does not imply that the God Indra committed such a crime, but Indra means the sun, and Ahalyá (from ahan and lí) the night; and as the night is seduced and ruined by the sun of the morning, therefore is Indra called the paramour of Ahalyá.” M AX M ULLER {FNS , History of Ancient Sanskrit Literature, p. 530.
- **Translation**: 

---

### Verse 16 (Ramayana 0.221)
- **Original**: Canto XLIX. Ahalyá Freed. 203 Of Brahmá launches through the air, Designed by his illusive art To flash a moment and depart: Or like the flame that leaps on high To sink involved in smoke and die: Or like the full moon shining through The wintry mist, then lost to view: Or like the sun's reflection, cast Upon the flood, too bright to last: So was the glorious dame till then Removed from Gods' and mortals' ken, Till— such was Gautam's high decree— Prince Ráma came to set her free. Then, with great joy that dame to meet, The sons of Raghu clapped her feet; And she, remembering Gautam's oath, With gentle grace received them both; Then water for their feet she gave, Guest-gift, and all that strangers crave. The prince, of courteous rule aware, Received, as meet, the lady's care. Then flowers came down in copious rain, And moving to the heavenly strain Of music in the skies that rang, The nymphs and minstrels danced and sang: And all the Gods with one glad voice Praised the great dame, and cried,“Rejoice! Through fervid rites no more defiled, But with thy husband reconciled.” Gautam, the holy hermit knew— For naught escaped his godlike view— That Ráma lodged beneath that shade,
- **Translation**: 

---

### Verse 17 (Ramayana 0.222)
- **Original**: 204 The Ramayana And hasting there his homage paid. He took Ahalyá to his side, From sin and folly purified, And let his new-found consort bear In his austerities a share. Then Ráma, pride of Raghu's race, Welcomed by Gautam, face to face, Who every highest honour showed, To Mithilá pursued his road. Canto L. Janak. The sons of Raghu journeyed forth, Bending their steps 'twixt east and north. Soon, guided by the sage, they found, Enclosed, a sacrificial ground. Then to the best of saints, his guide, In admiration Ráma cried: “The high-souled king no toil has spared, But nobly for his rite prepared, How many thousand Bráhmans here, From every region, far and near, Well read in holy lore, appear! How many tents, that sages screen, With wains in hundreds, here are seen! Great Bráhman, let us find a place Where we may stay and rest a space.” The hermit did as Ráma prayed, And in a spot his lodging made,[062] Far from the crowd, sequestered, clear, With copious water flowing near.
- **Translation**: 

---

### Verse 18 (Ramayana 0.223)
- **Original**: Canto L. Janak. 205 Then Janak, best of kings, aware Of Vi[vámitra lodging there, With Zatánanda for his guide— The priest on whom he most relied, His chaplain void of guile and stain— And others of his priestly train, Bearing the gift that greets the guest, To meet him with all honour pressed. The saint received with gladsome mind Each honour and observance kind: Then of his health he asked the king, And how his rites were prospering, Janak, with chaplain and with priest, Addressed the hermits, chief and least, Accosting all, in due degree, With proper words of courtesy. Then, with his palms together laid, The king his supplication made: “Deign, reverend lord, to sit thee down With these good saints of high renown.” Then sate the chief of hermits there, Obedient to the monarch's prayer. Chaplain and priest, and king and peer, Sate in their order, far or near. Then thus the king began to say: “The Gods have blest my rite to-day, And with the sight of thee repaid The preparations I have made. Grateful am I, so highly blest, That thou, of saints the holiest, Hast come, O Bráhman, here with all These hermits to the festival. Twelve days, O Bráhman Sage, remain— For so the learned priests ordain—
- **Translation**: 

---

### Verse 19 (Ramayana 0.224)
- **Original**: 206 The Ramayana And then, O heir of Ku[ik's name, The Gods will come their dues to claim.” With looks that testified delight Thus spake he to the anchorite, Then with his suppliant hands upraised, He asked, as earnestly he gazed: “These princely youths, O Sage, who vie In might with children of the sky, Heroic, born for happy fate, With elephants' or lions' gait, Bold as the tiger and the bull, With lotus eyes so large and full, Armed with the quiver, sword and bow, Whose figures like the A[vins show, Like children of the heavenly Powers, Come freely to these shades of ours,— How have they reached on foot this place? What do they seek, and what their race? As sun and moon adorn the sky, This spot the heroes glorify: Alike in stature, port, and mien, The same fair form in each is seen.”219 Thus spoke the monarch, lofty-souled, The saint, of heart unfathomed, told How, sons of Da[aratha, they Accompanied his homeward way, How in the hermitage they dwelt, And slaughter to the demons dealt: Their journey till the spot they neared 219 “The preceding sixteen lines have occurred before in Canto XLVIII. This Homeric custom of repeating a passage of several lines is strange to our poet. This is the only instance I remember. The repetition of single lines is common enough.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 20 (Ramayana 0.225)
- **Original**: Canto LI. Visvámitra. 207 Whence fair Vi[álá's towers appeared: Ahalyá seen and freed from taint; Their meeting with her lord the saint; And how they thither came, to know The virtue of the famous bow. Thus Vi[vámitra spoke the whole To royal Janak, great of soul, And when this wondrous tale was o'er, The glorious hermit said no more. Canto LI. Visvámitra. Wise Vi[vámitra's tale was done: Then sainted Gautam's eldest son, GreatZatánanda, far-renowned, Whom long austerities had crowned With glory— as the news he heard The down upon his body stirred,— Filled full of wonder at the sight Of Ráma, felt supreme delight. When Zatánanda saw the pair Of youthful princes seated there, He turned him to the holy man Who sate at ease, and thus began: “And didst thou, mighty Sage, in truth Show clearly to this royal youth My mother, glorious far and wide, Whom penance-rites have sanctified? And did my glorious mother— she, Heiress of noble destiny—
- **Translation**: 

---



--- End of Ramayan_batch_109.md ---


--- Start of Ramayan_batch_110.md ---

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

### Verse 1 (Ramayana 0.226)
- **Original**: 208 The Ramayana Serve her great guest with woodland store, Whom all should honour evermore? Didst thou the tale to Ráma tell Of what in ancient days befell, The sin, the misery, and the shame Of guilty God and faithless dame? And, O thou best of hermits, say, Did Ráma's healing presence stay Her trial? was the wife restored Again to him, my sire and lord? Say, Hermit, did that sire of mine Receive her with a soul benign, When long austerities in time Had cleansed her from the taint of crime?[063] And, son of Ku[ik, let me know, Did my great-minded father show Honour to Ráma, and regard, Before he journeyed hitherward?” The hermit with attentive ear Marked all the questions of the seer: To him for eloquence far-famed, His eloquent reply he framed: “Yea, 'twas my care no task to shun, And all I had to do was done; As ReGuká and Bhrigu's child, The saint and dame were reconciled.” When the great sage had thus replied, To Ráma Zatánanda cried: “A welcome visit, Prince, is thine, Thou scion of King Raghu's line. With him to guide thy way aright, This sage invincible in might, This Bráhman sage, most glorious-bright,
- **Translation**: 

---

### Verse 2 (Ramayana 0.227)
- **Original**: Canto LI. Visvámitra. 209 By long austerities has wrought A wondrous deed, exceeding thought: Thou knowest well, O strong of arm, This sure defence from scathe and harm. None, Ráma, none is living now In all the earth more blest than thou, That thou hast won a saint so tried In fervid rites thy life to guide. Now listen, Prince, while I relate His lofty deeds and wondrous fate. He was a monarch pious-souled. His foemen in the dust he rolled; Most learned, prompt at duty's claim, His people's good his joy and aim. Of old the Lord of Life gave birth To mighty Ku[a, king of earth. His son was Ku[anábha, strong, Friend of the right, the foe of wrong. Gádhi, whose fame no time shall dim, Heir of his throne was born to him, And Vi[vámitra, Gádhi's heir, Governed the land with kingly care. While years unnumbered rolled away The monarch reigned with equal sway. At length, assembling many a band, He led his warriors round the land— Complete in tale, a mighty force, Cars, elephants, and foot, and horse. Through cities, groves, and floods he passed, O'er lofty hills, through regions vast. He reached Va[ishmha's pure abode, Where trees, and flowers, and creepers glowed, Where troops of sylvan creatures fed;
- **Translation**: 

---

### Verse 3 (Ramayana 0.228)
- **Original**: 210 The Ramayana Which saints and angels visited. Gods, fauns, and bards of heavenly race, And spirits, glorified the place; The deer their timid ways forgot, And holy Bráhmans thronged the spot. Bright in their souls, like fire, were these, Made pure by long austerities, Bound by the rule of vows severe, And each in glory Brahmá's peer. Some fed on water, some on air, Some on the leaves that withered there. Roots and wild fruit were others' food; All rage was checked, each sense subdued, There Bálakhilyas220 went and came, Now breathed the prayer, now fed the flame: These, and ascetic bands beside, The sweet retirement beautified. Such was Va[ishmha's blest retreat, Like Brahmá's own celestial seat, Which gladdened Vi[vámitra's eyes, Peerless for warlike enterprise. Canto LII. Vasishtha's Feast. 220 Divine personages of minute size produced from the hair of Brahmá, and probably the origin of “That small infantry Warred on by cranes.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.229)
- **Original**: Canto LII. Vasishtha's Feast. 211 Right glad was Vi[vámitra when He saw the prince of saintly men. Low at his feet the hero bent, And did obeisance, reverent. The king was welcomed in, and shown A seat beside the hermit's own, Who offered him, when resting there, Fruit in due course, and woodland fare. And Vi[vámitra, noblest king, Received Va[ishmha's welcoming, Turned to his host, and prayed him tell That he and all with him were well. Va [ishmha to the king replied That all was well on every side, That fire, and vows, and pupils throve, And all the trees within the grove. And then the son of Brahmá, best Of all who pray with voice suppressed, Questioned with pleasant words like these The mighty king who sate at ease: “And is it well with thee? I pray; And dost thou win by virtuous sway Thy people's love, discharging all The duties on a king that fall? Are all thy servants fostered well? Do all obey, and none rebel? Hast thou, destroyer of the foe, No enemies to overthrow? Does fortune, conqueror! still attend Thy treasure, host, and every friend? Is it all well? Does happy fate On sons and children's children wait?”
- **Translation**: 

---

### Verse 5 (Ramayana 0.230)
- **Original**: 212 The Ramayana He spoke. The modest king replied That all was prosperous far and wide. [064] Thus for awhile the two conversed, As each to each his tale rehearsed, And as the happy moments flew, Their joy and friendship stronger grew. When such discourse had reached an end, Thus spoke the saint most reverend To royal Vi[vámitra, while His features brightened with a smile: “O mighty lord of men. I fain Would banquet thee and all thy train In mode that suits thy station high: And do not thou my prayer deny. Let my good lord with favour take The offering that I fain would make, And let me honour, ere we part, My royal guest with loving heart.” Him Vi[vámitra thus addressed: “Why make, O Saint, this new request? Thy welcome and each gracious word Sufficient honour have conferred. Thou gavest roots and fruit to eat, The treasures of this pure retreat, And water for my mouth and feet; And — boon I prize above the rest— Thy presence has mine eyesight blest. Honoured by thee in every way, To whom all honour all should pay, I now will go. My lord, Good-bye! Regard me with a friendly eye.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.231)
- **Original**: Canto LIII. Visvámitra's Request. 213 Him speaking thus Va[ishmha stayed, And still to share his banquet prayed. The will of Gádhi's son he bent, And won the monarch to consent, Who spoke in answer.“Let it be, Great Hermit, as it pleases thee.” When, best of those who breathe the prayer, He heard the king his will declare, He called the cow of spotted skin, All spot without, all pure within. “Come, Dapple-skin,” he cried,“with speed; Hear thou my words and help at need. My heart is set to entertain This monarch and his mighty train With sumptuous meal and worthy fare; Be thine the banquet to prepare. Each dainty cate, each goodly dish, Of six-fold taste221 as each may wish— All these, O cow of heavenly power, Rain down for me in copious shower: Viands and drink for tooth and lip, To eat, to suck, to quaff, to sip— Of these sufficient, and to spare, O plenty-giving cow, prepare.” Canto LIII. Visvámitra's Request. 221 Sweet, salt, pungent, bitter, acid, and astringent.
- **Translation**: 

---

### Verse 7 (Ramayana 0.232)
- **Original**: 214 The Ramayana Thus charged, O slayer of thy foes, The cow from whom all plenty flows, Obedient to her saintly lord, Viands to suit each taste, outpoured. Honey she gave, and roasted grain, Mead sweet with flowers, and sugar-cane. Each beverage of flavour rare, An food of every sort, were there: Hills of hot rice, and sweetened cakes, And curdled milk and soup in lakes. Vast beakers foaming to the brim With sugared drink prepared for him, And dainty sweetmeats, deftly made, Before the hermit's guests were laid. So well regaled, so nobly fed, The mighty army banqueted, And all the train, from chief to least, Delighted in Va[ishmha's feast. Then Vi[vámitra, royal sage, Surrounded by his vassalage, Prince, peer, and counsellor, and all From highest lord to lowest thrall, Thus feasted, to Va[ishmha cried With joy, supremely gratified: “Rich honour I, thus entertained, Most honourable lord, have gained: Now hear, before I journey hence, My words, O skilled in eloquence. Bought for a hundred thousand kine, Let Dapple-skin, O Saint, be mine. A wondrous jewel is thy cow, And gems are for the monarch's brow.222 222 “Of old hoards and minerals in the earth, the king is entitled to half by reason of his general protection, and because he is the lord paramount of the
- **Translation**: 

---

### Verse 8 (Ramayana 0.233)
- **Original**: Canto LIII. Visvámitra's Request. 215 To me her rightful lord resign This Dapple-skin thou callest thine.” The great Va[ishmha, thus addressed, Arch-hermit of the holy breast, To Vi[vámitra answer made, The king whom all the land obeyed: “Not for a hundred thousand,— nay, Not if ten million thou wouldst pay, With silver heaps the price to swell,— Will I my cow, O Monarch, sell. Unmeet for her is such a fate. That I my friend should alienate. As glory with the virtuous, she For ever makes her home with me. On her mine offerings which ascend To Gods and spirits all depend: My very life is due to her, My guardian, friend, and minister. [065] The feeding of the sacred flame,223 The dole which living creatures claim.224. The mighty sacrifice by fire, Each formula the rites require,225 And various saving lore beside, Are by her aid, in sooth, supplied. The banquet which thy host has shared, soil.” M ANU {FNS , Book VIII. 39. 223 Ghí or clarified butter,“holy oil,” being one of the essentials of sacrifice. 224 “A Bráhman had five principal duties to discharge every day: study and teaching the Veda, oblations to the manes or spirits of the departed, sacrifice to the Gods, hospitable offerings to men, anda gift of food to all creatures. The last consisted of rice or other grain which the Bráhman was to offer every day outside his house in the open air. MANU {FNS , Book III. 70.” G ORRESIO {FNS 225 These were certain sacred words of invocation such asváhá,vasham, etc., pronounced at the time of sacrifice.
- **Translation**: 

---

### Verse 9 (Ramayana 0.234)
- **Original**: 216 The Ramayana Believe it, was by her prepared, In her mine only treasures lie, She cheers mine heart and charms mine eye. And reasons more could I assign Why Dapple-skin can ne'er be thine.” The royal sage, his suit denied, With eloquence more earnest cried: “Tusked elephants, a goodly train, Each with a golden girth and chain, Whose goads with gold well fashioned shine— Of these be twice seven thousand thine. And four-horse cars with gold made bright, With steeds most beautifully white, Whose bells make music as they go, Eight hundred, Saint, will I bestow. Eleven thousand mettled steeds From famous lands, of noble breeds— These will I gladly give, O thou Devoted to each holy vow. Ten million heifers, fair to view, Whose sides are marked with every hue— These in exchange will I assign; But let thy Dapple-skin be mine. Ask what thou wilt, and piles untold Of priceless gems and gleaming gold, O best of Bráhmans, shall be thine; But let thy Dapple-skin be mine.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.235)
- **Original**: Canto LIV. The Battle. 217 The great Va[ishmha, thus addressed, Made answer to the king's request: “Ne'er will I give my cow away, My gem, my wealth, my life and stay. My worship at the moon's first show, And at the full, to her I owe; And sacrifices small and great, Which largess due and gifts await. From her alone, their root, O King, My rites and holy service spring. What boots it further words to say? I will not give my cow away Who yields me what I ask each day.” Canto LIV. The Battle. As Saint Va[ishmha answered so, Nor let the cow of plenty go, The monarch, as a last resource, Began to drag her off by force. While the king's servants tore away Their moaning, miserable prey, Sad, sick at heart, and sore distressed, She pondered thus within her breast: “Why am I thus forsaken? why Betrayed by him of soul most high. Va [ishmha, ravished by the hands Of soldiers of the monarch's bands? Ah me! what evil have I done Against the lofty-minded one, That he, so pious, can expose
- **Translation**: 

---

### Verse 11 (Ramayana 0.236)
- **Original**: 218 The Ramayana The innocent whose love he knows?” In her sad breast as thus she thought, And heaved deep sighs with anguish fraught, With wondrous speed away she fled, And back to Saint Va[ishmha sped. She hurled by hundreds to the ground The menial crew that hemmed her round, And flying swifter than the blast Before the saint herself she cast. There Dapple-skin before the saint Stood moaning forth her sad complaint, And wept and lowed: such tones as come From wandering cloud or distant drum. “O son of Brahmá,” thus cried she, “Why hast thou thus forsaken me, That the king's men, before thy face, Bear off thy servant from her place?” Then thus the Bráhman saint replied To her whose heart with woe was tried, And grieving for his favourite's sake, As to a suffering sister spake: “I leave thee not: dismiss the thought; Nor, duteous, hast thou failed in aught. This king, o'erweening in the pride Of power, has reft thee from my side. Little, I ween, my strength could do 'Gainst him, a mighty warrior too. Strong, as a soldier born and bred,— Great, as a king whom regions dread. See! what a host the conqueror leads, With elephants, and cars, and steeds. O'er countless bands his pennons fly; So is he mightier far than I.”[066]
- **Translation**: 

---

### Verse 12 (Ramayana 0.237)
- **Original**: Canto LIV. The Battle. 219 He spoke. Then she, in lowly mood, To that high saint her speech renewed: “So judge not they who wisest are: The Bráhman's might is mightier far. For Bráhmans strength from Heaven derive, And warriors bow when Bráhmans strive. A boundless power 'tis thine to wield: To such a king thou shouldst not yield, Who, very mighty though he be,— So fierce thy strength,— must bow to thee. Command me, Saint. Thy power divine Has brought me here and made me thine; And I, howe'er the tyrant boast, Will tame his pride and slay his host.” Then cried the glorious sage:“Create A mighty force the foe to mate.” She lowed, and quickened into life, Pahlavas,226 burning for the strife, King Vi[vámitra's army slew Before the very leader's view. The monarch in excessive ire, His eyes with fury darting fire, Rained every missile on the foe Till all the Pahlavas were low. 226 “It is well known that the Persians were called Pahlavas by the Indians. The Zakasare nomad tribes inhabiting Central Asia, the Scythes of the Greeks, whom the Persians also, as Herodotus tells us, called Sakæ just as the Indians did. Lib. VII 64A¹ ³pÁ sÁÃ±¹ Àq½Ä±Â Ä¿zÂ £{¸±Â.º±»s¿ÅÃ¹ £qº±Â. The name Yavans seems to be used rather indefinitely for nations situated beyond Persia to the west.… After the time of Alexander the Great the Indians as well as the Persians called the Greeks also Yavans.” SCHLEGEL {FNS . Lassen thinks that the Pahlavas were the same people as the qºÄÅµÂ of Herodotus, and that this non-Indian people dwelt on the north-west confines of India.
- **Translation**: 

---

### Verse 13 (Ramayana 0.238)
- **Original**: 220 The Ramayana She, seeing all her champions slain, Lying by thousands on the plain. Created, by her mere desire, Yavans andZakas, fierce and dire. And all the ground was overspread With Yavans and withZakas dread: A host of warriors bright and strong, And numberless in closest throng: The threads within the lotus stem, So densely packed, might equal them. In gold-hued mail 'against war's attacks, Each bore a sword and battle-axe, The royal host, where'er these came, Fell as if burnt with ravening flame. The monarch, famous through the world Again his fearful weapons hurled, That made Kámbojas,227 Barbars,228 all, With Yavans, troubled, flee and fall. Canto LV. The Hermitage Burnt. So o'er the field that host lay strown, By Vi[vámitra's darts o'erthrown. Then thus Va[ishmha charged the cow: “Create with all thy vigour now.” 227 See page 13, note 6. 228 Barbarians, non-Sanskrit-speaking tribes.
- **Translation**: 

---

### Verse 14 (Ramayana 0.239)
- **Original**: Canto LV. The Hermitage Burnt. 221 Forth sprang Kámbojas, as she lowed; Bright as the sun their faces glowed, Forth from her udder Barbars poured,— Soldiers who brandished spear and sword,— And Yavans with their shafts and darts, And Zakas from her hinder parts. And every pore upon her fell, And every hair-producing cell, With Mlechchhas229 and Kirátas230 teemed, And forth with them Hárítas streamed. And Vi[vámitra's mighty force, Car, elephant, and foot, and horse, Fell in a moment's time, subdued By that tremendous multitude. The monarch's hundred sons, whose eyes Beheld the rout in wild surprise, Armed with all weapons, mad with rage, Rushed fiercely on the holy sage. One cry he raised, one glance he shot, And all fell scorched upon the spot: Burnt by the sage to ashes, they With horse, and foot, and chariot, lay. The monarch mourned, with shame and pain, His army lost, his children slain, Like Ocean when his roar is hushed, Or some great snake whose fangs are crushed: [067] 229 A comprehensive term for foreign or outcast races of different faith and language from the Hindus. 230 The Kirátas and Hárítas are savage aborigines of India who occupy hills and jungles and are altogether different in race and character from the Hindus. Dr. Muir remarks in his Sanskrit Texts, Vol. I. p. 488 (second edition) that it does not appear that it is the object of this legend to represent this miraculous creation as the origin of these tribes, and that nothing more may have been intended than that the cow called into existence large armies, of the same stock with particular tribes previously existing.
- **Translation**: 

---

### Verse 15 (Ramayana 0.240)
- **Original**: 222 The Ramayana Or as in swift eclipse the Sun Dark with the doom he cannot shun: Or a poor bird with mangled wing— So, reft of sons and host, the king No longer, by ambition fired, The pride of war his breast inspired. He gave his empire to his son— Of all he had, the only one: And bade him rule as kings are taught Then straight a hermit-grove he sought. Far to Himálaya's side he fled, Which bards and Nágas visited, And, Mahádeva's231 grace to earn, He gave his life to penance stern. A lengthened season thus passed by, When Ziva's self, the Lord most High, Whose banner shows the pictured bull,232 Appeared, the God most bountiful: “Why fervent thus in toil and pain? What brings thee here? what boon to gain? Thy heart's desire, O Monarch, speak: I grant the boons which mortals seek.” The king, his adoration paid, To Mahádeva answer made: “If thou hast deemed me fit to win Thy favour, O thou void of sin, On me, O mighty God, bestow The wondrous science of the bow, All mine, complete in every part, With secret spell and mystic art. To me be all the arms revealed 231 The Great God,Ziva. 232 Nandi, the snow-white bull, the attendant and favourite vehicle ofZiva.
- **Translation**: 

---

### Verse 16 (Ramayana 0.241)
- **Original**: Canto LV. The Hermitage Burnt. 223 That Gods, and saints, and Titans wield, And every dart that arms the hands Of spirits, fiends and minstrel bands, Be mine, O Lord supreme in place, This token of thy boundless grace.” The Lord of Gods then gave consent, And to his heavenly mansion went. Triumphant in the arms he held, The monarch's breast with glory swelled. So swells the ocean, when upon His breast the full moon's beams have shone. Already in his mind he viewed Va [ishmha at his feet subdued. He sought that hermit's grove, and there Launched his dire weapons through the air, Till scorched by might that none could stay The hermitage in ashes lay. Where'er the inmates saw, aghast, The dart that Vi[vámitra cast, To every side they turned and fled In hundreds forth disquieted. Va [ishmha's pupils caught the fear, And every bird and every deer, And fled in wild confusion forth Eastward and westward, south and north, And so Va[ishmha's holy shade A solitary wild was made, Silent awhile, for not a sound Disturbed the hush that was around.
- **Translation**: 

---

### Verse 17 (Ramayana 0.242)
- **Original**: 224 The Ramayana Va [ishmha then, with eager cry, Called,“Fear not, friends, nor seek to fly. This son of Gádhi dies to-day, Like hoar-frost in the morning's ray.” Thus having said, the glorious sage Spoke to the king in words of rage: “Because thou hast destroyed this grove Which long in holy quiet throve, By folly urged to senseless crime, Now shalt thou die before thy time.” Canto LVI. Visvámitra's Vow. But Vi[vámitra, at the threat Of that illustrious anchoret, Cried, as he launched with ready hand A fiery weapon,“Stand, O Stand!” Va [ishmha, wild with rage and hate, Raising, as 'twere the Rod of Fate, His mighty Bráhman wand on high, To Vi[vámitra made reply: “Nay, stand, O Warrior thou, and show What soldier can, 'gainst Bráhman foe. O Gádhi's son, thy days are told; Thy pride is tamed, thy dart is cold. How shall a warrior's puissance dare With Bráhman's awful strength compare? To-day, base Warrior, shall thou feel That God-sent might is more than steel.” He raised his Bráhman staff, nor missed The fiery dart that near him hissed:
- **Translation**: 

---

### Verse 18 (Ramayana 0.243)
- **Original**: Canto LVI. Visvámitra's Vow. 225 And quenched the fearful weapon fell, As flame beneath the billow's swell. Then Gádhi's son in fury threw Lord VaruG's arm and Rudra's too: Indra's fierce bolt that all destroys; That which the Lord of Herds employs: The Human, that which minstrels keep, The deadly Lure, the endless Sleep: The Yawner, and the dart which charms; Lament and Torture, fearful arms: The Terrible, the dart which dries, The Thunderbolt which quenchless flies, And Fate's dread net, and Brahmá's noose, And that which waits for VaruG's use: The dart he loves who wields the bow Pináka, and twin bolts that glow With fury as they flash and fly, The quenchless Liquid and the Dry: The dart of Vengeance, swift to kill: The Goblins' dart, the Curlew's Bill: [068] The discus both of Fate and Right, And VishGu's, of unerring flight: The Wind-God's dart, the Troubler dread, The weapon named the Horse's Head. From his fierce hand two spears were thrown, And the great mace that smashes bone; The dart of spirits of the air, And that which Fate exults to bear: The Trident dart which slaughters foes, And that which hanging skulls compose:233 233 “The names of many of these weapons which are mythical and partly alle- gorical have occurred in Canto XXIX. The general signification of the story is clear enough. It is a contest for supremacy between the regal or military order
- **Translation**: 

---

### Verse 19 (Ramayana 0.244)
- **Original**: 226 The Ramayana These fearful darts in fiery rain He hurled upon the saint amain, An awful miracle to view. But as the ceaseless tempest flew, The sage with wand of God-sent power Still swallowed up that fiery shower. Then Gádhi's son, when these had failed, With Brahmá's dart his foe assailed. The Gods, with Indra at their head, And Nágas, quailed disquieted, And saints and minstrels, when they saw The king that awful weapon draw; And the three worlds were filled with dread, And trembled as the missile sped. The saint, with Bráhman wand, empowered By lore divine that dart devoured. Nor could the triple world withdraw Rapt gazes from that sight of awe; For as he swallowed down the dart Of Brahmá, sparks from every part, From finest pore and hair-cell, broke Enveloped in a veil of smoke. The staff he waved was all aglow Like Yáma's sceptre, King below, Or like the lurid fire of Fate Whose rage the worlds will desolate. and Bráhmanical or priestly authority, like one of those struggles which our own Europe saw in the middle ages when without employing warlike weapons the priesthood frequently gained the victory.” SCHLEGEL {FNS . For a full account of the early contests between the Bráhmans and the Kshattriyas, see Muir's Original Sanskrit Texts (Second edition) Vol. I. Ch. IV.
- **Translation**: 

---

### Verse 20 (Ramayana 0.245)
- **Original**: Canto LVII. Trisanku. 227 The hermits, whom that sight had awed, Extolled the saint, with hymn and laud: “Thy power, O Sage, is ne'er in vain: Now with thy might thy might restrain. Be gracious, Master, and allow The worlds to rest from trouble now; For Vi[vámitra, strong and dread, By thee has been discomfited.” Then, thus addressed, the saint, well pleased, The fury of his wrath appeased. The king, o'erpowered and ashamed, With many a deep-drawn sigh exclaimed: “Ah! Warriors' strength is poor and slight; A Bráhman's power is truly might. This Bráhman staff the hermit held The fury of my darts has quelled. This truth within my heart impressed, With senses ruled and tranquil breast My task austere will I begin, And Bráhmanhood will strive to win.” Canto LVII. Trisanku. Then with his heart consumed with woe, Still brooding on his overthrow By the great saint he had defied, At every breath the monarch sighed. Forth from his home his queen he led, And to a land far southward fled. There, fruit and roots his only food,
- **Translation**: 

---



--- End of Ramayan_batch_110.md ---


--- Start of Ramayan_batch_111.md ---

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

### Verse 1 (Ramayana 0.246)
- **Original**: 228 The Ramayana He practised penance, sense-subdued, And in that solitary spot Four virtuous sons the king begot: Havishyand, from the offering named, And Madhushyand, for sweetness famed, Mahárath, chariot-borne in fight, And Dri hanetra strong of sight. A thousand years had passed away, When Brahmá, Sire whom all obey, Addressed in pleasant words like these Him rich in long austerities: “Thou by the penance, Ku[ik's son, A place 'mid royal saints hast won. Pleased with thy constant penance, we This lofty rank assign to thee.” Thus spoke the glorious Lord most High Father of earth and air and sky, And with the Gods around him spread Home to his changeless sphere he sped. But Vi[vámitra scorned the grace, And bent in shame his angry face. Burning with rage, o'erwhelmed with grief, Thus in his heart exclaimed the chief: “No fruit, I ween, have I secured By strictest penance long endured, If Gods and all the saints decree To make but royal saint of me.” Thus pondering, he with sense subdued, With sternest zeal his vows renewed.[069]
- **Translation**: 

---

### Verse 2 (Ramayana 0.247)
- **Original**: Canto LVII. Trisanku. 229 Then reigned a monarch, true of soul, Who kept each sense in firm control; Of old Ikshváku's line he came, That glories in Tri[anku's234 name. Within his breast, O Raghu's child, Arose a longing, strong and wild, Great offerings to the Gods to pay, And win, alive, to heaven his way. His priest Va[ishmha's aid he sought, And told him of his secret thought. But wise Va[ishmha showed the hope Was far beyond the monarch's scope. Tri[anku then, his suit denied, Far to the southern region hied, To beg Va[ishmha's sons to aid The mighty plan his soul had made. There King Tri[anku, far renowned, Va [ishmha's hundred children found, Each on his fervent vows intent, For mind and fame preëminent. To these the famous king applied, Wise children of his holy guide. Saluting each in order due. His eyes, for shame, he downward threw, And reverent hands together pressed, The glorious company addressed: “I as a humble suppliant seek Succour of you who aid the weak. A mighty offering I would pay, 234 “Tri[anku, king of Ayodhyá, was seventh in descent from Ikshváku, and Da [aratha holds the thirty-fourth place in the same genealogy. See Canto LXX. We are thrown back, therefore, to very ancient times, and it occasions some surprise to find Va[ishmha and Vi[vámitra, actors in these occurences, still alive in Rama's time.”
- **Translation**: 

---

### Verse 3 (Ramayana 0.248)
- **Original**: 230 The Ramayana But sage Va[ishmha answered, Nay. Be yours permission to accord, And to my rites your help afford. Sons of my guide, to each of you With lowly reverence here I sue; To each, intent on penance-vow, O Bráhmans, low my head I bow, And pray you each with ready heart In my great rite to bear a part, That in the body I may rise And dwell with Gods within the skies. Sons of my guide, none else I see Can give what he refuses me. Ikshváku's children still depend Upon their guide most reverend; And you, as nearest in degree To him, my deities shall be!” Canto LVIII. Trisanku Cursed. Tri[anku's speech the hundred heard, And thus replied, to anger stirred: “Why foolish King, by him denied, Whose truthful lips have never lied, Dost thou transgress his prudent rule, And seek, for aid, another school?235 235 “It does not appear how Tri[anku, in asking the aid of Va[ishmha's sons after applying in vain to their father, could be charged with resorting to another [ákhá (School) in the ordinary sense of that word; as it is not conceivable that the sons should have been of anotherZákhá from the father, whose cause they espouse with so much warmth. The commentator in the Bombay edition
- **Translation**: 

---

### Verse 4 (Ramayana 0.249)
- **Original**: Canto LVIII. Trisanku Cursed. 231 Ikshváku's sons have aye relied Most surely on their holy guide: Then how dost thou, fond Monarch, dare Transgress the rule his lips declare? “Thy wish is vain,” the saint replied, And bade thee cast the plan aside. Then how can we, his sons, pretend In such a rite our aid to lend? O Monarch, of the childish heart, Home to thy royal town depart. That mighty saint, thy priest and guide, At noblest rites may well preside: The worlds for sacrifice combined A worthier priest could never find.” Such speech of theirs the monarch heard, Though rage distorted every word, And to the hermits made reply: “You, like your sire, my suit deny. For other aid I turn from you: So, rich in penance, Saints, adieu!” Va [ishmha's children heard, and guessed His evil purpose scarce expressed, And cried, while rage their bosoms burned, “Be to a vile ChaG ála236 turned!” [070] This said, with lofty thoughts inspired, Each to his own retreat retired. explains the wordZákhantaram as Yájanádiná rakshántaram,‘one who by sacrificing for thee, etc., will be another protector.’ Gorresio's Gau a text, which may often be used as a commentary on the older one, has the following paraphrase of the words in question, ch. 60, 3. Múlam uts[ijya kasmát tvam sákhásv ichhasi lambitum.‘Why, forsaking the root, dost thou desire to hang upon the branches?’ ”M UIR {FNS , Sanskrit Texts, Vol. I., p. 401. 236 A ChaG ála was a man born of the illegal and impure union of aZúdra with a woman of one of the three higher castes.
- **Translation**: 

---

### Verse 5 (Ramayana 0.250)
- **Original**: 232 The Ramayana That night Tri[anku underwent Sad change in shape and lineament. Next morn, an outcast swart of hue, His dusky cloth he round him drew. His hair had fallen from his head, And roughness o'er his skin was spread. Such wreaths adorned him as are found To flourish on the funeral ground. Each armlet was an iron ring: Such was the figure of the king, That every counsellor and peer, And following townsman, fled in fear. Alone, unyielding to dismay, Though burnt by anguish night and day, Great Vi[vámitra's side he sought, Whose treasures were by penance bought. The hermit with his tender eyes Looked on Tri[anku's altered guise, And grieving at his ruined state Addressed him thus, compassionate: “Great King,” the pious hermit said, “What cause thy steps has hither led, Ayodhyá's mighty Sovereign, whom A curse has plagued with outcast's doom?” In vile ChaG ála237 shape, the king Heard Vi[vámitra's questioning, And, suppliant palm to palm applied, With answering eloquence he cried: 237 “The ChaG ála was regarded as the vilest and most abject of the men sprung from wedlock forbidden by the law (Mánavadharma[ástra, Lib. X. 12.); a kind of social malediction weighed upon his head and rejected him from human society.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 6 (Ramayana 0.251)
- **Original**: Canto LVIII. Trisanku Cursed. 233 “My priest and all his sons refused To aid the plan on which I mused. Failing to win the boon I sought, To this condition I was brought. I, in the body, Saint, would fain A mansion in the skies obtain. I planned a hundred rites for this, But still was doomed the fruit to miss. Pure are my lips from falsehood's stain, And pure they ever shall remain,— Yea, by a Warrior's faith I swear,— Though I be tried with grief and care. Unnumbered rites to Heaven I paid, With righteous care the sceptre swayed; And holy priest and high-souled guide My modest conduct gratified. But, O thou best of hermits, they Oppose my wish these rites to pay; They one and all refuse consent, Nor aid me in my high intent. Fate is, I ween, the power supreme, Man's effort but an idle dream, Fate whirls our plans, our all away; Fate is our only hope and stay; Now deign, O blessed Saint, to aid Me, even me by Fate betrayed, Who come, a suppliant, sore distressed, One grace, O Hermit, to request. No other hope or way I see: No other refuge waits for me. Oh, aid me in my fallen state, And human will shall conquer Fate.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.252)
- **Original**: 234 The Ramayana Canto LIX. The Sons Of Vasishtha. Then Ku[ik's son, by pity warmed, Spoke sweetly to the king transformed: “Hail! glory of Ikshváku's line: I know how bright thy virtues shine. Dismiss thy fear, O noblest Chief, For I myself will bring relief. The holiest saints will I invite To celebrate thy purposed rite: So shall thy vow, O King, succeed, And from thy cares shalt thou be freed. Thou in the form which now thou hast, Transfigured by the curse they cast,— Yea, in the body, King, shalt flee, Transported, where thou fain wouldst be. O Lord of men, I ween that thou Hast heaven within thy hand e'en now, For very wisely hast thou done, And refuge sought with Ku[ik's son.” Thus having said, the sage addressed His sons, of men the holiest, And bade the prudent saints whate'er Was needed for the rite prepare. The pupils he was wont to teach He summoned next, and spoke this speech: “Go bid Va[ishmha'a sons appear, And all the saints be gathered here. And what they one and all reply When summoned by this mandate high, To me with faithful care report, Omit no word and none distort.”
- **Translation**: 

---

### Verse 8 (Ramayana 0.253)
- **Original**: Canto LIX. The Sons Of Vasishtha. 235 The pupils heard, and prompt obeyed, To every side their way they made. Then swift from every quarter sped The sages in the Vedas read. Back to that saint the envoys came, Whose glory shone like burning flame, And told him in their faithful speech The answer that they bore from each: “Submissive to thy word, O Seer, The holy men are gathering here. By all was meet obedience shown: Mahodaya 238 refused alone. [071] And now, O Chief of hermits, hear What answer, chilling us with fear, Va [ishmha's hundred sons returned, Thick-speaking as with rage they burned: “How will the Gods and saints partake The offerings that the prince would make, And he a vile and outcast thing, His ministrant one born a king? Can we, great Bráhmans, eat his food, And think to win beatitude, By Vi[vámitra purified?” Thus sire and sons in scorn replied, And as these bitter words they said, Wild fury made their eyeballs red. Their answer when the arch-hermit heard, His tranquil eyes with rage were blurred; Great fury in his bosom woke, And thus unto the youths he spoke: “Me, blameless me they dare to blame, 238 This appellation, occuring nowhere else in the poem except as the name of a city, appears twice in this Canto as a name of Va[ishmha.
- **Translation**: 

---

### Verse 9 (Ramayana 0.254)
- **Original**: 236 The Ramayana And disallow the righteous claim My fierce austerities have earned: To ashes be the sinners turned. Caught in the noose of Fate shall they To Yáma's kingdom sink to-day. Seven hundred times shall they be born To wear the clothes the dead have worn. Dregs of the dregs, too vile to hate, The flesh of dogs their maws shall sate. In hideous form, in loathsome weed, A sad existence each shall lead. Mahodaya too, the fool who fain My stainless life would try to stain, Stained in the world with long disgrace Shall sink into a fowler's place. Rejoicing guiltless blood to spill, No pity through his breast shall thrill. Cursed by my wrath for many a day, His wretched life for sin shall pay.” Thus, girt with hermit, saint, and priest, Great Vi[vámitra spoke— and ceased. Canto LX. Trisanku's Ascension.
- **Translation**: 

---

### Verse 10 (Ramayana 0.255)
- **Original**: Canto LX. Trisanku's Ascension. 237 So with ascetic might, in ire, He smote the children and the sire. Then Vi[vámitra, far-renowned, Addressed the saints who gathered round: “See by my side Tri[anku stand, Ikshváku's son, of liberal hand. Most virtuous and gentle, he Seeks refuge in his woe with me. Now, holy men, with me unite, And order so his purposed rite That in the body he may rise And win a mansion in the skies.” They heard his speech with ready ear And, every bosom filled with fear Of Vi[vámitra, wise and great, Spoke each to each in brief debate: “The breast of Ku[ik's son, we know, With furious wrath is quick to glow. Whate'er the words he wills to say, We must, be very sure, obey. Fierce is our lord as fire, and straight May curse us all infuriate. So let us in these rites engage, As ordered by the holy sage. And with our best endeavour strive That King Ikshváku's son, alive, In body to the skies may go By his great might who wills it so.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.256)
- **Original**: 238 The Ramayana Then was the rite begun with care: All requisites and means were there: And glorious Vi[vámitra lent His willing aid as president. And all the sacred rites were done By rule and use, omitting none. By chaplain-priest, the hymns who knew, In decent form and order due. Some time in sacrifice had past, And Vi[vámitra made, at last, The solemn offering with the prayer That all the Gods might come and share. But the Immortals, one and all, Refused to hear the hermit's call. Then red with rage his eyeballs blazed: The sacred ladle high he raised, And cried to King Ikshváku's son: “Behold my power, by penance won: Now by the might my merits lend, Ikshváku's child, to heaven ascend. In living frame the skies attain, Which mortals thus can scarcely gain. My vows austere, so long endured, Have, as I ween, some fruit assured. Upon its virtue, King, rely, And in thy body reach the sky.” His speech had scarcely reached its close, When, as he stood, the sovereign rose, And mounted swiftly to the skies Before the wondering hermits' eyes.
- **Translation**: 

---

### Verse 12 (Ramayana 0.257)
- **Original**: Canto LX. Trisanku's Ascension. 239 But Indra, when he saw the king His blissful regions entering, With all the army of the Blest Thus cried unto the unbidden guest: “With thy best speed, Tri[anku, flee: Here is no home prepared for thee. By thy great master's curse brought low, Go, falling headlong, earthward go.” Thus by the Lord of Gods addressed, Tri[anku fell from fancied rest, And screaming in his swift descent, “O, save me, Hermit!” down he went. And Vi[vámitra heard his cry, And marked him falling from the sky, And giving all his passion sway, Cried out in fury,“Stay, O stay!” [072] By penance-power and holy lore, Like Him who framed the worlds of yore, Seven other saints he fixed on high To star with light the southern sky. Girt with his sages forth he went, And southward in the firmament New wreathed stars prepared to set In many a sparkling coronet. He threatened, blind with rage and hate, Another Indra to create, Or, from his throne the ruler hurled, All Indraless to leave the world. Yea, borne away by passion's storm, The sage began new Gods to form. But then each Titan, God, and saint, Confused with terror, sick and faint, To high souled Vi[vámitra hied,
- **Translation**: 

---

### Verse 13 (Ramayana 0.258)
- **Original**: 240 The Ramayana And with soft words to soothe him tried: “Lord of high destiny, this king, To whom his master's curses cling, No heavenly home deserves to gain, Unpurified from curse and stain.” The son of Ku[ik, undeterred, The pleading of the Immortals heard, And thus in haughty words expressed The changeless purpose of his breast: “Content ye, Gods: I soothly sware Tri[anku to the skies to bear Clothed in his body, nor can I My promise cancel or deny. Embodied let the king ascend To life in heaven that ne'er shall end. And let these new-made stars of mine Firm and secure for ever shine. Let these, my work, remain secure Long as the earth and heaven endure. This, all ye Gods, I crave: do you Allow the boon for which I sue.” Then all the Gods their answer made: “So be it, Saint, as thou hast prayed. Beyond the sun's diurnal way Thy countless stars in heaven shall stay: And 'mid them hung, as one divine, Head downward shall Tri[anku shine; And all thy stars shall ever fling Their rays attendant on the king.”239 239 “The seven ancient rishis or saints, as has been said before, were the seven stars of Ursa Major. The seven other new saints which are here said to have been created by Vi[vámitra should be seven new southern stars, a sort of new Ursa. Von Schlegel thinks that this mythical fiction of new stars created by
- **Translation**: 

---

### Verse 14 (Ramayana 0.259)
- **Original**: Canto LXI. Sunahsepha. 241 The mighty saint, with glory crowned, With all the sages compassed round, Praised by the Gods, gave full assent, And Gods and sages homeward went. Canto LXI. Sunahsepha. Then Vi[vámitra, when the Blest Had sought their homes of heavenly rest, Thus, mighty Prince, his counsel laid Before the dwellers of the shade: “The southern land where now we are Offers this check our rites to bar:240 To other regions let us speed, And ply our tasks from trouble freed. Now turn we to the distant west. To Pushkar's241 wood where hermits rest, Vi[vámitra may signify that these southern stars, unknown to the Indians as long as they remained in the neighbourhood of the Ganges, became known to them at a later date when they colonized the southern regions of India.” G ORRESIO {FNS . 240 “This cannot refer to the events just related: for Vi[vámitra was successful in the sacrifice performed for Tri[anku. And yet no other impediment is mentioned. Still his restless mind would not allow him to remain longer in the same spot. So the character of Vi[vámitra is ingeniously and skilfully shadowed forth: as he had been formerly a most warlike king, loving battle and glory, bold, active, sometimes unjust, and more frequently magnanimous, such also he always shows himself in his character of anchorite and ascetic.” SCHLEGEL {FNS . 241 Near the modern city of Ajmere. The place is sacred still, and the name is preserved in the Hindí. Lassen, however, says that this Pushkala or Pushkara, called by the Grecian writers µÅºµ»wÄ¹Â, the earliest place of pilgrimage mentioned by name, is not to be confounded with the modern Pushkara in Ajmere.
- **Translation**: 

---

### Verse 15 (Ramayana 0.260)
- **Original**: 242 The Ramayana And there to rites austere apply, For not a grove with that can vie.” The saint, in glory's light arrayed, In Pushkar's wood his dwelling made, And living there on roots and fruit Did penance stern and resolute. The king who filled Ayodhyá's throne, By Ambarísha's name far known, At that same time, it chanced, began A sacrificial rite to plan. But Indra took by force away The charger that the king would slay. The victim lost, the Bráhman sped To Ambarísha's side, and said: “Gone is the steed, O King, and this Is due to thee, in care remiss.[073] Such heedless faults will kings destroy Who fail to guard what they enjoy. The flaw is desperate: we need The charger, or a man to bleed. Quick! bring a man if not the horse, That so the rite may have its course.”
- **Translation**: 

---

### Verse 16 (Ramayana 0.261)
- **Original**: Canto LXI. Sunahsepha. 243 The glory of Ikshváku's line Made offer of a thousand kine, And sought to buy at lordly price A victim for the sacrifice. To many a distant land he drove, To many a people, town, and grove, And holy shades where hermits rest, Pursuing still his eager quest. At length on Bhrigu's sacred height The saint Richíka met his sight Sitting beneath the holy boughs. His children near him, and his spouse. The mighty lord drew near, assayed To win his grace, and reverence paid; And then the sainted king addressed The Bráhman saint with this request: “Bought with a hundred thousand kine, Give me, O Sage, a son of thine To be a victim in the rite, And thanks the favour shall requite. For I have roamed all countries round, Nor sacrificial victim found. Then, gentle Hermit, deign to spare One child amid the number there.” Then to the monarch's speech replied The hermit, penance-glorified: “For countless kine, for hills of gold, Mine eldest son shall ne'er be sold.” But, when she heard the saint's reply, The children's mother, standing nigh, Words such as these in answer said To Ambarísha, monarch dread:
- **Translation**: 

---

### Verse 17 (Ramayana 0.262)
- **Original**: 244 The Ramayana “My lord, the saint, has spoken well: His eldest child he will not sell. And know, great Monarch, that above The rest my youngest born I love. 'Tis ever thus: the father's joy Is centred in his eldest boy. The mother loves her darling best Whom last she rocked upon her breast: My youngest I will ne'er forsake.” As thus the sire and mother spake, Young Zunah[epha, of the three The midmost, cried unurged and free: “My sire withholds his eldest son, My mother keeps her youngest one: Then take me with thee, King: I ween The son is sold who comes between.” The king with joy his home resought, And took the prize his kine had bought. He bade the youth his car ascend, And hastened back the rites to end.242 So the ram caught in the thicket took the place of Isaac, or, as the Musalmáns say, of Ishmael. 242 “Ambarísha is the twenty-ninth in descent from Ikshváku, and is there- fore separated by an immense space of time from Tri[anku in whose story Vi[vámitra had played so important a part. Yet Richíka, who is represented as having young sons while Ambarísha was yet reigning being himself the son of Bhrigu and to be numbered with the most ancient sages, is said to have married the younger sister of Vi[vámitra. But I need not again remark that there is a perpetual anachronism in Indian mythology.” SCHLEGEL .{FNS . “In the mythical story related in this and the following Canto we may discover, I think, some indication of the epoch at which the immolation of lower animals was substituted for human sacrifice.… So when Iphigenia was about to be sacrificed at Aulis, one legend tells us that a hind was substituted for the virgin.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 18 (Ramayana 0.263)
- **Original**: Canto LXII. Ambarísha's Sacrifice. 245 Canto LXII. Ambarísha's Sacrifice. As thus the king that youth conveyed, His weary steeds at length he stayed At height of noon their rest to take Upon the bank of Pushkar's lake. There while the king enjoyed repose The captiveZunah[epha rose, And hasting to the water's side His uncle Vi[vámitra spied, With many a hermit 'neath the trees Engaged in stern austerities. Distracted with the toil and thirst, With woeful mien, away he burst, Swift to the hermit's breast he flew, And weeping thus began to sue: “No sire have I, no mother dear, No kith or kin my heart to cheer: As justice bids, O Hermit, deign To save me from the threatened pain. O thou to whom the wretched flee, And find a saviour, Saint, in thee, Now let the king obtain his will, And me my length of days fulfil, That rites austere I too may share, May rise to heaven and rest me there. With tender soul and gentle brow Be guardian of the orphan thou, And as a father pities, so Preserve me from my fear and woe.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.264)
- **Original**: 246 The Ramayana When Vi [vámitra, glorious saint, Had heard the boy's heart-rending plaint. He soothed his grief, his tears he dried, [074] Then called his sons to him, and cried: “The time is come for you to show The duty and the aid bestow For which, regarding future life, A man gives children to his wife. This hermit's son, whom here you see A suppliant, refuge seeks with me. O sons, the friendless youth befriend, And, pleasing me, his life defend. For holy works you all have wrought, True to the virtuous life I taught. Go, and as victims doomed to bleed, Die, and Lord Agni's hunger feed. So shall the rite completed end, This orphan gain a saving friend, Due offerings to the Gods be paid, And your own father's voice obeyed.” Then Madhushyand and all the rest Answered their sire with scorn and jest: “What! aid to others' sons afford, And leave thine own to die, my lord! To us it seems a horrid deed, As 'twere on one's own flesh to feed.” The hermit heard his sons' reply, And burning rage inflamed his eye. Then forth his words of fury burst: “Audacious speech, by virtue cursed! It lifts on end each shuddering hair— My charge to scorn! my wrath to dare!
- **Translation**: 

---

### Verse 20 (Ramayana 0.265)
- **Original**: Canto LXII. Ambarísha's Sacrifice. 247 You, like Va[ishmha's evil brood, Shall make the flesh of dogs your food A thousand years in many a birth, And punished thus shall dwell on earth.” Thus on his sons his curse he laid. Then calmed again that youth dismayed, And blessed him with his saving aid: “When in the sacred fetters bound, And with a purple garland crowned, At VishGu's post thou standest tied, With lauds be Agni glorified. And these two hymns of holy praise Forget not, Hermit's son, to raise In the king's rite, and thou shalt be Lord of thy wish, preserved, and free.” He learnt the hymns with mind intent, And from the hermit's presence went. To Ambarísha thus he spake: “Let us our onward journey take. Haste to thy home, O King, nor stay The lustral rites with slow delay.” The boy's address the monarch cheered, And soon the sacred ground he neared. The convocation's high decree Declared the youth from blemish free; Clothed in red raiment he was tied A victim at the pillar's side. There bound, the Fire-God's hymn he raised, And Indra and Upendra praised. Thousand-eyed VishGu, pleased to hear The mystic laud, inclined his ear, And won by worship, swift to save,
- **Translation**: 

---



--- End of Ramayan_batch_111.md ---


--- Start of Ramayan_batch_112.md ---

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

### Verse 1 (Ramayana 0.266)
- **Original**: 248 The Ramayana Long life toZunah[epha gave. The king in bounteous measure gained The fruit of sacrifice ordained, By grace of Him who rules the skies, Lord Indra of the thousand eyes. And Vi[vámitra evermore. Pursued his task on Pushkar's shore Until a thousand years had past In fierce austerity and fast. Canto LXIII. Menaká. A thousand years had thus flown by When all the Gods within the sky, Eager that he the fruit might gain Of fervent rite and holy pain, Approached the great ascetic, now Bathed after toil and ended vow. Then Brahmá speaking for the rest With sweetest words the sage addressed: “Hail, Saint! This high and holy name Thy rites have won, thy merits claim.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.267)
- **Original**: Canto LXIII. Menaká. 249 Thus spoke the Lord whom Gods revere, And sought again his heavenly sphere. But Vi[vámitra, more intent, His mind to sterner penance bent. So many a season rolled away, When Menaká, fair nymph, one day Came down from Paradise to lave Her perfect limbs in Pushkar's wave, The glorious son of Ku[ik saw That peerless shape without a flaw Flash through the flood's translucent shroud Like lightning gleaming through a cloud. He saw her in that lone retreat, Most beautiful from head to feet, And by Kandarpa's243 might subdued He thus addressed her as he viewed: “Welcome, sweet nymph! O deign, I pray, In these calm shades awhile to stay. To me some gracious favour show, For love has set my breast aglow.” He spoke. The fairest of the fair Made for awhile her dwelling there, While day by day the wild delight Stayed vow austere and fervent rite There as the winsome charmer wove Her spells around him in the grove, And bound him in a golden chain, Five sweet years fled, and five again. Then Vi[vámitra woke to shame, And, fraught with anguish, memory came For quick he knew, with anger fired, That all the Immortals had conspired [075] 243 The Indian Cupid.
- **Translation**: 

---

### Verse 3 (Ramayana 0.268)
- **Original**: 250 The Ramayana To lap his careless soul in ease, And mar his long austerities. “Ten years have past, each day and night Unheeded in delusive flight. So long my fervent rites were stayed, While thus I lay by love betrayed.” As thus long sighs the hermit heaved, And, touched with deep repentance, grieved, He saw the fair one standing nigh With suppliant hands and trembling eye. With gentle words he bade her go, Then sought the northern hills of snow. With firm resolve he vowed to beat The might of love beneath his feet. Still northward to the distant side Of Kau[ikí244, the hermit hide, And gave his life to penance there With rites austere most hard to bear. A thousand years went by, and still He laboured on the northern hill With pains so terrible and drear That all the Gods were chilled with fear, 244 “The same as she whose praises Vi[vámitra has already sung in Canto XXXV, and whom the poet brings yet alive upon the scene in Canto LXI. Her proper name wasSatyavatí(Truthful); the patronymic, Kau[ikí was preserved by the river into which she is said to have been changed, and is still recognized in the corrupted forms Ku[a and Ku[í. The river flows from the heights of the Himálaya towards the Ganges, bounding on the east the country of Videha (Behar). The name is no doubt half hidden in theCosoagus of Pliny and the Kossounos of Arrian. But each author has fallen into the same error in his enumeration of these rivers (Condochatem, Erannoboam, Cosoagum, Sonum). The Erannoboas, (HiraGyaváha) and the Sone are not different streams, but well-known names of the same river. Moreover the order is disturbed, in which on the right and left they fall into the Ganges. To be consistent with geogra- phy it should be written: Erannoboam sive Sonum, Condochatem (Gandakí), Cosoagum.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 4 (Ramayana 0.269)
- **Original**: Canto LXIII. Menaká. 251 And Gods and saints, for swift advice, Met in the halls of Paradise. “Let Ku[ik's son,” they counselled,“be A Mighty saint by just decree.” His ear to hear their counsel lent The Sire of worlds, omnipotent. To him enriched by rites severe He spoke in accents sweet to hear: “Hail, Mighty Saint! dear son, all hail! Thy fervour wins, thy toils prevail. Won by thy vows and zeal intense I give this high preëminence.” He to the General Sire replied, Not sad, nor wholly satisfied: “When thou, O Brahmá, shalt declare The title, great beyond compare, Of Bráhman saint my worthy meed, Hard earned by many a holy deed, Then may I deem in sooth I hold Each sense of body well controlled.” Then Brahmá cried,“Not yet, not yet: Toil on awhile O Anchoret!”
- **Translation**: 

---

### Verse 5 (Ramayana 0.270)
- **Original**: 252 The Ramayana Thus having said to heaven he went, The saint, upon his task intent, Began his labours to renew, Which sterner yet and fiercer grew. His arms upraised, without a rest, With but one foot the earth he pressed; The air his food, the hermit stood Still as a pillar hewn from wood. Around him in the summer days Five mighty fires combined to blaze. In floods of rain no veil was spread Save clouds, to canopy his head. In the dank dews both night and day Couched in the stream the hermit lay. Thus, till a thousand years had fled, He plied his task of penance dread. Then VishGu and the Gods with awe The labours of the hermit saw, And Zakra, in his troubled breast, Lord of the skies, his fear confessed. And brooded on a plan to spoil The merits of the hermit's toil. Encompassed by his Gods of Storm He summoned Rambhá, fair of form, And spoke a speech for woe and weal, The saint to mar, the God to heal. Canto LXIV. Rambhá.
- **Translation**: 

---

### Verse 6 (Ramayana 0.271)
- **Original**: Canto LXIV. Rambhá. 253 “A great emprise, O lovely maid, To save the Gods, awaits thine aid: To bind the son of Ku[ik sure, And take his soul with love's sweet lure.” Thus order'd by the Thousand-eyed The suppliant nymph in fear replied: “O Lord of Gods, this mighty sage Is very fierce and swift to rage. I doubt not, he so dread and stern On me his scorching wrath will turn. Of this, my lord, am I afraid: Have mercy on a timid maid.” Her suppliant hands began to shake, When thus again Lord Indra spake: “O Rambhá, drive thy fears away, And as I bid do thou obey. In Koïl's form, who takes the heart When trees in spring to blossom start, I, with Kandarpa for my friend, Close to thy side mine aid will lend. [076] Do thou thy beauteous splendour arm With every grace and winsome charm, And from his awful rites seduce This Ku[ik's son, the stern recluse.” Lord Indra ceased. The nymph obeyed: In all her loveliest charms arrayed, With winning ways and witching smile She sought the hermit to beguile. The sweet note of that tuneful bird The saint with ravished bosom heard, And on his heart a rapture passed As on the nymph a look he cast. But when he heard the bird prolong
- **Translation**: 

---

### Verse 7 (Ramayana 0.272)
- **Original**: 254 The Ramayana His sweet incomparable song, And saw the nymph with winning smile, The hermit's heart perceived the wile. And straight he knew the Thousand-eyed A plot against his peace had tried. Then Ku[ik's son indignant laid His curse upon the heavenly maid: “Because thou wouldst my soul engage Who fight to conquer love and rage, Stand, till ten thousand years have flown, Ill-fated maid, transformed to stone. A Bráhman then, in glory strong, Mighty through penance stern and long, Shall free thee from thine altered shape; Thou from my curse shalt then escape.” But when the saint had cursed her so, His breast was burnt with fires of woe, Grieved that long effort to restrain His mighty wrath was all in vain. Cursed by the angry sage's power, She stood in stone that selfsame hour. Kandarpa heard the words he said, And quickly from his presence fled. His fall beneath his passion's sway Had reft the hermit's meed away. Unconquered yet his secret foes, The humbled saint refused repose: “No more shall rage my bosom till, Sealed be my lips, my tongue be still. My very breath henceforth I hold Until a thousand years are told: Victorious o'er each erring sense, I'll dry my frame with abstinence, Until by penance duly done
- **Translation**: 

---

### Verse 8 (Ramayana 0.273)
- **Original**: Canto LXV. Visvámitra's Triumph 255 A Bráhman's rank be bought and won. For countless years, as still as death, I taste no food, I draw no breath, And as I toil my frame shall stand Unharmed by time's destroying hand.” Canto LXV. Visvámitra's Triumph Then from Himálaya's heights of snow, The glorious saint prepared to go, And dwelling in the distant east His penance and his toil increased. A thousand years his lips he held Closed by a vow unparalleled, And other marvels passing thought, Unrivalled in the world, he wrought. In all the thousand years his frame Dry as a log of wood became. By many a cross and check beset, Rage had not stormed his bosom yet. With iron will that naught could bend He plied his labour till the end. So when the weary years were o'er, Freed from his vow so stern and sore, The hermit, all his penance sped, Sate down to eat his meal of bread. Then Indra, clad in Bráhman guise, Asked him for food with hungry eyes. The mighty saint, with steadfast soul, To the false Bráhman gave the whole, And when no scrap for him remained,
- **Translation**: 

---

### Verse 9 (Ramayana 0.274)
- **Original**: 256 The Ramayana Fasting and faint, from speech refrained. His silent vow he would not break: No breath he heaved, no word he spake, Then as he checked his breath, behold! Around his brow thick smoke-clouds rolled And the three worlds, as if o'erspread With ravening flames, were filled with dread. Then God and saint and bard, convened, And Nága lord, and snake, and fiend, Thus to the General Father cried, Distracted, sad, and terrified: “Against the hermit, sore assailed, Lure, scathe, and scorn have naught availed, Proof against rage and treacherous art He keeps his vow with constant heart. Now if his toils assist him naught To gain the boon his soul has sought, He through the worlds will ruin send That fixt and moving things shall end, The regions now are dark with doom, No friendly ray relieves the gloom. Each ocean foams with maddened tide, The shrinking hills in fear subside. Trembles the earth with feverous throe The wind in fitful tempest blows. No cure we see with troubled eyes: And atheist brood on earth may rise. The triple world is wild with care, Or spiritless in dull despair. Before that saint the sun is dim, His blessed light eclipsed by him. Now ere the saint resolve to bring Destruction on each living thing, Let us appease, while yet we may,
- **Translation**: 

---

### Verse 10 (Ramayana 0.275)
- **Original**: Canto LXV. Visvámitra's Triumph 257 Him bright as fire, like fire to slay. Yea, as the fiery flood of Fate Lays all creation desolate, He o'er the conquered Gods may reign: O, grant him what he longs to gain.” [077] Then all the Blest, by Brahmá led, Approached the saint and sweetly said: “Hail, Bráhman Saint! for such thy place: Thy vows austere have won our grace. A Bráhman's rank thy penance stern And ceaseless labour richly earn. I with the Gods of Storm decree Long life, O Bráhman Saint, to thee. May peace and joy thy soul possess: Go where thou wilt in happiness.” Thus by the General Sire addressed, Joy and high triumph filled his breast. His head in adoration bowed, Thus spoke he to the Immortal crowd: “If I, ye Gods, have gained at last Both length of days and Bráhman caste, Grant that the high mysterious name, And holy Vedas, own my claim, And that the formula to bless The sacrifice, its lord confess. And let Va[ishmha, who excels In Warriors' art and mystic spells, In love of God without a peer, Confirm the boon you promise here.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.276)
- **Original**: 258 The Ramayana With Brahmá's son Va[ishmha, best Of those who pray with voice repressed, The Gods by earnest prayer prevailed, And thus his new-made friend he hailed: “Thy title now is sure and good To rights of saintly Bráhmanhood.” Thus spake the sage. The Gods, content, Back to their heavenly mansions went. And Vi[vámitra, pious-souled, Among the Bráhman saints enrolled, On reverend Va[ishmha pressed The honours due to holy guest. Successful in his high pursuit, The sage, in penance resolute, Walked in his pilgrim wanderings o'er The whole broad land from shore to shore. 'Twas thus the saint, O Raghu's son, His rank among the Bráhmans won. Best of all hermits, Prince, is he; In him incarnate Penance see. Friend of the right, who shrinks from ill, Heroic powers attend him still.” The Bráhman, versed in ancient lore, Thus closed his tale, and said no more, To Zatánanda Ku[ik's son Cried in delight, Well done! well done! Then Janak, at the tale amazed, Spoke thus with suppliant hands upraised: “High fate is mine, O Sage, I deem, And thanks I owe for bliss supreme, That thou and Raghu's children too Have come my sacrifice to view. To look on thee with blessed eyes
- **Translation**: 

---

### Verse 12 (Ramayana 0.277)
- **Original**: Canto LXVI. Janak's Speech. 259 Exalts my soul and purifies. Yea, thus to see thee face to face Enriches me with store of grace. Thy holy labours wrought of old, And mighty penance, fully told, Ráma and I with great delight Have heard, O glorious Anchorite. Unrivalled thine ascetic deeds: Thy might, O Saint, all might exceeds. No thought may scan, no limit bound The virtues that in thee are found. The story of thy wondrous fate My thirsty ears can never sate. The hour of evening rites is near: The sun declines in swift career. At early dawn, O Hermit, deign To let me see thy face again. Best of ascetics, part in bliss: Do thou thy servant now dismiss.” The saint approved, and glad and kind Dismissed the king with joyful mind Around the sage King Janak went With priests and kinsmen reverent. Then Vi[vámitra, honoured so, By those high-minded, rose to go, And with the princes took his way To seek the lodging where they lay. Canto LXVI. Janak's Speech.
- **Translation**: 

---

### Verse 13 (Ramayana 0.278)
- **Original**: 260 The Ramayana With cloudless lustre rose the sun; The king, his morning worship done, Ordered his heralds to invite The princes and the anchorite. With honour, as the laws decree, The monarch entertained the three. Then to the youths and saintly man Videha's lord this speech began: “O blameless Saint, most welcome thou! If I may please thee tell me how. Speak, mighty lord, whom all revere, 'Tis thine to order, mine to hear.” Thus he on mighty thoughts intent; Then thus the sage most eloquent: “King Da[aratha's sons, this pair Of warriors famous everywhere, Are come that best of bows to see That lies a treasure stored by thee. This, mighty Janak, deign to show, That they may look upon the bow, And then, contented, homeward go.” Then royal Janak spoke in turn: “O best of Saints, the story learn Why this famed bow, a noble prize, A treasure in my palace lies. A monarch, Devarát by name, Who sixth from ancient Nimi came, Held it as ruler of the land, A pledge in his successive hand. This bow the mighty Rudra bore[078] At Daksha's245 sacrifice of yore, 245 “Daksha was one of the ancient Progenitors or Prajápatis created by Brah- má. The sacrifice which is here spoken of and in whichZankar orZiva (called
- **Translation**: 

---

### Verse 14 (Ramayana 0.279)
- **Original**: Canto LXVI. Janak's Speech. 261 When carnage of the Immortals stained The rite that Daksha had ordained. Then as the Gods sore wounded fled, Victorious Rudra, mocking, said: “Because, O Gods, ye gave me naught When I my rightful portion sought, Your dearest parts I will not spare, But with my bow your frames will tear.” The Sons of Heaven, in wild alarm, Soft flatteries tried his rage to charm. Then Bhava, Lord whom Gods adore, Grew kind and friendly as before, And every torn and mangled limb Was safe and sound restored by him. Thenceforth this bow, the gem of bows, That freed the God of Gods from foes, Stored by our great forefathers lay A treasure and a pride for aye. Once, as it chanced, I ploughed the ground, When sudden, 'neath the share was found An infant springing from the earth, Named Sítá from her secret birth.246 In strength and grace the maiden grew, My cherished daughter, fair to view. also here Rudra and Bhava) smote the Gods because he had not been invited to share the sacred oblations with them, seems to refer to the origin of the worship ofZiva, to its increase and to the struggle it maintained with other older forms of worship.” G ORRESIO {FNS . 246 Sítá means a furrow. “Great Erectheus swayed, That owed his nurture to the blue-eyed maid, But from the teeming furrow took his birth, The mighty offspring of the foodful earth.” Iliad, Book II.
- **Translation**: 

---

### Verse 15 (Ramayana 0.280)
- **Original**: 262 The Ramayana I vowed her, of no mortal birth, Meet prize for noblest hero's worth. In strength and grace the maiden grew, And many a monarch came to woo. To all the princely suitors I Gave, mighty Saint, the same reply: “I give not thus my daughter, she Prize of heroic worth shall be.247 To Míthilá the suitors pressed Their power and might to manifest. To all who came with hearts aglow I offeredZiva's wondrous bow. Not one of all the royal band Could raise or take the bow in hand. The suitors' puny might I spurned, And back the feeble princes turned. Enraged thereat, the warriors met, With force combined my town beset. Stung to the heart with scorn and shame, With war and threats they madly came, Besieged my peaceful walls, and long To Míthilá did grievous wrong. There, wasting all, a year they lay, And brought my treasures to decay, Filling my soul, O Hermit chief, With bitter woe and hopeless grief. At last by long-wrought penance I Won favour with the Gods on high, Who with my labours well content A four-fold host to aid me sent. Then swift the baffled heroes fled To all the winds discomfited— 247 “The whole story of Sítá, as will be seen in the course of the poem has a great analogy with the ancient myth of Proserpine.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 16 (Ramayana 0.281)
- **Original**: Canto LXVII. The Breaking Of The Bow. 263 Wrong-doers, with their lords and host, And all their valour's idle boast. This heavenly bow, exceeding bright, These youths shall see, O Anchorite. Then if young Ráma's hand can string The bow that baffled lord and king, To him I give, as I have sworn, My Sítá, not of woman born.” Canto LXVII. The Breaking Of The Bow. Then spoke again the great recluse: “This mighty bow, O King, produce.” King Janak, at the saint's request, This order to his train addressed: “Let the great bow be hither borne, Which flowery wreaths and scents adorn.” Soon as the monarch's words were said, His servants to the city sped, Five thousand youths in number, all Of manly strength and stature tall, The ponderous eight-wheeled chest that held The heavenly bow, with toil propelled. At length they brought that iron chest, And thus the godlike king addressed: “This best of bows, O lord, we bring, Respected by each chief and king, And place it for these youths to see, If, Sovereign, such thy pleasure be.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.282)
- **Original**: 264 The Ramayana With suppliant palm to palm applied King Janak to the strangers cried: “This gem of bows, O Bráhman Sage, Our race has prized from age to age, Too strong for those who yet have reigned, Though great in might each nerve they strained.[079] Titan and fiend its strength defies, God, spirit, minstrel of the skies. And bard above and snake below Are baffled by this glorious bow. Then how may human prowess hope With such a bow as this to cope? What man with valour's choicest gift This bow can draw, or string, or lift? Yet let the princes, holy Seer, Behold it: it is present here.” Then spoke the hermit pious-souled: “Ráma, dear son, the bow behold.” Then Ráma at his word unclosed The chest wherein its might reposed, Thus crying, as he viewed it:“Lo! I lay mine hand upon the bow: May happy luck my hope attend Its heavenly strength to lift or bend.” “Good luck be thine,” the hermit cried: “Assay the task!” the king replied. Then Raghu's son, as if in sport, Before the thousands of the court, The weapon by the middle raised That all the crowd in wonder gazed. With steady arm the string he drew Till burst the mighty bow in two. As snapped the bow, an awful clang,
- **Translation**: 

---

### Verse 18 (Ramayana 0.283)
- **Original**: Canto LXVII. The Breaking Of The Bow. 265 Loud as the shriek of tempests, rang. The earth, affrighted, shook amain As when a hill is rent in twain. Then, senseless at the fearful sound, The people fell upon the ground: None save the king, the princely pair, And the great saint, the shock could bear. When woke to sense the stricken train, And Janak's soul was calm again, With suppliant hands and reverent head, These words, most eloquent, he said: “O Saint, Prince Ráma stands alone: His peerless might he well has shown. A marvel has the hero wrought Beyond belief, surpassing thought. My child, to royal Ráma wed, New glory on our line will shed: And true my promise will remain That hero's worth the bride should gain. Dearer to me than light and life, My Sítá shall be Ráma's wife. If thou, O Bráhman, leave concede, My counsellors, with eager speed, Borne in their flying cars, to fair Ayodhyá's town the news shall bear, With courteous message to entreat The king to grace my royal seat. This to the monarch shall they tell, The bride is his who won her well: And his two sons are resting here Protected by the holy seer. So, at his pleasure, let them lead The sovereign to my town with speed.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.284)
- **Original**: 266 The Ramayana The hermit to his prayer inclined And Janak, lord of virtuous mind, With charges, to Ayodhyá sent His ministers: and forth they went. Canto LXVIII. The Envoys' Speech. Three nights upon the road they passed To rest the steeds that bore them fast, And reached Ayodhyá's town at last. Then straight at Da[aratha's call They stood within the royal hall, Where, like a God, inspiring awe, The venerable king they saw. With suppliant palm to palm applied, And all their terror laid aside, They spoke to him upon the throne With modest words, in gentle tone: “Janak, Videha's king, O Sire, Has sent us hither to inquire The health of thee his friend most dear, Of all thy priests and every peer. Next Ku[ik's son consenting, thus King Janak speaks, dread liege, by us: “I made a promise and decree That valour's prize my child should be. Kings, worthless found in worth's assay, With mien dejected turned away. Thy sons, by Vi[vámitra led, Unurged, my city visited, And peerless in their might have gained
- **Translation**: 

---

### Verse 20 (Ramayana 0.285)
- **Original**: Canto LXVIII. The Envoys' Speech. 267 My daughter, as my vow ordained. Full in a vast assembly's view Thy hero Ráma broke in two The gem of bows, of monstrous size, That came a treasure from the skies. Ordained the prize of hero's might, Sítá my child is his by right. Fain would I keep my promise made, If thou, O King, approve and aid. Come to my town thy son to see: Bring holy guide and priest with thee. O lord of kings, my suit allow, And let me keep my promised vow. So joying for thy children's sake Their triumph too shalt thou partake, With Vi[vámitra's high consent.” Such words with friendship eloquent Spoke Janak, fair Videha's king, By Zatánanda's counselling.” The envoys thus the king addressed, And mighty joy his heart possessed. To Vámadeva quick he cried, Va [ishmha, and his lords beside: “Lakshma G, and he, my princely boy Who fills Kau[alyá's soul with joy, By Vi[vámitra guarded well Among the good Videhans dwell. [080] Their ruler Janak, prompt to own The peerless might my child has shown, To him would knit in holy ties His daughter, valour's lovely prize. If Janak's plan seem good to you, Come, speed we to his city too,
- **Translation**: 

---



--- End of Ramayan_batch_112.md ---
