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

### Verse 1 (Vaivtpuran 7.9753)
- **Original**: देख वहाँ आकाशवाणी हुई--' बसुश्रेष्ठ ! तुम दोनों गोलोकनाथकी महिमाका कौन वर्णन कर सकता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9754)
- **Original**: दूसरे जन्ममें भूतलपर अवतीर्ण हो गोकुलमें अपने है? जिन्हें स्वयं हम भी नहीं जानते और न पुत्रके रूपमें श्रीहरिके दर्शन करोगे; योगियोंकों वेद ही जानते हैं। फिर दूसरे विद्वान्‌ क्या जान
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9755)
- **Original**: भी उन भगवान्‌का दर्शन होना अत्यन्त कठिन सकते हैं ? शूकर, वामन, कल्कि, बुद्ध, कपिल
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9756)
- **Original**: है। बड़े-बड़े विद्वानोंक लिये भी ध्यानके द्वारा और मत्स्य--ये भी श्रीकृष्णके अंश हैं तथा अन्य
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9757)
- **Original**: उन्हें वशमें कर पाना असम्भव है। वे ब्रह्मा आदि कितने ही अवतार हैं, जो श्रीकृष्णकी कलामात्र
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9758)
- **Original**: देवताओंके भी बन्दनीय हैं।' यह सुनकर धरा हैं। नूसिंह, राम तथा श्वेतद्वीपके स्वामी विराट्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9759)
- **Original**: और द्रोण सुखपूर्वक अपने घरकों चले गये विष्णु पूर्ण अंशसे सम्पन्न हैं। श्रीकृष्ण परिपूर्णतम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9760)
- **Original**: और भारतवर्षमें जन्म लेकर उन्होंने श्रीहरिके परमात्मा हैं। वे स्वयं ही बैकुण्ठ और गोकुलमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9761)
- **Original**: मुखारबिन्दके दर्शन किये। इस प्रकार यशोदा और निवास करते हैं। वैकुण्ठमें वे कमलाकान्त कहे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9762)
- **Original**: नन्दका चरित तुमसे कहा गया; अब देवताओंके गये हैं और रूप-भेदसे चतुर्भुज हैं। गोलोक और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9763)
- **Original**: लिये भी परम गोपनीय रोहिणीका चरित्र सुनो। गोकुलमें ये द्विभुज श्रीकृष्ण स्वयं ही राधाकानत)
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9764)
- **Original**: एक समय देवमाता अदितिने ऋतुमती कहलाते हैं। योगी पुरुष इन्हींके तेजको सदा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9765)
- **Original**: होनेपर समस्त श्रृज्ञारोंसे सुसज्जित हो अपने अपने चित्तमें धारण करते हैं। भक्त पुरुष इन्हीं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9766)
- **Original**: पतिदेव श्रीकश्यपजीसे मिलना चाहा। उस समय भगवान्‌के तेजोमय चरणारविन्दका चिन्तन करते
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9767)
- **Original**: कश्यपजी अपनी दूसरी पत्नी सर्पमाता कद्गके हैं। भला, तेजस्वीके बिना तेज कहाँ रह सकता
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9768)
- **Original**: पास थे। कश्यपजीके आनेमें विलम्ब होनेपर है? ब्रह्मन्‌! सुनो। मैं तुमसे यशोदा, नन्द और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9769)
- **Original**: अदितिको बहुत क्षोभ हुआ और उन्होंने कद्रको रोहिणीके तपका वर्णन करता हूँ, जिसके कारण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9770)
- **Original**: शाप दे दिया कि 'वे स्वर्गलोकको त्यागकर उन्होंने श्रीहरिका मुँह देखा था। वसुओंमें श्रेष्ठ मानव-योनिको प्राप्त हों।!' इस बातकों सुनकर तपोधन द्रोण नन्द नामसे इस धरातलपर अवतीर्ण
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9771)
- **Original**: कट्टने भी अदितिको शाप दिया कि “वे जरायुक्त हुए थे। उनकी पन्नी जो तपस्विनी धरा थीं, वे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9772)
- **Original**: होकर मर्त्यलोकमें मानव-योनिमें जायेँ।' ही सती-साध्वी यशोदा हुई थीं। सर्पोंको जन्म
- **Translation**: 

---

