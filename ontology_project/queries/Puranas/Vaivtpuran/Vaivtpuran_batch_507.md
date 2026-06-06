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

### Verse 1 (Vaivtpuran 29.7338)
- **Original**: मेरे लिये एक श्रेष्ठ पुत्रके समान हुए; अतः मैं “>अ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 29.7339)
- **Original**: तुम्हें ऐसा गुहा मन्त्र प्रदान करूँगा, जो त्रिलोकीमें 825 ,6
- **Translation**: 

---

### Verse 3 (Vaivtpuran 29.7340)
- **Original**: 346 5 _
- **Translation**: 

---

### Verse 4 (Vaivtpuran 29.7341)
- **Original**: दुर्लभ है। इसी प्रकार एक ऐसा परम अद्भुत घटना बिस्तारसे सुनाकर परशुरामने कहा कि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 29.7342)
- **Original**: कवच बतलाऊँगा, जिसे धारण करके तुम मेरी मैंने पृथ्वीको इक्कीस बार क्षत्रियशून्य करने तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 29.7343)
- **Original**: कृपासे अनायास ही कार्तवीर्यका वध कर डालोगे। मेरे पिताका वध करनेवाले कार्तबीर्यको मारनेकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 29.7344)
- **Original**: विप्रवर ! तुम इक्कोस बार पृथ्वीको भूपालोंसे शून्य प्रतिज्ञा की है। आप मेरी प्रतिज्ञाको पूर्ण करें। भी कर दोगे और सारे जगत्में तुम्हारी कोर्ति यमाकाशमिवाद्यन्तमध्यही न तथाव्ययम्‌ । विश्वतन्त्रमतन्‍त्र॑ च स्वतन्त्र तन्त्रबीजकम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 29.7345)
- **Original**: ध्यानासाध्य॑ दुराशध्यमतिसाध्य॑ कृपानिधिम्‌ । त्राहि मां करुणासिन्थो दीनबन्धो5तिदीनकम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 29.7346)
- **Original**: अद्य मे सफलं जन्य जीवित च सुजीवितम्‌ । स्वप्रादृष्ट च भक्तानां पश्यामि चक्षुपाधुना
- **Translation**: 

---

### Verse 10 (Vaivtpuran 29.7347)
- **Original**: शक्रादय: सुरगणा: कलया यस्य सम्भवा: । चराचरा: कलांशेन त॑ नमामि महेश्वरम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 29.7348)
- **Original**: ये भास्करस्वरूप॑ च शशिरूप॑ हुताशनम्‌ । जलरूपं॑ वायुरूपं त॑ नमामि महेश्वरम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 29.7349)
- **Original**: स्त्रीरूप॑ क्‍्लीबरूपं च पुंरूष च ब्रिभर्ति य: । सर्वाधार॑ सर्वरूप॑ त॑ नमामि महेश्वरम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 29.7350)
- **Original**: देव्या फकठोरतपसा यो लब्धों गिरिकन्यया
- **Translation**: 

---

### Verse 14 (Vaivtpuran 29.7351)
- **Original**: दुर्लभस्तपसां यो हि. त॑ नमामि महेश्वरम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 29.7352)
- **Original**: सर्वेधषां कल्पवृक्ष॑ च वाज्छाधिकफलप्रदम्‌ । आशुतोष भक्तबन्धु॑त॑ नमामि महेश्वरम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 29.7353)
- **Original**: अनन्तविश्वसृष्टीनां संहर्तारे भयंकरम्‌ । क्षणेन लीलामात्रेण त॑ नमामि महेश्वरम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 29.7354)
- **Original**: यः काल: कालकालक्ष कालबीज॑च कालज: । अज: प्रजश्व॒यः सर्वस्तं॑ नमामि महेश्वरम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 29.7355)
- **Original**: इत्येबमुक्ला स॒ भृगु: पपात चरणाम्बुजे। आशिष॑ च ददी तस्मै सुप्रसन्नो बभूब सः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 29.7356)
- **Original**: जामदग्न्यकृतं स्तोत्र यः पठेदू भक्तिसंयुत: । सर्वपापविनिर्मुकछ: शिवलोक॑ स॒ गच्छति
- **Translation**: 

---

### Verse 20 (Vaivtpuran 29.7357)
- **Original**: (गणपतिखण्ड 29। 43-57)
- **Translation**: 

---

