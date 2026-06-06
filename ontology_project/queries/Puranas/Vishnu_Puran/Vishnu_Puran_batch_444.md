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

### Verse 1 (Vishnu Puran 0.8861)
- **Original**: यहाँ उसने अह्याजीके सहित समस्त देवताओँको प्रणामकर खेदपूर्तक करुणल्वर्से बोलती हुई अपना सारा ृत्तान्त कहा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8862)
- **Original**: पृथिवी बोली--जिस प्रकार अग्नि सुवर्णक्र तथा सूर्य गो (किरण) समूहका परमगुर है उसी प्रकार सम्पूर्ण व्लेकोंके गुरू श्रोनारायण मेरे गुरू हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8863)
- **Original**: वे अज़ापतियोके पति और पूर्वजोंके पूर्वज त्रह्माजी हैं तथा से ही कला-काष्ठा निमेष स्वरूप अन्यक्त मूर्तिमान्‌ काल हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8864)
- **Original**: है देवश्रेष्टण ! आप सब ल्मेगॉका सपुह भी उन्हींका अंशस्वरूप है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8865)
- **Original**: आदित्य, मरुद्रण, साध्यगण, रुद्र, बसु, अग्नि, पितगणः और अत्रि आदि अजापतिगण--ये सब अप्रमेय महात्मा किष्णुके ही रूँदे हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8866)
- **Original**: यक्ष, राक्षस, दैत्य, पिश्ञाच, सर्प, दानस, गन्धर्व और अप्सय आदि भी महात्मा विष्णुके हो रूप हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8867)
- **Original**: अह, नक्षत्र तथा तारागणॉसे चित्रित आकात्ा,; अप्ि, जल, खायु, मैं और इच्धियोंके सम्पूर्ण विषय-- यह सारा जगत्‌ विष्णुमय ही है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8868)
- **Original**: तथापि उन अनेक रूपधारी विष्णुके ये रूप समुद्रकी तसड्रोकि समान रात-दिन एक-दूसरेके बराध्य-बाघक होते रहते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8869)
- **Original**: इस समय कालनेमि आदि दैत्यगण मर्ल्यल्रेकपर अधिकार जमाकर अहर्निश जनताको क्रेशित कर रहे हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8870)
- **Original**: जिस कालनेमिको सामर्थ्यबान्‌ू भगवान्‌ छिष्णुने मारा था, इस समय सही उम्रसेनके पुत्र महान्‌ असुर कंसके रूपमें उत्पन्न हुआ है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8871)
- **Original**: अरिष्ट, धेनुक, केशी, भ्रल्म्ब, नरक, सुन्द, बलिका पुत्र अति भयंकर बाणासुर तथा और भी जो महाबलवान्‌ दुरात्मा राक्षस राजाओंके घरमें उत्पत्र हो गये हैं उनकी. मैं गणना नहीं कर सकती
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8872)
- **Original**: आ्1] अक्षौहिण्योउत्र बहुला दिव्यमूर्त्तिधरास्तुरा: । महाबलानां दृप्तानां दैत्येन्राणां ममोपरि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8873)
- **Original**: 26 तद्धूरिभारपीडार्त्ता न शरक्ोम्यमरेश्वरा: । विभर्त्तुमात्मानमहमिति विज्ञापयामि व:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8874)
- **Original**: 27 क्रियतां तन्महाभागा मम भारावतारणम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8875)
- **Original**: यथा रसातलं नाहं गच्छेबमतिविद्ञला
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8876)
- **Original**: 28 डत्याकर्ण्ण. धरावाक्यमशेपैस्विद्शेश्वरै: । भुवो भारावतारार्थ ब्रह्मा प्राह प्रचोदित:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8877)
- **Original**: 29 ब्रह्मोचाच नस सर्व सत्यमेव दिवोकस: । अहे भव्रो भवन्तश्न सर्वे नारायणात्मका:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8878)
- **Original**: 30 विभृतयश्च यास्तस्थ तासामेव परस्परम्‌। आधिकय न्यूनता बाध्यबाधकत्वेन वर्तते बाध्यबाधकत्वेन वर्तते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8879)
- **Original**: 31 तदागच्छत गच्छाम क्षीराब्धेस्तटमुत्तमम्‌। तत्राराध्य हरि तस्मै सर्व विज्ञापयाम वै
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8880)
- **Original**: 32 सर्वथैव जगत्यर्थे स सर्वात्मा जगन्मय: । सत्तांशेनावतीर्योष्यां घर्मस्य कुरुते स्थितिम्‌
- **Translation**: 

---

