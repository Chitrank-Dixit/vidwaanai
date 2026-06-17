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

### Verse 1 (Vaivtpuran 36.7962)
- **Original**: 376 * संक्षिप्त ग्रह्मवैवर्तपुराण + 44 5. 28 5. 2 2 2 2.2 2 8 8 2 2 9
- **Translation**: 

---

### Verse 2 (Vaivtpuran 36.7963)
- **Original**: ) 2] 2 0 0 ) 9 ] 20 ] 0408 ]889897 सुचन्द्र-पुत्र पुष्कराक्षके साथ परशुरामका युद्ध, पाशुपतास्त्र छोड़नेके लिये उद्यत परशुरामके पास विष्णुका आना और उन्हें समझाना, विष्णुका विप्रवेषसे पुत्रसहित पुष्कराक्षसे लक्ष्मीकवच तथा दुर्गाकबचको माँग लेना, लक्ष्मी-कवचका वर्णन श्रीनारायण कहते हैं--ब्रह्मन्‌! रणक्षेत्रमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 36.7964)
- **Original**: है; क्योंकि श्रीहरिका सुदर्शनचक्र समस्त अस्त्रोंका राजाधिराजोंके शिरोमणि सुचन्द्रके गिर जानेपर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.7965)
- **Original**: मान मर्दन करनेवाला है। शिवजीका पाशुपतास्त्र तीन अक्षौहिणी सेनाके साथ पुष्कराक्ष आ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.7966)
- **Original**: और श्रीहरिका सुदर्शनचक्र-ये ही दोनों तीनों धमका। महान्‌ पराक्रमी राजा पुष्कराक्ष सूर्यवंशमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.7967)
- **Original**: लोकोंमें समस्त अस्त्रोंमें प्रधान हैं। इसलिये उत्पन्न, महालक्ष्मीका सेवक, लक्ष्मीवान्‌ और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.7968)
- **Original**: ब्रह्मन्‌! तुम पाशुपतास्त्रको रख दो और मेरी बात सूर्यक समान प्रभाशाली था। वह सुचन्द्रका पुत्र
- **Translation**: 

---

### Verse 8 (Vaivtpuran 36.7969)
- **Original**: सुनों। इस समय तुम जिस प्रकार महाबली राजा था। उसके गलेमें महालक्ष्मीका मनोहर कवच
- **Translation**: 

---

### Verse 9 (Vaivtpuran 36.7970)
- **Original**: पुष्कराक्षको जीत सकोगे तथा जिस प्रकार अजेय बँधा था, जिसके प्रभावसे वह परमैश्चर्यसम्पन्न
- **Translation**: 

---

### Verse 10 (Vaivtpuran 36.7971)
- **Original**: कार्तवीर्यपर विजय पा सकोगे, वह सारा उपाय और त्रिलोकविजयी हो गया था। उसे देखकर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 36.7972)
- **Original**: तुम्हें बतलाता हूँ; सावधानतया श्रवण करो। बुद्धिमान्‌ू परशुरामके सभी भाई हाथोंमें नाना
- **Translation**: 

---

### Verse 12 (Vaivtpuran 36.7973)
- **Original**: महालक्ष्मीका कवच, जो तीनों लोकोमें दुर्लभ है, प्रकारके शस्त्रासत्र धारण करके युद्ध करनेके लिये
- **Translation**: 

---

### Verse 13 (Vaivtpuran 36.7974)
- **Original**: पुष्कराक्षने भक्तिपूर्वक विधि-विधानके साथ अपने आ डटे। राजाने लीलापूर्वक बाणसमूहकी वर्षा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 36.7975)
- **Original**: गलेमें धारण कर रखा है और पुष्कराक्षका पुत्र करके उन्हें छेद डाला। तब उन वीरोंने भी हँसते-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 36.7976)
- **Original**: दुर्गतिनाशिनी दुर्गाका परम अद्भुत एवं उत्तम हँसते उन बाणोंके टुकड़े-टुकड़े कर डाले। फिर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 36.7977)
- **Original**: ककच अपनी दाहिनी भुजापर बाँधे हुए है। इन तो पुष्कराक्षेके साथ घोर युद्ध आरम्भ हुआ।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 36.7978)
- **Original**: कवचोंकी कृपासे वे दोनों विश्वपर विजय पा परशुरामने पाशुपतास्त्रके सिवा सभी अस्त्र-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 36.7979)
- **Original**: लेनेमें समर्थ हैं। उनके शरीरपर कवचोंके वर्तमान शस्त्रोंका प्रयोग किया, पर पुष्कराक्षने सबको [रहते त्रिभुवनमें उन्हें कौन जीत सकता है। मुने ! काट गिराया। तब अपने समस्त शश्त्रास्त्रोंकों
- **Translation**: 

---

### Verse 19 (Vaivtpuran 36.7980)
- **Original**: मैं तुम्हारी प्रतिज्ञा सफल करनेके निमित्त उन विफल देखकर परशुरामने स्नान करके शिवजीको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 36.7981)
- **Original**: दोनोंके संनिकट माँगनेके लिये जाऊँगा और उनसे प्रणाम किया और पाशुपतास्त्रका प्रयोग करना
- **Translation**: 

---

