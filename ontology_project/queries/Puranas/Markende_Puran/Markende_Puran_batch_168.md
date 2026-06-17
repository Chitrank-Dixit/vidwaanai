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

### Verse 1 (Markende Puran 0.3341)
- **Original**: पहले जो उत्पातसूचक मेष और उल्कापात होते थे, ने सब शान्त हो गये तथा उस दैत्यके भर ज्यनेपर नदियाँ भी टीक मार्गसे बहने लगीं
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3342)
- **Original**: उस समय जशुम्भकी पृत्युके बाद सम्धूर्ण देवताओंका हृदय हर्षस्े भर गया और गजधर्वंगण मथुर गीत गाने लगे
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3343)
- **Original**: दूसरे गन्ध्वं बाजे बजाने लगे और अप्सराएँ नाचने लगीं। यत्ित्र वायु बहने लगो। सूर्थकी प्रभा उत्तम हो गयी
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3344)
- **Original**: अग्निशलाकी चुझी हुई आग अपने- आप प्रज्वलित हो उठी तथा सम्पूर्ण दिशाओंके भयडूर शब्द शानतर हो गये
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3345)
- **Original**: जि औयार्कण्फेयवृराणें ताकणिक पन्चत्ते देवीफाहात्मे जुम्भवधों कम दशमोहध्यास:
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3346)
- **Original**: 204 डवाच & अफेशशोक्र:₹, श्लोफा: 27 एफ्म 32, एक्सादित: 05054 डुस प्रकार श्रीमार्कण्डेयपुराणमें सावर्णिक मन्वन्तरकी कथाके अन्तर्गत्र देवीमाहात्म्वमें “शुम्भ-बध्च' नापक दसकाँ अश्याय पूरा हुआ
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3347)
- **Original**: >+«पश46प0-3++
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3348)
- **Original**: 330 + संक्षिप्त मार्कण्डेयपुराण + (446 &ऊ 5 क# 848 & 8 & # & #4##/4 4:44 ##& ### & ##& एकादशो5ध्याय: देवताओंद्वारा देवीकी स्तुति तथा देबीद्वारा देवताओंको बरदान ध्यान त््ववैक्तया पूरितमम्नबैतत्‌ ( बालरविद्युतिमिन्दुकिग्टां तुझकुचां नयनप्रययुक्ताम्‌। का ते स्तुति: स्तत्मपरा परोक्ति:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3349)
- **Original**: स्मेरमुखी बरदाडुक्षापाशाभीतिकरां प्रभजे भुवनेशीम्‌
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3350)
- **Original**: सर्वभूतता यदा देवी स्वर्ममुक्तिप्रदायिनी
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3351)
- **Original**: मैं भरुवनेभ्वरी देवीका ध्यान करता' हूँ। उनके
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3352)
- **Original**: त्व॑ स्तुता स्तुतये का वा भवन्तु परमोक्तय:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3353)
- **Original**: श्रीअज्ञोंकी आधा प्रभातकालके सूर्बके समान है।
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3354)
- **Original**: सर्वस्य बुद्धिरूपेण जनस्य हृदि संस्थिते। मस्‍्तकपर चन्द्रमाका मुकुट है। वे उभो हुए स्तनों
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3355)
- **Original**: स्वर्गापवर्गदे देवि नारायण नप्रोउस्तु ते
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3356)
- **Original**: और तीन नेजेंस युक्त हैं । उनके मुखपर पुसकानकी
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3357)
- **Original**: कलाकापष्ठादिरपेण. परिण्पाप्पप्रदायिनि। छटा छायी रहती हैं और हाथोंपें परदे, अछुशं, विश्वस्योपरतो शक्ते नारायण नपोउस्तु ते
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3358)
- **Original**: पाश एवं अभय-मुद्गा शीभा पातें हैं।) सर्वपडुलमदत्ये शिवरे सर्वार्थसाधिके। ऋष्िरुकान 2 1
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3359)
- **Original**: शरण्ये ज््यम्यके गौरि नागरायणि नमोस्तु ते
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3360)
- **Original**: आ0' देव्या हतें त्तत्र महासुरेन्दरे सृष्टिस्थिनिविनाशानां शक्तिभूते सनातनि। , सेन्द्रा: सुरा वदह्लिपुरोगमास्तोमं।
- **Translation**: 

---

