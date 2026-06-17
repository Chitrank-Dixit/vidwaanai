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

### Verse 1 (Vaivtpuran 55.5225)
- **Original**: तुम्हारा स्वरूप है। तुम वास्तवमें निराकार हो। श्रीकृष्णकी आज्ञासे पुष्करमें श्रीराधाकी पूजा की
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.5226)
- **Original**: भक्तोंपर अनुग्रह करनेके लिये ही तुम रूप धारण और उसके प्रभावसे तुम्हें प्राप्त किया। पतिब्रता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.5227)
- **Original**: करती हो। भक्तोंकी विभिन्न रुचिके कारण नाना श्रीराधाकी पूजा करके उनके दिये हुए वरसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.5228)
- **Original**: प्रकारकी मूर्तियाँ ग्रहण करती हो। वैकुण्ठमें कामदेवने रतिको, धर्मदेवने सती साध्वी मूर्तिको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.5229)
- **Original**: महालक्ष्मी और सरस्वतीके रूपमें तुम्हारा ही तथा देवताओं और मुनियोंने धर्म, अर्थ, काम एवं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.5230)
- **Original**: निवास है। पुण्यक्षेत्र भारतवर्षमें सत्पुरुषोंकी मोक्षको प्राप्त किया था। इस प्रकार मैंने श्रीराधाकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.5231)
- **Original**: जननी भी तुम्हीं हो। सती और पार्वतीके रूपमें पूजाका विधान बताया है। अब स्तोत्र सुनो।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.5232)
- **Original**: तुम्हारा ही प्राकटय हुआ है। तुम्हीं पुण्यरूपा एक बार श्रीराधाजी मान करके श्रीकृष्णके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.5233)
- **Original**: तुलसी और भुवनपावनी गड्ज़ा हो। ब्रह्मलोकमें समीपसे अन्तर्धान हो गयीं। तब ब्रह्मा, विष्णु
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.5234)
- **Original**: सावित्रीके रूपमें तुम्हीं रहती हो। तुम्हीं अपनी और शिव आदि सब देवता ऐश्वर्यभ्रष्ट, श्रीहीन,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.5235)
- **Original**: कलासे वसुन्धरा हुई हो, गोलोकमें तुम्हीं समस्त भार्यारहित तथा उपद्रवग्रस्त हो गये। इस
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.5236)
- **Original**: गोपालोंकी अधीश्वरी राधा हो। तुम्हारे बिना मैं परिस्थितिपर विचार करके उन सबने भगवान्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.5237)
- **Original**: निर्जीव हूँ। किसी भी कर्मको करनेमें असमर्थ श्रीकृष्णकी शरण ली। उनके स्तोत्रसे संतुष्ट हुए
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.5238)
- **Original**: हूँ। तुम्हें शक्तिके रूपमें पाकर ही शिव शक्तिमान्‌ सबके परमात्मा श्रीकृष्णने स्नान करके शुद्ध हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.5239)
- **Original**: हैं। तुम्हारे बिना वे शिव नहीं, शब हैं। तुम्हें ही सती राधिकाकी पूजा करके उनका इस प्रकार
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.5240)
- **Original**: बेदमाता सावित्रीके रूपमें अपने साथ पाकर स्तवन किया। साक्षात्‌ ब्रह्माजी बेदोंके प्राकट्यकर्ता माने गये हैं। श्रीकृष्ण बोले--सुमुखि श्रीराधे! कया मैं
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.5241)
- **Original**: तुम लक्ष्मीका सहयोग मिलनेसे ही जगत्पालक इसी प्रकार तुम्हारा प्रिय हूँ और मुझमें तुम्हारी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.5242)
- **Original**: नारायण जगत्‌का पालन करते हैं। तुम्हीं दक्षिणारूपसे प्रीति है? तुम्हारी वाणीमें जो छलना थी, वह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.5243)
- **Original**: साथ रहती हो, इसलिये यज्ञ फल देता है। आज अच्छी तरह प्रकट हो गयी। ' हे कृष्ण! तुम
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.5244)
- **Original**: पृथ्वीके रूपमें तुम्हें मस्तकपर धारण करके ही मेरे प्राण हो, जीवात्मा हो' इस तरहकी बातें जो
- **Translation**: 

---

