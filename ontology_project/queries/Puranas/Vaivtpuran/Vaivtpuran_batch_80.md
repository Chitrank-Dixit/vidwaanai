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

### Verse 1 (Vaivtpuran 6.9411)
- **Original**: सरस्वतीने बड़ी प्रसन्नताके साथ परात्पर श्रीकृष्णका वायुसे भरकर रोके रहों। दसवाँ महीना आनेपर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9412)
- **Original**: स्तवतन किया। उस समय उनके विरहज्वरसे तुम भूतलपर प्रकट हो जाना। अपने दिव्य रूपका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9413)
- **Original**: व्याकुल तथा प्रेम-विह्लल गोपों और गोपियोंने भी परित्याग करके शिशुरूप धारण कर लेना। जब
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9414)
- **Original**: भक्तिभावसे वहाँ श्रीकृष्णको स्तुति करके उनके गर्भसे वायुके निकलनेका समय हो, तब कलावतीके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9415)
- **Original**: चरणोंमें मस्तक झुकाया। विरह-ज्वरसे कातर हुई समीप पृथ्वीपर नग्र शिशुके रूपमें गिरकर निश्चय
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9416)
- **Original**: पूर्णमनोरथा राधाने भी अपने प्राणाधिक प्रियतम ही रोना। साध्वि! तुम गोकुलमें अयोनिजा-रूपसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9417)
- **Original**: हृदयवल्लभ श्रीकृष्णका भक्तिभावसे स्तवन किया। प्रकट होओगी। मैं भी अयोनिज-रूपसे ही अपने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9418)
- **Original**: उस समय श्रीराधाके नेत्रोंमें आँसू भरे हुए थे। आपको प्रकट करूँगा; क्योंकि हम दोनोंका गर्भमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9419)
- **Original**: वे अत्यन्त दीन और भवसे व्याकुल दिखायी देती निवास होना सम्भव नहीं है। मेरे भूमिपर स्थित
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9420)
- **Original**: थीं। उन्हें इस अवस्थामें देख स्वयं श्रीहरिने होते ही पिताजी मुझे गोकुलमें पहुँचा देंगे।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9421)
- **Original**: सान्त्वना देनेके लिये यह सच्ची बात कही। वास्तवमें कंसके भयका बहाना लेकर मैं तुम्हारं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9422)
- **Original**: . श्रीकृष्ण बोले--प्राणधिके महादेवि ! सुस्थिर मा ही गोकुलमें जाऊँगा। कल्याणि! तुम वहाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9423)
- **Original**: होओ। भयका त्याग करो। जैसी तुम हो वैसा ही यशोदाके मन्दिरमें मुझ नन्दनन्दनको प्रतिदिन मैं हूँ। मेरे रहते तुम्हें क्या चिन्ता है? श्रीदामके आनन्दपूर्वक देखोगी और हृदयसे लगाओगी।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9424)
- **Original**: शापकी सत्यताके लिये कुछ समयतक (बाहारूपमें) राधिके! मेरे वरदानसे तुम्हें समयपर मेरी स्मृति मेरे साथ तुम्हारा वियोग रहेगा। तदनन्तर मैं होगी और मैं तुम्हारे साथ बृन्दाबनमें नित्य
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9425)
- **Original**: मथुरामें आ जाऊँगा। वहाँ भूतलका भार उतारना, स्वच्छन्द विहार करूँगा। सुशीला आदि जो तैंतीस
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9426)
- **Original**: माता-पिताको बन्धनसे छुड़ाना, माली, दर्जी और तुम्हारी सख्ियाँ हैं, उनके तथा अन्यान्य बहुसंख्यक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9427)
- **Original**: कुब्जाका उद्धार करना, कालयवनकों मरवाकर गोपियोंके साथ तुम गोकुलको पधारो। असंख्य
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9428)
- **Original**: मुचुकुन्दको मोक्ष देना, द्वारकाका निर्माण, राजसूय- गोपियोंकों अपने अमृतोपम एवं परिमित वाणीद्वारा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9429)
- **Original**: यज्ञका दर्शन, सोलह हजार एक सौ दस राजकन्याओंकि समझा-बुझाकर आश्वासन दे गोलोकमें ही रखकर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9430)
- **Original**: साथ विवाह करना, शत्रुओंका दमन, मित्रोंका मया चिता त्वं निर्जीवा चादृश्यो5हं त्वया बिना । त्वया बिना भवं क्तु नाल॑ सुन्दरि निश्चितम्‌
- **Translation**: 

---

