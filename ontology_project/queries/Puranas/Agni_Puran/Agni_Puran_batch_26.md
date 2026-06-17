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

### Verse 1 (Agni Puran 0.501)
- **Original**: सर्वदुष्टानि रक्षांसि क्षयं यान्तु विभीषण। प्राच्यां प्रतीच्यां च दिशि दक्षिणोत्तरतस्तथा
- **Translation**: 

---

### Verse 2 (Agni Puran 0.502)
- **Original**: 39 4 रक्षां करोतु सर्वात्मा नरसिंह: स्वगर्जिते:। दिवि भुव्यन्तरिक्षे च पृष्ठतः पारश्चतोउग्रत: # 40
- **Translation**: 

---

### Verse 3 (Agni Puran 0.503)
- **Original**: रक्षां करोतु भगवान्‌ बहुरूपी जनार्दन:। यथा विष्णुर्जगत्सरव॑ सदेवासुरमानुषम्‌
- **Translation**: 

---

### Verse 4 (Agni Puran 0.504)
- **Original**: तेन सत्येन दुष्टानि शममस्य ब्रजन्तु वै। वासुदेव! आप सर्वात्मा परमेश्वर जनार्दन हैं। इस व्यक्तिके जो भी रोग, महान्‌ उत्पात, विष, महाग्रह, क्रूर भूत, दारुण ग्रहपीडा तथा ज्वालागर्दभक आदि शस्त्र-क्षत-जनित दोष हों, उन सबका कोई भी रूप धारण करके नाश करें। देवश्रेष् अच्युत ! ज्वालामालाओंसे अत्यन्त भीषण सुदर्शन- चक्रको प्रेरित करके समस्त दुष्ट रोगोंका शमन कौजिये। महाभयंकर सुदर्शन! तुम प्रचण्ड ज्वालाओंसे सुशोभित और महान्‌ शब्द करनेवाले हो; अत: सम्पूर्ण दुष्ट राक्षसोंका संहार करो, संहार करो। बे तुम्हारे प्रभावसे क्षयको प्राप्त हों। पूर्व, पश्चिम, उत्तर और दक्षिण दिशामें सर्वात्मा नृसिंह अपनी गर्जनासे रक्षा करें। स्वर्गलोकमें, भूलोकमें, अन्तरिक्षमें तथा आगे-पीछे अनेक रूपधारी भगवान्‌ जनार्दन रक्षा करें। देवता, असुर और मनुष्योंसहित यह सम्पूर्ण जगत्‌ भगवान्‌ विष्णुका ही स्वरूप है; इस सत्यके प्रभावसे इसके दुष्ट रोग शान्त हों
- **Translation**: 

---

### Verse 5 (Agni Puran 0.505)
- **Original**: 35- 41 3
- **Translation**: 

---

### Verse 6 (Agni Puran 0.506)
- **Original**: यथा विष्णौ स्मृते सद्यः संक्षयं यान्ति पातका:
- **Translation**: 

---

### Verse 7 (Agni Puran 0.507)
- **Original**: सत्येन तेन सकल॑ दुष्ट्रमस्य प्रशाम्यतु। यथा यज्ञेश्वरो विष्णुर्देवेष्यपि हि गीयते
- **Translation**: 

---

### Verse 8 (Agni Puran 0.508)
- **Original**: सत्येन तेन सकल॑ यन्मयोक्त तथास्तु तत्‌। शान्तिरस्तु शिव चास्तु दुष्टमस्य प्रशाम्यतु
- **Translation**: 

---

### Verse 9 (Agni Puran 0.509)
- **Original**: वासुदेवशरीरोत्यै: कुशैर्नि्णाशितं मया। अपामार्जतु गोविन्दो नरो नारायणस्तथा
- **Translation**: 

---

### Verse 10 (Agni Puran 0.510)
- **Original**: तथास्तु सर्वदुःखानां प्रशमो बचनाद्धरे:।
- **Translation**: 

---

### Verse 11 (Agni Puran 0.511)
- **Original**: अपामार्जनक॑ शस्तं सर्वरोगादिवारणम्‌
- **Translation**: 

---

### Verse 12 (Agni Puran 0.512)
- **Original**: शान्त हो। मैंने भगवान्‌ वासुदेवके शरीरसे प्रादुर्भूत अहं हरिः कुशा विष्णुईता रोगा मया तव
- **Translation**: 

---

### Verse 13 (Agni Puran 0.513)
- **Original**: कुशोंसे इसके रोगोंको नष्ट किया है। नर-नारायण श्रीविष्णुके स्मरणमाज्नसे पापसमूह तत्काल नष्ट
- **Translation**: 

---

### Verse 14 (Agni Puran 0.514)
- **Original**: और गोविन्द-इसका अप्ामार्जन करें। श्रीहरिके हो जाते हैं, इस सत्यके प्रभावसे इसके समस्त
- **Translation**: 

---

### Verse 15 (Agni Puran 0.515)
- **Original**: वचनसे इसके सम्पूर्ण दुःखोंका शमन हो जाय। दूषित रोग शान्त हो जायें। यज्ञेश्वर विष्णु देवताओंद्वार
- **Translation**: 

---

### Verse 16 (Agni Puran 0.516)
- **Original**: समस्त रोगादिके निवारणके लिये “अपामार्जन- प्रशंसित होते हैं; इस सत्यके प्रभावसे मेरा कथन
- **Translation**: 

---

### Verse 17 (Agni Puran 0.517)
- **Original**: स्तोत्र' प्रशस्त है। मैं श्रीहरि हूँ, कुशा विष्णु हैं। सत्य हो। शान्ति हो, मंगल हो। इसका दुष्ट रोग
- **Translation**: 

---

### Verse 18 (Agni Puran 0.518)
- **Original**: मैंने तुम्हारे रोगोंका नाश कर दिया है
- **Translation**: 

---

### Verse 19 (Agni Puran 0.519)
- **Original**: 42--47
- **Translation**: 

---

### Verse 20 (Agni Puran 0.520)
- **Original**: इस प्रकार आदि आरनेय महापुराणमें 'कुशाप्रामार्जन-स्तोत्रका वर्णन नामक इकतीसवाँ अध्याय पूरा हुआ
- **Translation**: 

---

