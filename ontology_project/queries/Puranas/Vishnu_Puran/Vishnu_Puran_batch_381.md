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

### Verse 1 (Vishnu Puran 0.7601)
- **Original**: अनन्तरं चातिशुद्धलअहोरांशकावयवोक्त कृतपुत्रजन्पलाभगुणाइयस: परिणाममुपगतापि झात्रुओंको जीत लिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7602)
- **Original**: उस समय जे समस्त जात्रुगण पुत्र, भिन्र, स्त्री, सेना और कोझादिसे हीन होकर अपने-अपने स्थानोंको खेड़कर दिशा-विदिद्ञाओंमें भाग गये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7603)
- **Original**: उनके भाग जानेपर उसने एक राजकन्याम्तरे देखा जो अत्यन्त भयसे क्यूतर हुई विशाल आँखोंसे [ देखती हुई ] 'हे तात, हे मातः, है भ्रातः ! मेरी रक्षा करो, रक्षा करो' इस प्रकार व्याकुख्तापूर्वक विस्तप कर रही थी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7604)
- **Original**: उसको देखते ही उसमें अनुरक्त-चित्त हो जानेसे राजाने वियार किया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7605)
- **Original**: “यह अच्छा ही ई मैं पुत्रहीन और वन्ध्याका पति हूँ; ऐसा मालूम होता है कि सनत्तानकी कारणरूपा इस कन्यारत्रको विधाताने ही इस समय यहाँ भेजा है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7606)
- **Original**: तो फिर मुझे इससे विवाह कर लेगा चाहिये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7607)
- **Original**: अथवा इसे अपने रथपर बैठकर अपने निवासस्थानक्व लिये चलता हूँ, बहाँ देवी दौब्याकी आज्ञा लेकर ही इससे विवाह कर रूँगा'
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7608)
- **Original**: तदनत्तर ये उसे रथपर चढ़ाकर अपने नगरको के चले
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7609)
- **Original**: वहाँ विजयी राजाके दर्शानके लिये सम्पूर्ण पुरवासी, सेवक, कुटुम्बीजन और मन्त्रिवर्गके सहित महारानी झ्ैव्या नगरके द्वारपर आयी हुई थीं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7610)
- **Original**: उसने राजाके खरामभागमें बैठी हुई राजकन्याक्रे देखकर क्रोधके कारण कुछ काँपते हुए होठोंसे कहा---
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7611)
- **Original**: “है अति चपलचित्त ! तुमने रथमें यह कौन बैठा रखी है ?”
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7612)
- **Original**: राजाको भी जब कोई उत्तर न सुझा तो अत्यन्त डरते-डरते कहा--'यह मेरी पुत्रवधू है।''
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7613)
- **Original**: तब दौव्या बोली---
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7614)
- **Original**: “मेरे तो कोई पुत्र हुआ नहीं है और आपके दूसरी कोई
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7615)
- **Original**: स्री भी नहीं है, फिर किस पुक्रके कारण आपका इससे पुत्रवधूका सम्बन्ध हुआ ?'
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7616)
- **Original**: श्रीपराह्रजी बोले--इस प्रकार, दौज्याके ईर्ष्या और क्रोघ-कल॒षित वचनोंसे विवेकहीन होकर भयके कारण कही हुई असंबद्ध बातके सन्देहक्यी दूर करनेके लिये राजाने कहा---
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7617)
- **Original**: “तुम्हारे जो पुत्र होनेबाला है उस भावी शिशु मैंने यह पहलेसे ही भार्या निश्चित कर दी है।” यह सुनकर रानौने मधुर मुसुक्नानके साथ कहा--' अच्छा, ऐसा ही हो” और राजाके साथ नगरमें प्रनेश किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7618)
- **Original**: तदनत्तर पुत्र-लाभके गुणोंसे युक्त उस अति विशुद्ध लग्न होरांशक अवयबके समय हूए पुप्रजन्मचिषयक वातांस्ख्पके प्रभावसे गर्भधारणके योग्य अवस्था न
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7619)
- **Original**: 270 जैव्या स्वल्पैरेवाहोधिर्गर्भपवाप
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7620)
- **Original**: कालेन च कुमारमजीजनत्‌
- **Translation**: 

---

