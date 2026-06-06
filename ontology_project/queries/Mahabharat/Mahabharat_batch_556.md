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

### Verse 1 (Mahabharat 0.5551)
- **Original**: 108 संक्षिप्त महाभारत [ जल्यपर्व बह रथ्पर बैठे हुए पाण्डुपुन्नोंपर, धृष्टश्युज्रपप और आनर्त
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5551)
- **Original**: 108 संक्षिप्त महाभारत [ जल्यपर्व बह रथ्पर बैठे हुए पाण्डुपुन्नोंपर, धृष्टश्युज्रपप और आनर्त
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5552)
- **Original**: कृपाचार्यको भी घायल किया। घोड़े मारे जानेसे कृतवर्मा देशके राजापर बाणोंकी वर्षा करने छगा। जैसे मरणश्र्मा
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5552)
- **Original**: कृपाचार्यको भी घायल किया। घोड़े मारे जानेसे कृतवर्मा देशके राजापर बाणोंकी वर्षा करने छगा। जैसे मरणश्र्मा
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5553)
- **Original**: रथहीन हो गया--यह देख अश्वद्थामा उसे अपने रथषपर मनुष्य अपनी मौतको नहीं टाल सकते, उसी प्रकार ये पाण्डक बिठाकर युथिष्ठिरसे दूर हटा ले गया। महाराज ! आप और महारथी दुर्घोधनको नहीं ल्मैघ सके ।
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5553)
- **Original**: रथहीन हो गया--यह देख अश्वद्थामा उसे अपने रथषपर मनुष्य अपनी मौतको नहीं टाल सकते, उसी प्रकार ये पाण्डक बिठाकर युथिष्ठिरसे दूर हटा ले गया। महाराज ! आप और महारथी दुर्घोधनको नहीं ल्मैघ सके ।
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5554)
- **Original**: आपके पुत्रके अन्यायसे इस प्रकार झेष युद्ध हुआ था।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5554)
- **Original**: आपके पुत्रके अन्यायसे इस प्रकार झेष युद्ध हुआ था।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5555)
- **Original**: चरुधिष्ठिरके द्वारा झल्वके मारे जानेपर सब पाण्डव प्रसन्न हो इसी बीचमें कृतवर्मा भी दूसरे रथपर बैठकर वहाँ आ
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5555)
- **Original**: चरुधिष्ठिरके द्वारा झल्वके मारे जानेपर सब पाण्डव प्रसन्न हो इसी बीचमें कृतवर्मा भी दूसरे रथपर बैठकर वहाँ आ
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5556)
- **Original**: झद्भू बजाने लगे। सबने राजा युथ्चिष्ठिरकी धूरि-धूरि प्रशंसा पहुँचा । तब युथिष्ठिस्ने चार बाणोंसे कृतवर्माके चारों घोड़ोंको
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5556)
- **Original**: झद्भू बजाने लगे। सबने राजा युथ्चिष्ठिरकी धूरि-धूरि प्रशंसा पहुँचा । तब युथिष्ठिस्ने चार बाणोंसे कृतवर्माके चारों घोड़ोंको
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5557)
- **Original**: की । नाना प्रकारके बाजे बजाये गये, जिससे चारों ओस्की यमल्ओोक पहुँचा दिया और तेज किये हुए छः भल्लोंसे
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5557)
- **Original**: की । नाना प्रकारके बाजे बजाये गये, जिससे चारों ओस्की यमल्ओोक पहुँचा दिया और तेज किये हुए छः भल्लोंसे
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5558)
- **Original**: पृथ्वी गूँज उठी । कऊफमा और मद्रराजके अनुचरोंका वध, कौरव-सेनाका पलायन, भीमद्वारा इक्कीस हजार पैदलोंका संहार और दुर्योधनका अपनी सेनाको उत्साहित करना
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5558)
- **Original**: पृथ्वी गूँज उठी । कऊफमा और मद्रराजके अनुचरोंका वध, कौरव-सेनाका पलायन, भीमद्वारा इक्कीस हजार पैदलोंका संहार और दुर्योधनका अपनी सेनाको उत्साहित करना
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5559)
- **Original**: सऊय कहते हैं--ज्ल्यके मारे जानेपर उनके अनुयायी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5559)
- **Original**: सऊय कहते हैं--ज्ल्यके मारे जानेपर उनके अनुयायी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5560)
- **Original**: तो वे गाष्डीवकी टेकार करते हुए वहाँ आ पहुँचे। उस समय सात सौ रथी युधिष्ठिरसे लड़नेके लिये आगे बढ़े ! उस समय
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5560)
- **Original**: तो वे गाष्डीवकी टेकार करते हुए वहाँ आ पहुँचे। उस समय सात सौ रथी युधिष्ठिरसे लड़नेके लिये आगे बढ़े ! उस समय
- **Translation**: 

---

