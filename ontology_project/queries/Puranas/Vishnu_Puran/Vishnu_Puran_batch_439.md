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

### Verse 1 (Vishnu Puran 0.8761)
- **Original**: पुरुवैशीय राजा देवापि तथा इश्ष्याकुकुस्मेत्पन्न राजा पुरु-झे दोनों अत्यन्त योगबलसम्पन्न हैं और कलाप्राममें रहते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8762)
- **Original**: सत्ययुगका आरम्भ होनेपर ये पुनः सर्व्यल्लेकोों आकर क्षत्रिय-कुलके प्रतर्तक होंगे। ले आगामी मनुवंशके ब्रीजरूप हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8763)
- **Original**: सत्ययुग, ब्रेता और द्वापर इन तीनों युगोमें इसी क्रमसे मनुपुत्र पृथिचीका भोग करते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8764)
- **Original**: फिर करियुगयें उन्हींमेंसे कोई-कोई आगामी मनुसन्तानके बीजरूपसे स्थित रहते हैं जिस प्रकार कि आजकल देवापि और पुरु हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8765)
- **Original**: इस प्रकार मैंने तुमसे सम्पूर्ण राजलंशोंका यह संक्षिप्त वर्णन कर दिया है, इनका पूर्णतया वर्णन तो सौ वर्षमें भी नहीं किया जा सकता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8766)
- **Original**: इस हेय शरीरके मोहसे अन्धे हुए ये तथा और भी ऐसे अनेक भूपतिगण हो गये हैं जिन्होंने इस पृथिवीमण्डल्क्फों अपना-अपना माना है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8767)
- **Original**: “यह पथिवरी किस प्रकार अचलभानसे मेरी, मेरे पुत्रकी अथबा मेरे वेशकी होगी ?' इसी चिन्तामें व्याकुऊ हुए इन सभी राजाओंका अन्त हो गया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8768)
- **Original**: इसी चिन्तामें डूबे रहकर इन सम्पूर्ण राजाओंके पूर्व-पूर्वतरवर्ती राजालोग चले गये और इसीमें मग्र रहकर आगामी भूषतिगण भो मुृल्यु-मुंसें चले जायैंगे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8769)
- **Original**: इस प्रकार अपनेको जीतनेके ल्थ्यि राजाओँकों अथक उद्योग करते देखकर खसुन्धरा दारत्कालीन पुष्पोके रूपसें मानो हँस रही है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8770)
- **Original**: हे मैत्रेय ! अब तुम पृथिवीके कहे हुए कुछ इलोकॉको सुनो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8771)
- **Original**: पूर्वकालमें इन्हें असित मुनिने धर्मघ्वजी राजा जनकको सुनाया था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8772)
- **Original**: श्रीकिष्णुपुराण [ अल रेड प्रधिव्युवाच कथ्मेष नरेनद्राणां मोहों ब्रुद्धिमतामपि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8773)
- **Original**: येन फेनसथर्माणोउप्यतिविश्वस्तवेतस:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8774)
- **Original**: 128 पूर्वभात्मजर्य कृत्वा जेतुपिच्छन्ति मन्तरिण: । ततो भृत्यांश्व पोराश्व जिगीषन्ते तथा रिपून
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8775)
- **Original**: 129 क्रमेणानेन जेष्यामो बय॑ पृथ्वी ससागराम्‌ । इत्यासक्तधियो मृत्यु न पश्यन्त्यविदूरगम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8776)
- **Original**: 130 समुद्रावरणं याति भूमण्डलमथों वशम्‌। कियदात्मजयस्वैतन्युक्तिरात्यजये फलम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8777)
- **Original**: 131 उत्सज्य पूर्वजा याता यां नादाय गतः पिता । ता मामतीवमूढत्वाज्जतुमिच्छन्ति पार्थिवाः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8778)
- **Original**: 132 त्ता >> प् -न चापि विग्रह: । जानतेज्यलमहिन मलादुतचेल्साक
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8779)
- **Original**: 133 पृथ्वी ममेयं सकला ममैषा म्रदन्‍्ववस्यापि च शाश्रतीयप्‌ । यो यो मृतो द्वाम्र बभूव राजा तस्य तस्य
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8780)
- **Original**: 134 वह कह तमा माँ मृत्युवश ब्रजन्तम्‌
- **Translation**: 

---

