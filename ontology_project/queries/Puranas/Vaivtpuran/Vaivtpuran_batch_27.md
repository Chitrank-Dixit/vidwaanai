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

### Verse 1 (Vaivtpuran 4.8436)
- **Original**: वे भगवान्‌ श्रीकृष्ण ही अपने अंशसे पार्वती- ये सर्वशक्तिस्वरूपा हैं। जगत्‌ इन्हींसे शक्तिमान्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8437)
- **Original**: पुत्र होकर प्रकट हुए हैं। इसलिये जो मज्जलस्वरूपा, हुआ है। यहाँतक कि जो प्रकृतिसे परे और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8438)
- **Original**: कल्याणदायिनी, शिवपरायणा, मड्नलकी कारण निर्गुण हैं, वे श्रीकृष्ण भी इन्हींसे शक्तिशाली
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8439)
- **Original**: और मम़जलकी अधीश्वरी हैं; उन शिवप्रिया हुए हैं। इस शक्तिके बिना ब्रह्मा भी सृष्टिरचनामें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8440)
- **Original**: दुर्गाकी तुम हाथ जोड़ सिर झुकाकर शिवाके समर्थ नहीं हैं। हम--ब्रह्मा, विष्णु और महेश्वर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8441)
- **Original**: स्तोत्रराजद्वारा, जिसे पूर्वकालमें त्रिपुरोंके भयंकर इन्हींसे उत्पन्न हुए हैं। ट्विजवर! पूर्वकालमें जब
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8442)
- **Original**: वधके अवसरपर ब्रह्माकी प्रेरणासे शंकरजीने असुरोने देवसमुदायको अपने अधीन कर लिया
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8443)
- **Original**: स्तवन किया था, उससे स्तुति करो। तामाष्टाथा/ च. पुत्रस्य शरण... मातहरप्रिये । स्तोत्नाणां सारधूत॑ च सर्वविप्रहरं॑ परम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8444)
- **Original**: ज्ञनार्थाचको. गंश्ष॒ णश्ष॒ निर्वाणवाचक: । तयोरीशं पर ब्रह्म गणेश प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8445)
- **Original**: एकशब्द: प्रधानाधों.. दन्‍्तक्ष॒ बलवाचक: । बल॑ प्रधान सर्वस्मादेकदन्त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8446)
- **Original**: दीनार्थवाचको हेश्व रम्ब:. पालकवाचक: । परिपालक॑ दीतातां हेरम्ब॑ प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8447)
- **Original**: विपत्तिवाचकों विप्लो.. नायक: खण्डतार्थक: । विपत्खण्डनकारक॑ नमामि विप्ननायकम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8448)
- **Original**: विष्णुदतैश्.. नैवेधैर्यस्थ. लम्बोदरं॑ पुरा । पित्रा दत्तैश्ष विविधैर्वन्दे लम्बोदरं च तम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8449)
- **Original**: शूर्पकराौ च यत्कर्णी.विप्रवारणकारणी । सम्पद्दी ज्ञासरूपौ च शूर्पकर्ण नमाम्यहम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8450)
- **Original**: - बिष्णुप्रसादपुष्प॑ च यम्यूर्त्रि. मुनिदत्कम्‌ । तद्‌ गजेन्द्रवक्‍त्रयुत॑ गजवक्त्र॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8451)
- **Original**: गुहस्याग्रे . च जातोउयमाविर्भूती हरालये । वन्दे गुहाग्रज॑ देव॑ सर्वदेवाग्रपूजितम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8452)
- **Original**: एतन्नामाष्टके दुर्गे नाम्भि: संयुतं परम्‌ । पुत्रस्य पश्य वेदे च तदा कोप॑ तथा कुरू
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8453)
- **Original**: एतज्नामाष्टक॑ स्तोत्र. नातार्थसंयुतं शुभम्‌ । त़िसंध्यं यः पठेन्नित्य॑ स सुखी सर्वतों जयी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8454)
- **Original**: ततो विप्रा: पलायन्ते बैनतेयाद्‌ यथोरगा: । गणेश्वरप्रसादेन महाज्ञानी भवेद्‌ धुवम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8455)
- **Original**: पुत्रार्थी लभते पुत्र॑ भार्याथी विपुलां. स्त्रियम्‌ू । महाजड: कवीद्धक्ष विद्यावांश् भवेद्‌ ध्रुवम्‌
- **Translation**: 

---

