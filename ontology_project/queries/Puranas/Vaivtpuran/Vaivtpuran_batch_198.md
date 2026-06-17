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

### Verse 1 (Vaivtpuran 13.10102)
- **Original**: इत्यादि कार्य करके ये श्रीकृष्ण श्रीराधाके साथ भीतर अक्रूरको अपने स्वरूपका दर्शन कराकर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10103)
- **Original**: फिर ब्रजमें आयेंगे। तदनन्तर अपने नारायण- उन्हें ज्ञान देंगे। फिर सायंकाल मथुरामें पहुँचकर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10104)
- **Original**: अंशको द्वारकापुरीमें भेजकर ये जगदीश्वर गोलोकनाथ कौतूहलवश नगरमें घृम-घूमकर सबको दर्शन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10105)
- **Original**: यहाँ राधाके साथ समस्त आवश्यक कार्यय पूर्ण देंगे। माली, दर्जी और कुब्जाको भवबन्धनसे मुक्त
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10106)
- **Original**: करेंगे तथा व्रजवासियों एवं राधाकों साथ लेकर करेंगे। शंकरजीके धनुषकों तोड़कर यज्ञभूमिका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10107)
- **Original**: शीघ्र ही गोलोकधाममें पधारेंगे। नारायणदेव तुम्हें दर्शन करेंगें। फिर कुबलयापीड़ हाथी और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10108)
- **Original**: साथ लेकर बैकुण्ठ पधारेंगे। नर-नारायण नामक मल्लोंका वध करनेके पश्चात्‌ अपने सामने राजा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10109)
- **Original**: जो दोनों ऋषि हैं, वे धर्मके घरको चले जावे कंसको देखेंगे और तत्काल उसका विध्वंस करके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10110)
- **Original**: तथा श्वेतद्वीपनिवासी विष्णु क्षीरसागरको पधारेंगे। माता-पिताकों बन्धनसे छुड़ायेंगे। तदनन्तर तुम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10111)
- **Original**: नन्द! इस प्रकार भविष्यमें होनेवाली लीलाओंका सब गोपोंकों समझा-बुझाकर लौटायेंगे। कंसके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10112)
- **Original**: वर्णन मैंने किया है। यह बेदका निश्चित मत राज्यपर उग्रसेनका अभिषेक करेंगे। कंसके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10113)
- **Original**: है। अब इस समय जिस उद्देश्यसे मेरा आना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10114)
- **Original**: * श्रीकृष्णजन्मखण्ड + 455 55% 1 4 54 5 8 $ 8 8 % # % 4 4 4 5 5 8 6 # 8 6 8424 444 44644 4844 44688 89448 888 6 # 8 588 88 68. हुआ है, उसे बताता हूँ; सुनो। माघ शुक्ल
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10115)
- **Original**: दिया। तदनन्तर मुनि अपने आसनपर विराजमान चतुर्दशीकी शुभ बेलामें इन बालकॉका संस्कार हुए और वे समागत स्त्री-पुरुष अपने-अपने करो। उस दिन गुरुवार है। रेवती नक्षत्र है। चन्द्र घरको गये। और तारा शुद्ध हैं। मीनके चन्द्रमा हैं। उसपर नन्दने आनन्दित होकर निकटवर्ती तथा लग्रेशकी पूर्ण दृष्टि है। उत्तम वणिज नामक करण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10116)
- **Original**: दूरवर्तो बन्धुजनोंके पास शीघ्र ही मड्गलपत्रिका है और मनोहर शुभ योग है। वह दिन परम
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10117)
- **Original**: पठायी। इसके बाद उन्होंने दूध, दही, घी, गुड़, दुर्लभ है। उसमें सभी उत्कृष्ट एवं उपयोगी तेल, मधु, माखन, तक्र और चीनीके शर्बतसे योगोंका उदय हुआ है। अत: पण्डितोंके साथ
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10118)
- **Original**: भरी हुई बहुत-सी नहरें लीलापूर्वक तैयार विचार करके उसी दिन प्रसन्नतापूर्वक संस्कार-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10119)
- **Original**: करायीं। इसके बाद उन्होंने अगहनीके चावलोंके कर्मका सम्पादन करो। सौ ऊँचे-ऊँचे पर्वताकार ढेर लगवाये। चिउरोंके ऐसा कह मुनीश्वर गर्ग बाहर आकर बैठ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10120)
- **Original**: सौ पर्वत, नमकके सात, शर्कराके भी सात, गये। नन्द और यशोदाको बड़ा हर्ष हुआ और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10121)
- **Original**: लड्डुओंके सात तथा पके फलोंके सोलह पर्वत वे संस्कार-कर्मके लिये तैयारी करने लगे। इसी
- **Translation**: 

---

