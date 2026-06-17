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

### Verse 1 (Bramha 0.5821)
- **Original**: है, वह सब तू ही है। जो प्रातःकाल और आधी रातके समय मेरा प्रादुर्भाव होगा और तू
- **Translation**: 

---

### Verse 2 (Bramha 0.5822)
- **Original**: अपराहमें तेरे सामने मस्तक झुकायेंगे और तुझे नवमी तिथिमें यशोदाके गर्भसे जन्म लेगी। उस
- **Translation**: 

---

### Verse 3 (Bramha 0.5823)
- **Original**: आर्या, दुर्गा, वेदगर्भा, अम्बिका, भद्रा, भद्रकाली, समय बसुदेव मेरी शक्तिसे प्रेरित होकर मुझे तो
- **Translation**: 

---

### Verse 4 (Bramha 0.5824)
- **Original**: क्षेम्या तथा क्षेमंकरी आदि कहकर तेरी स्तुति यशोदाकी शब्यापर पहुँचा देंगे और तुझे देवकीके
- **Translation**: 

---

### Verse 5 (Bramha 0.5825)
- **Original**: करेंगे, उनके समस्त मनोरथ मेरे प्रसादसे सिद्ध हो पास लायेंगे। फिर कंस तुझे लेकर पत्थरकी
- **Translation**: 

---

### Verse 6 (Bramha 0.5826)
- **Original**: जायँंगे। जो लोग भक्ष्य-भोज्य आदि पदार्थसे तेरी शिलापर पछाड़ेगा, किंतु तू उसके हाथसे निकलकर
- **Translation**: 

---

### Verse 7 (Bramha 0.5827)
- **Original**: पूजा करेंगे, उन मनुष्योंपर प्रसन्न होकर तू उनकी आकाशमें ठहर जायगी। यों करनेपर इन्द्र मेरे
- **Translation**: 

---

### Verse 8 (Bramha 0.5828)
- **Original**: समस्त अभिलाषाएँ पूर्ण करेगी। वे सब लोग सदा गौरवका स्मरण करके तुझे सौ-सौ बार प्रणाम करेंगे
- **Translation**: 

---

### Verse 9 (Bramha 0.5829)
- **Original**: मेरी कृपासे निश्चय ही कल्याणके भागी होंगे; और विनीतभावसे अपनी बहिन बना लेंगे। फिर तू
- **Translation**: 

---

### Verse 10 (Bramha 0.5830)
- **Original**: अतः देवि! जो कार्य मैंने तुझे बताया है, उसे पूर्ण शुम्भ-निशुम्भ आदि सहसौरों दैत्योंका वध करके
- **Translation**: 

---

### Verse 11 (Bramha 0.5831)
- **Original**: करनेके लिये जा।' #+*#ग्येधयएन> न भगवान्‌का अवतार, गोकुलगमन, पूतना-वध, शकट-भजञ्ञन, -उद्धार, गोपोंका वृन्दावनगमन तथा बलराम और श्रीकृष्णका बछड़े चराना व्यासजी कहते हैं--देवाधिदेव श्रीहरिने पहले
- **Translation**: 

---

### Verse 12 (Bramha 0.5832)
- **Original**: गयीं। देवकोके शरीरमें इतना तेज आ गया कि जैसा आदेश दिया था, उसके अनुसार जगज्जननी
- **Translation**: 

---

### Verse 13 (Bramha 0.5833)
- **Original**: कोई उनको ओर आँख उठाकर देख भी नहीं योगमायाने देवकौके उदरमें क्रमश: छ: गर्भ
- **Translation**: 

---

### Verse 14 (Bramha 0.5834)
- **Original**: सकता था। देवतागण स्त्री-पुरुषोंसे अदृश्य रहकर स्थापित किये और सातबेंको खींचकर रोहिणीके
- **Translation**: 

---

### Verse 15 (Bramha 0.5835)
- **Original**: अपने उदरमें श्रीविष्णुकों धारण करनेवाली माता उदरमें डाल दिया। तदनन्तर तीनों लोकोंका
- **Translation**: 

---

### Verse 16 (Bramha 0.5836)
- **Original**: देवकीका प्रतिदिन स्तवन करने लगे। उपकार करनेके लिये साक्षात्‌ श्रीहरिने देवकीके
- **Translation**: 

---

### Verse 17 (Bramha 0.5837)
- **Original**: देवता बोले--देवि! तुम स्वाहा, तुम स्वधा गर्भमें प्रवेश किया और उसी दिन योगनिद्रा
- **Translation**: 

---

### Verse 18 (Bramha 0.5838)
- **Original**: और तुम्हीं विद्या, सुधा एवं ज्योति हो। इस यशोदाके उदरमें प्रविष्ट हुईं। भगवान्‌ विष्णुके
- **Translation**: 

---

### Verse 19 (Bramha 0.5839)
- **Original**: पृथ्वीपर सम्पूर्ण लोकोंको रक्षाके लिये तुम्हारा अंशके भूतलपर आते ही आकाशमें ग्रहोंकी गति
- **Translation**: 

---

### Verse 20 (Bramha 0.5840)
- **Original**: अवतार हुआ है। तुम प्रसन्न होकर सम्पूर्ण अथावत्‌ होने लगी। समस्त ऋतुएँ सुखदायिनी हो
- **Translation**: 

---

