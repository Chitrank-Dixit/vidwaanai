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

### Verse 1 (Vishnu Puran 0.4701)
- **Original**: 148 छ &9>जऊ>अ अ अविष्णपुराण ॑॑॑॑ आर 68 त्तेषामिन्द्रश्तन भविता शान्तिर्नाम महायल: । सप्तर्षयो भविष्यन्ति ये तथा ताउछणुप्न है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4702)
- **Original**: 26 हविष्पान्सुकृतस्सत्यस्तपोमूर्तिस्तथापर: .। नाभागो5प्रतिमौजाश्र सत्यकेतुस्तयैव च
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4703)
- **Original**: 27 सुक्षेत्रभोत्तरौजाश॒ भूरिषेणादयो दश। ब्रह्मसावर्णिपुत्रास्तु रक्षिष्यन्ति वसुन्धराम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4704)
- **Original**: 28 एकादशश्न भविता धर्मसावर्णिको मनुः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4705)
- **Original**: 29 विहड्वममा: कामगमा निर्वाणरतयस्तथा । गणास्त्वेते तदा मुख्या देवानां च भविष्यताम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4706)
- **Original**: एकैकस्ब्रिंशकस्तेषां गणश्रेन्रकश्ष वे वृष:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4707)
- **Original**: 30 निःस्वस्श्ाभितेजाश वपुष्मान्धृणिरारुणि: । हविष्माननघश्चैव भाव्या: सप्तर्षयस्तथा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4708)
- **Original**: 39 सर्वत्रगस्सुधर्मा चर देवानीकादयस्तथा । भविष्यन्ति मनोस्तस्य तनयाः पृथिवीश्वरा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4709)
- **Original**: 32 रुद्रपुत्नस्तु सावर्णिभविता द्वादशों मनुः। ऋतुथामा च तत्रेन्द्रो भविता श्रूणु मे सुरान्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4710)
- **Original**: 33 हरिता रोहिता देवास्तथा सुमनसो द्विज । सुकर्माण: सुरापाश्च दशका: पञ्न वै गणा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4711)
- **Original**: 34 तपोधृतिश्युतिश्लान्य: सप्तमस्तु तपोधनः । सप्रर्षयस्त्विपे तस्य पुत्रानपि निबोध में
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4712)
- **Original**: 35 देववानुपदेवअ देवश्रेष्टादयस्तथा । मनोस्तस्थ महाबीर्या भविष्यन्ति महानूपा: । 36 त्रयोदशो रुचिर्नामा भविष्यति मुने मनुः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4713)
- **Original**: 37 सुत्नामाण: सुकर्माण: सुधर्माणस्तथामरा: । त्रवर्खिशद्विभेदास्ते देवानां यत्र वे गणा:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4714)
- **Original**: 38 दिवस्पतिर्महावोर्यस्तेषामिन्द्रों भविष्यति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4715)
- **Original**: 39 निर्मोहस्तत्त्वदर्शी च निष्प्रकम्प्यो निरुत्सुक: । धृतिमानव्यवश्षान्यस्सप्तमस्सुतपा मुनि: । सप्रर्षयस्त्वमी तस्य पुत्रनानपि निबोध में
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4716)
- **Original**: 40 चित्रसेनविचित्राद्मया भविष्यन्ति पहीक्षितः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4717)
- **Original**: 49 (अ0 2 सुधामा और विशुद्ध नामक सौ-सौ देवताओंके दो गण होगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4718)
- **Original**: महाबलखान्‌ दाक्ति उनका इन्द्र होगा तथा उस समय जो सप्तर्षिगण होंगे उनके नाम सुनो---
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4719)
- **Original**: उनके नाम हविष्पान्‌, सुकृत, सत्य, तपोसूर्ति, नाभाग, अप्रतिमौजा और सत्यकेतु हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4720)
- **Original**: उस समय त्रह्मसावर्णिमनुके सुक्षेत्र, उत्तमौजा और भूरिषेण आदि दस पुत्र पृथिज्ीकी रक्षा करेंगे
- **Translation**: 

---

