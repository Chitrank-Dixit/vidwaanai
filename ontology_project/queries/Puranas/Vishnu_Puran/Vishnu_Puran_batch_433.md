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

### Verse 1 (Vishnu Puran 0.8641)
- **Original**: इनके उच्छिन्न होनेपर कैंकिल नामक यवनजातीय अभिषेकरहित राजा झोंगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8642)
- **Original**: 300 श्रीविष्णुपुराण [ अ0 र4 तेषामपत्य॑ विन्ध्यशक्तिस्तत: पुरझबस्तस्मा-
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8643)
- **Original**: उनका वेशघर विन्ध्यशक्ति डोगा। विन्ध्यशक्तिका पुत्र द्रामचन्द्रस्तस्माद्धर्मवर्मा ततो वड्जस्ततो5भून्नन्दन- स्ततस्सुनन्दी तदभ्राता नन्दियश्ञाइशुक्र: प्रवीर एते वर्षशर्त षड़वर्षाणि भूषतयो भविष्यन्ति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8644)
- **Original**: ततस्तत्पुत्रास्रयोदकैते बाह्िकाश्न त्रय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8645)
- **Original**: ततः पुष्पमित्रा: पदुमित्रास्रयोदशैकलाअ्र सप्नाश्रां:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8646)
- **Original**: ततश्न कोशलायां तु नव चैव भूपतयो भ्रविष्यन्ति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8647)
- **Original**: नैषथास्तु तएवं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8648)
- **Original**: मगधायां तु विश्वस्फटिकसंज्ञो5न्यान्वर्णा- न्करिष्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8649)
- **Original**: । कैवर्त्तवदुपुलिन्द- ब्राह्मणान्राज्ये स्थापयिष्यति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8650)
- **Original**: उत्साद्याखिलक्षत्रजाति नव नागा: पद्मावत्यां नाम पुर्यामनुगड्राप्रयाग॑ गयायाज्ञ मागधा गुप्ताश्न भोक्ष्यन्ति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8651)
- **Original**: कोशलाअपुण्डूताग्रलिप्त- समुद्गरतटपुरी चर देवरक्षितो रक्षिता
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8652)
- **Original**: भोक्ष्यन्ति भोक्ष्यन्ति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8653)
- **Original**: भोक्ष्यति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8654)
- **Original**: सौराष्ट्रावन्तिशुद्रा भीराज्नर्मदा- मरुभूविषयांश्न ब्रात्यद्विजाभीरशद्राद्मा भोक्ष्यन्ति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8655)
- **Original**: सिन्धुतटदाविकोर्वीचन्द्रभागा- काइमीरविषयांश् ओ्रोक्ष्यन्ति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8656)
- **Original**: एते क् तुल्यकालास्सवें पृथिव्यां भूभुजो भविष्यन्ति
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8657)
- **Original**: अल्पप्रसादा बृहत्कोपा- स्सर्वकालमनृताधर्मरुतय: सत्रीबालगोवधकर्त्तार: परस्वादानरुचयो5ल्‍्पसारास्तमिस्रप्राया उदिता- स्तमितप्राया अल्पायुषो महेच्छा ह्ाल्पधर्मा लुग्याश्व भविष्यन्ति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8658)
- **Original**: तैश्व विमिश्रा जनपदास्तच्छीलानुवर्त्तिने._ राजाश्रयश्ुष्पिणो प्लेच्छाक्षार्याश्ष॒बिपर्ययेण वर्त्तमाना: प्रजा: क्षपयिष्यन्ति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8659)
- **Original**: परदात्मणिधान्यकवंशा पुरकय होगा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8660)
- **Original**: पुरकृयका रामचन्द्र, रामचरद्रका धर्मवर्मा, घर्मवर्माका वेग, बंगका नन्‍्दन तथा नन्दनका पुत्र सुनन्‍दी होगा। सुनन्‍्दीके नन्दियशा, झुक्र और प्रवीर ये तीन भाई होंगे। ये सब्र एक सौ छः वर्ष राज्य करेंगे
- **Translation**: 

---

