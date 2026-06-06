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

### Verse 1 (Vishnu Puran 0.12221)
- **Original**: यारह मासका एक वर्ष होता है, देवलोकमें यही एक दिन-रात होता है । ऐसे तीन सौ साठ नर्षोंक्र देजताओंका एक यर्ष होता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12222)
- **Original**: ऐसे जारह हजार दिग्य वर्षोका एक चतुर्युग होता है और एक हजार चतुर्युगका ब्रह्माका एक दिन होता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12223)
- **Original**: हे महामुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12224)
- **Original**: यही एक कल्प है। इसमें चौदह मनु जीत जाते हैं । हे मैत्रेय ! इसके अन्तमों ब्रह्माका नैमित्तिक प्रकय होता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12225)
- **Original**: हे मैत्रेव ! सुनो, मैं उस नैमित्तिक प्ररूयका अत्यन्त भयानक रूप वर्णन करता हूँ। इसके पीछे मैं तुमसे प्राकृत प्रक्यका भी वर्णन करूँगा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12226)
- **Original**: एक सहख्र चतुर्युग बीतनेपर जब पृथिवी क्षीणप्राय हो जाती है तो सौ वर्षतक अति घोर अनावृष्टि होती है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12227)
- **Original**: हे मुनिश्रेष्ठ ! उस समय जो पार्थिव जीव अल्प गक्तिचाले होते हैं वे सब अनावृष्टिसे पीड़ित होकर सर्वचा नष्ट हो जाते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12228)
- **Original**: तदनन्तर, रुद्ररूपधारी अव्ययात्मा भगयान्‌ विष्णु संसास्का क्षय करनेके लिये सम्पूर्ण प्रजाको अपनेमें लीन कर लेनेका प्रयत्न करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12229)
- **Original**: है मुनिसत्तम ! उस समय भगवान्‌ विष्णु सूर्यकी सातों किरणोंमें स्थित होकर सम्पूर्ण जलको सोख छेते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12230)
- **Original**: हे मैत्रेय ! इस प्रकार प्राणियों तथा पृथिवीके अन्तर्गत सम्पूर्ण जलक्ये सोख्ककर वे समस्त भूमण्डलको शुष्क कर देते हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12231)
- **Original**: समुद्र तथा नदियोंमें, पर्वतीय सरिताओं और ख्रोतोंमें तथा विभिन्न पाताछोंमें जितना जल है वे उस सबको सुखा डालते है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12232)
- **Original**: तय भगवानके प्रभावसे प्रभावित होकर तथा जलपानसे पुष्ट होकर वे सातें सूर्यरद्षिमयाँ सात सूर्य हो जाती हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12233)
- **Original**: है ट्विज ! उस समय ऊपर-नीचे सब ओर देदीप्यमान होकर वे सातों सूर्य पाताल्पर्यन्त सम्पूर्ण त्रिलोकीको भस्म कर डालते है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12234)
- **Original**: हे द्विज ! उन प्रदीक्त भास्करोंसे दग्ध हुई त्रित्लेकी पर्वत, नदी और समुद्रादिके सहित सर्वथा नीरस हो जाती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12235)
- **Original**: उस समय रप्पूर्ण त्रिलोकीके वृक्ष और जल-आदिके दग्ध हो जानेसे यह पृथित्री कछुणकी पीठके समान कठोर हो जाती है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12236)
- **Original**: डेज्षे2 शेषाहिशाससम्भूत: पातालानि दहत्यध:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12237)
- **Original**: 24 पातालानि समस्तानि स दग्ध्वा ज्वलनो महान्‌ । भूमिमभ्येत्य सकलं बभस्ति वसुधातलम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12238)
- **Original**: 25 भुव्लोंक॑ ततस्सव॑ स्वलॉक चर सुदारूण: । ज्वालामालामहावर्तस्तत्रैेव. परिवर्तते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12239)
- **Original**: 26 अम्बरीषमिवाभाति तैलोक्यमखिलं; तदा। ज्वालावर्तपरीवारमुपक्षीणचराचरप्‌.
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12240)
- **Original**: 27 लोकद्दयनिवासिन: । कृताधिकारा गच्छन्ति महलोंक॑ महामुने
- **Translation**: 

---

