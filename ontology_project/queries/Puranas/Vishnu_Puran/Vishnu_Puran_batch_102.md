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

### Verse 1 (Vishnu Puran 0.2021)
- **Original**: छ्र आगछ्छत दूत देवा अदिति सम्प्रविश्य वै । मन्बन्‍्तरे प्रसूमामस्तन्न: श्रेयो भवेदिति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2022)
- **Original**: 128 एचमुकत्वा तु ते सर्वे चाक्षुषस्थान्तरे मनो: । मारीचात्कश्यपाज्ञाता अदित्या दक्षकन्यया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2023)
- **Original**: 129 तत्र विष्णुश्व शक्रश्न जज्ञाते पुनरेव हि। अर्यमा चैव धाता च त्वष्टा पूषा तथैव च
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2024)
- **Original**: 130 विवस्वान्सविता चैव प्रित्रो वरुण एव च । अंशुर्भगश्चातितेजा आदित्या द्वादद स्पृता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2025)
- **Original**: 139 चाक्षुषस्यान्तरे पूर्वमासन्ये तुषिता: सुरा: । वैवस्वतेउन्तरे ते वै आदित्या द्वादह् स्मृता:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2026)
- **Original**: 132 या: सप्तविश्तिः प्रोक्ता: सोमपल्यो5थ सुक्रता: । सर्वा नक्षत्रयोगिन्यस्तत्नाम्यश्षैव ता: स्पृता:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2027)
- **Original**: 1933 तासाप्रपत्यान्यभवन्दीप्रान्यमिततेजसाम्‌ । अरिष्टनेमिपत्रीनामपत्थानीह षोड़्श
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2028)
- **Original**: 134 श्रीविष्णुपुराण [ अ" 157 “है देवणण ! आओ, हमल्त्रेग शीघ्र ही अदितिके गर्भमें प्रवेश कर इस बैवस्वत-मन्वन्तरमें जन्म लें, इसोमें हमारा हित है'
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2029)
- **Original**: इस प्रकार चाक्षुष-मन्वन्तरमें निश्चयकर उन सबने मरीचिपुत्र कक्यपजीके यहाँ दक्षकन्या अदितिके गर्भसे जन्य त्तया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2030)
- **Original**: वे अति तेजस्वी विवस्वान, सविता, मैत्र, वरुण, अशु और भग नामक द्वादश आदित्य कहरूाये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2031)
- **Original**: 130-131
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2032)
- **Original**: इस प्रकार पहले चाक्षुष-मन्वन्तरमें जो तुषित नामक देवगण थे वे ही वैवस्वत-मन्वन्तरमें द्वादश आदित्य हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2033)
- **Original**: सोमको जिन सत्ताईस सुश्नता पत्रियोंके विषयमें पहले कह चुके हैं ने सन नक्षत्रयोगिनी हैं और उन नामोंसे ही बिख्यात हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2034)
- **Original**: उन अति तेजस्विनियोंसे अनेक प्रतिभागाल्ल पुत्र उत्पन्न हुए। अरिष्टनेमिको पत्नियोंके सोलह पुत्र हुए। बुद्धिमान्‌ बहुपुत्रकी भार्या [ कपिल्ा, अतिस्योहिता, पीता और अदिता * नामक ] चार प्रकाफकी खिधुत्‌ कही. जाती हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2035)
- **Original**: 134-135
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2036)
- **Original**: बहुपुत्रस्य विदुषश्नतस्नो विद्युत: स्मृता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2037)
- **Original**: ऋह्र्पियोंसे सत्कृत ऋचाओके अभिमानी देवश्रेषठ प्रत्यड्रिस्सजा: श्रेष्ठा ऋचो ब्रह्मर्षिसत्कृता: । कृशाश्रस्य तु देवरषेदिवप्रहरणा: स्मृता:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2038)
- **Original**: 136 एते युगसहस्रान्ते जायन्ते पुनरेव हि। प्रत्यक्चिरासे उत्पन्न हुए हैं तथा झास्तरोके अभिमानी देवप्रहरण नामक देवगण देवर्षि कृशाश्चकी सन्तान कहे जाते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2039)
- **Original**: हे तात । [ आठ बसु, ग्यारह रूद्र, खारह आदिस्य, प्रजापति और वषट्कार ] ये तैंतीस वेदोक्त सर्वे देवगणास्तात त्रयख्त्रिंशत्तु छन्दजा:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2040)
- **Original**: देवता अपनी इच्छानुसार जन्म लेनेवाले है। कहते हैं, इस तेषामपीह सतत निरोधोत्पत्तिरुच्यते
- **Translation**: 

---

