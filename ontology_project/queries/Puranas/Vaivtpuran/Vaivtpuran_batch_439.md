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

### Verse 1 (Vaivtpuran 23.1742)
- **Original**: तेजोमण्डलके भीतर सदा साकार, सर्वात्मा, स्वेच्छामय बनानेमें सदा ही समर्थ होता है, उसी प्रकार वह
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1743)
- **Original**: पुरुषके मनोहर रूपका ध्यान करते हैं। करोड़ों ब्रह्म प्रकृतिके द्वारा सृष्टिका निर्माण करनेमें नित्य
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1744)
- **Original**: सूर्योंके समान प्रकाशमान जो मण्डलाकार तेज:पुझ्न समर्थ है। जैसे सुनार सुबर्णसे कुण्डल बनानेकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1745)
- **Original**: है, उसके भीतर नित्यधाम छिपा हुआ है, शक्ति रखता है, उसी तरह परमेश्वर उपादानभूता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1746)
- **Original**: जिसका नाम गोलोक है। बह मनोहर लोक चारों प्रकृतिके द्वारा सदा सृष्टि करनेमें समर्थ है। जैसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1747)
- **Original**: ओरसे लक्षकोटि योजन विस्तृत है। सर्वश्रेष्ठ दिव्य कुम्हार मिट्टीका निर्माण नहीं करता, मिट्टी उसके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1748)
- **Original**: रत्रोंके सारतत्त्वसे जिनका निर्माण हुआ है, ऐसे लिये नित्य एवं सनातन है तथा जैसे सुनार
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1749)
- **Original**: दिव्य भवनों तथा गोपाड्नाओंसे बह लोक भरा सुवर्णकी सृष्टि नहीं करता, सुवर्ण उसके लिये
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1750)
- **Original**: हुआ है। उसे सुखपूर्वक देखा जा सकता है। नित्य वस्तु ही है, उसी प्रकार वह परब्रह्म
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1751)
- **Original**: चन्द्रमण्डलके समान ही बह गोलाकार है। रत्रेद्रसारसे परमात्मा नित्य है और बह प्रकृति भी नित्य मानी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1752)
- **Original**: निर्मित वह धाम परमात्माकी इच्छाके अनुसार गयी है। इसीलिये कुछ लोग सृष्टिमें उन दोनोंकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1753)
- **Original**: बिना किसी आधारके ही स्थित है। उस नित्य ही समानरूपसे प्रधानता बतलाते हैं। कुम्हार और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1754)
- **Original**: लोककी स्थिति वैकुण्ठसे पचास करोड़ योजन सुनार स्वयं मिट्टी और सुवर्ण पैदा करके लानेमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1755)
- **Original**: ऊपर है। बहाँ गौएँ, गोप और गोपियाँ निवास समर्थ नहीं हैं तथा मिट्टी और सुवर्ण भी कुम्हार
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1756)
- **Original**: करती हैं। वहाँ कल्पवृक्षोंके वन हैं। गोलोक और सुनारकों ले आनेकी शक्ति नहीं रखते। अत:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1757)
- **Original**: कामधेनु गौओंसे भरा हुआ तथा रासमण्डलसे मिट्टी और कुम्हारकी घटमें तथा सुवर्ण और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1758)
- **Original**: मण्डित है। मुने! बह बृन्दाबनसे आच्छन्न और सुनारको कुण्डलमें समानरूपसे प्रधानता है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1759)
- **Original**: विरजा नदीसे आवेष्टित है। वहाँ सैकड़ों शिखरोंसे नारद! इस विवेचनसे ब्रह्म प्रकृतिसे परे ही
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1760)
- **Original**: सुशोभित गिरिराज विराजमान है। सुवर्णनिर्मित
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1761)
- **Original**: कं सरहाखेण्ड क्र 851
- **Translation**: 

---

