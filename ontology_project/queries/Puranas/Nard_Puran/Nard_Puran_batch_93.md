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

### Verse 1 (Nard Puran 224.1841)
- **Original**: (किंतु मिथुन पृष्ठोदय नहीं है)। शेष राशियोंकी पृष्ठभागसे उदय लेनेके कारण पृष्ठोदय कहलाते हैं
- **Translation**: 

---

### Verse 2 (Nard Puran 224.1842)
- **Original**: दिन संज्ञा है (वे दिनमें बली और शीर्षोदय माने
- **Translation**: 

---

### Verse 3 (Nard Puran 224.1843)
- **Original**: पूर्वभाग-द्वितीय पाद 281 गये- हैं); मीन राशिको उभयोदय कहा गया है। मेष
- **Translation**: 

---

### Verse 4 (Nard Puran 224.1844)
- **Original**: सूर्यका मेषमें 10 अंश, चन्द्रमाका वृषमें 3 अंश, आदि राशियाँ क़मसे क्रूर और सौम्य (अर्थात्‌ मेष आदि विषम राशियाँ क्रूर और वृष आदि सम राशियाँ सौम्य) हैं
- **Translation**: 

---

### Verse 5 (Nard Puran 224.1845)
- **Original**: मेष आदि राशियाँ क्रमसे पुरुष, स्त्री और नपुंसक होती हैं (नबीन मतमें दो विभाग हैं, मेष आदि विषम राशियाँ पुरुष और वृष आदि सम राशियाँ स्त्री हैं) । इसी प्रकार मेष आदि राशियाँ क्रमश: चर, स्थिर और द्विस्वभावमें विभाजित हैं (अर्थात्‌ मेष चर, वृष स्थिर और मिथुन द्विस्वभाव हैं, कर्क चर, सिंह स्थिर और कन्या द्विस्वभाव हैं। इसी क्रमसे शेष राशियोंको भी समझे)
- **Translation**: 

---

### Verse 6 (Nard Puran 224.1846)
- **Original**: मेष आदि राशियाँ पूर्व आदि दिशाओंमें स्थित हैं (यथा--मेष, सिंह, धनु पूर्वमें; वृष कन्या, मकर दक्षिणमें; मिथुन, तुला, कुम्भ पश्चिममें और कर्क, वृश्चिक, मीन उत्तरमें स्थित हैं)' । ये सब अपनी-अपनी दिशामें रहती हैं
- **Translation**: 

---

### Verse 7 (Nard Puran 224.1847)
- **Original**: सूर्यका उच्च मेष, चन्द्रमाका वृष, मड्लका मकर, बुधका कन्या, गुरुका कर्क, शुक्रका मीन तथा शनिका उच्च तुला है। मड्जलका मकरमें 28 अंश, बुधका कन्यामें 15 अंश, गुरुका कर्कमें 5 अंश, शुक्रका मीनमें 27 अंश तथा शनिका तुलामें 20 अंश उच्चांश (परमोच्च) है
- **Translation**: 

---

### Verse 8 (Nard Puran 224.1848)
- **Original**: सूर्यादि ग्रहोंकी जो उच्च राशियाँ कही गयी हैं, उनसे सातवां राशि उन ग्रहोंका नीच स्थान है। चरमें पूर्व नवमांश बर्गोत्तम है। स्थिरमें मध्य (पाँचवाँ) नवमांश और द्विस्वभावमें अन्तिम (नवाँ) नवमांश वर्गोत्तम है। तनु (लग्न) आदि बारह भाव हैं
- **Translation**: 

---

### Verse 9 (Nard Puran 224.1849)
- **Original**: सूर्यका सिंह, चन्द्रमाका वृष, मड्डलका मेष, बुधका कन्या, गुरुका धन, शुक्रका तुला और शनिका कुम्भ यह मूल त्रिकोण कहा गया है। चतुर्थ और अष्टभावका नाम चतुरल्न है। नवम और पपञ्ममका नाम त्रिकोण है
- **Translation**: 

---

### Verse 10 (Nard Puran 224.1850)
- **Original**: द्वादश, अष्टम और षष्ठका नाम त्रिक है; लघ्न चतुर्थ, सप्तम और दशमका नाम केन् है। ट्विपद, जलचर, कौट और पशु--ये राशियाँ क्रमश: केद्धमें बली होती हैं (अर्थात्‌ द्विपद लग्रमें, विषय राशियॉमें त्रिंशांश--
- **Translation**: 

---

### Verse 11 (Nard Puran 224.1851)
- **Original**: अंश [5 (58 [7
- **Translation**: 

---

### Verse 12 (Nard Puran 224.1852)
- **Original**: ज्क स्तल सप राशियों विशांश-- "कक्ताहा [6 7
- **Translation**: 

---

### Verse 13 (Nard Puran 224.1853)
- **Original**: 5 क्ष्््ज्क्ल 5 1. मेषादि राज्षियोंके रूप-गुण आदिका बोधक चक्र
- **Translation**: 

---

### Verse 14 (Nard Puran 224.1854)
- **Original**: वृक्षिक
- **Translation**: 

---

### Verse 15 (Nard Puran 224.1855)
- **Original**: ओ' न लिन मल
- **Translation**: 

---

### Verse 16 (Nard Puran 224.1856)
- **Original**: सोकंदव
- **Translation**: 

---

### Verse 17 (Nard Puran 224.1857)
- **Original**: पृ्ेदप कं जा
- **Translation**: 

---

### Verse 18 (Nard Puran 224.1858)
- **Original**: सीम्य [कर [सिम्य क्रिर
- **Translation**: 

---

### Verse 19 (Nard Puran 224.1859)
- **Original**: सौम्य [कर सौम्य [क्र
- **Translation**: 

---

### Verse 20 (Nard Puran 224.1860)
- **Original**: सौम्य [रोल
- **Translation**: 

---

