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

### Verse 1 (Vaivtpuran 4.8616)
- **Original**: घधारे 2? आप उनकी लीला-कथा सुनाइये; क्योंकि उसका श्रवण और कोर्तन पुण्यदायक है। श्रीहरिकी कथा अत्यन्त दुर्लभ है। वह भवसागरसे पार उतारनेके लिये नौकाके तुल्य है। प्रारब्धभोगरूपी बेड़ी तथा क्लेशोंका उच्छेद करनेके लिये कटार है। पापरूपी ईंधन-राशिका दाह करनेके लिये प्रज्वलित अग्नि-शिखाके समान है। इसे सुननेवाले
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8768)
- **Original**: 304 + संक्षिप्त ब्रह्मवैवर्तपुराण « 1666#####&# 6 # 44 4454 4 # # 4 4 $ 44 4 % 5 5 / 5 / 5 कक क# # 44% 45 5 5 / 845 48 8888 ### 68 ## ## अऊ अफ ड घक महामुने! ब्रह्मा आदिका किया हुआ यह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8769)
- **Original**: पचास करोड़ योजन ऊपर है और भगवान्‌ स्तोत्र जो छः श्लोकोंमें वर्णित है, पढ़कर मनुष्य
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8770)
- **Original**: श्रीकृष्णकी इच्छासे निर्मित है। उसका कोई बाह्य दुर्गग संकटसे मुक्त होता और मनोवाज्छित
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8771)
- **Original**: आधार नहीं है। श्रीकृष्ण ही बायुरूपसे उसे धारण 'फलको पाता है।* करते हैं। वे ब्रह्मा आदि देवता उस अनिर्वचनीय देवताओंकी स्तुति सुनकर साक्षात्‌ श्रीहरिने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8772)
- **Original**: लोककी ओर जानेके लिये उन्मुख हो चल दिये। उनसे कहा--तुम सब लोग गोलोकको जाओ।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8773)
- **Original**: उन सबकी गति मनके समान तीत्र थी। अतः पीछेसे मैं भी लक्ष्मीके साथ आऊँगा। श्वेतद्वीपनिवासी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8774)
- **Original**: वे सब-के-सब विरजाके तटपर जा पहुँचे। वे नर और नारायण मुनि तथा सरस्वतीदेवी--ये
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8775)
- **Original**: सरिताके तटका दर्शन करके उन देवताओंको बड़ा गोलोकमें जायँगे। अनन्तशेषनाग, मेरी माया,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8776)
- **Original**: आश्चर्य हुआ। विरजा नदीका बह तटप्रान्त शुद्ध कार्तिकिय, गणेश तथा वेदमाता सावित्री--ये सब
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8777)
- **Original**: स्फटिकमणिके समान उज्ज्वल, अत्यन्त विस्तृत पीछेसे निश्चित ही वहाँ जायँगे। वहाँ मैं गोपियों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8778)
- **Original**: और मनोहर था, मोती-माणिक्य तथा उत्कृष्ट तथा राधाके साथ द्विभुज श्रीकृष्णरूपसे निवास
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8779)
- **Original**: मणिरत्ञोंकी खानोंसे सुशोभित था। काले, उज्ज्वल, करता हूँ। यहाँ सुनन्द आदि पार्षदों तथा लक्ष्मीके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8780)
- **Original**: हरे तथा लाल रत्नोंकी श्रेणियोंसे उद्धासित होता साथ रहता हूँ। नारायण, श्रीकृष्ण तथा स्वेतद्वीपनिवासी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8781)
- **Original**: था। उस तटपर कहाँ तो मूँगोंके अड्डुर प्रकट विष्णु मैं ही हूँ। ब्रह्मा आदि अन्य सम्पूर्ण देवता
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8782)
- **Original**: हुए हैं, जो अत्यन्त मनोहर दिखायी देते हैं। मेरी ही कलाएँ हैं। देव, असुर और मनुष्य आदि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8783)
- **Original**: कहीं बहुमूल्य उत्तम रत्रोंकी अनेक खानें उसकी प्राणी मेरी कलाकी कलाकी अंशकलासे उत्पन्न
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8784)
- **Original**: शोभा बढ़ाती हैं। कहीं श्रेष्ठ निधियोंके आकर हुए हैं। तुमलोग गोलोकको जाओ। वहाँ तुम्हारे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8785)
- **Original**: उपलब्ध होते हैं, जिनसे वहाँकी छटा आश्चर्यमें अभीष्ट कार्यकी सिद्धि होगी। फिर हमलोग भी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8786)
- **Original**: डाल देती है। वह दृश्य विधाताके भी दृष्टिपथम्ें सबकी इष्टसिद्धिके लिये वहाँ आ जायँगे।
- **Translation**: 

---

