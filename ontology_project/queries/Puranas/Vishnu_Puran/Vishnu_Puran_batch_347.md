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

### Verse 1 (Vishnu Puran 0.6921)
- **Original**: तब ब्राह्मणीने अत्यन्त क्रोाधित होकर राजाको शाप दिया--
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6922)
- **Original**: 'ओरे ! तूने मेंरे अतृप्त रहते हुए भी इस अ्रकार मेरे पतिको खा लिया, इसलिये कामोपभोगमें प्रवृत्त होते ही तेरा अन्त हो जायगा'
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6923)
- **Original**: इस प्रकार शाप देकर वह अम्रिमें प्रथिष्ट हों गयी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6924)
- **Original**: तदनन्तर बारह वर्षके अन्तमें शापमुक्त हो जानेपर एक दिन थिषय कामसामें प्रवुत्त होनेपर रानी मदयन्तीने उसे ब्राह्मणीके शापका स्मरण करा दिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6925)
- **Original**: ] चतुर्थ अंझ रडर ततः परमसौ स्त्रीभोगं तत्याज
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6926)
- **Original**: बसिष्ठ- श्वापुत्रेण राज़ा पुत्रार्थमभ्यर्थितो मदयच्त्यां गर्भाधान॑ चकार
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6927)
- **Original**: यदा च सप्तवर्षाण्यसौ गर्भो न जन्ने ततस्तं गर्भभइमना सा देवी जघान
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6928)
- **Original**: पुत्रश्नाजायत
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6929)
- **Original**: तस्थ चाइमक इत्येव नामाभवत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6930)
- **Original**: अद्मकस्य मूलको नाम पुत्रोभवत्‌ । 73
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6931)
- **Original**: . योउसौ... निःश्षत्रे क्ष्मातलेउस्मिन्‌. क्रियमाणे स्त्रीभिर्विवश्लाभि: परिवार्य रक्षितस्ततस्तं नारोकवचमुदाहरन्ति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6932)
- **Original**: मूलकाइशरथस्तस्मादिलिविलस्ततश्र विश्वसह:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6933)
- **Original**: तस्माश्च खदबाड़ी योउसौ देवासुरसक्मामे देवैरभ्यर्थितो5सुराझघान
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6934)
- **Original**: स्वग्गें च कृतप्रियैर्देवैर्वरग्रहणाय चोदित: प्राह
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6935)
- **Original**: यहावहय वरो ग्राह्मस्तन्ममायुः कथ्यतामिति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6936)
- **Original**: अनत्तरं च॒ तैरुक्ते एकमुहूर्तप्रमाण॑ तवायुरित्युक्तो5थास्खलित- गतिना विमानेन लघिमगुणों मर्त्यलोकमागम्ये- दमाह
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6937)
- **Original**: यथा न ब्राह्मणेभ्यस्सकाशा- दात्मापि मे प्रियतरो न च॒ स्वधर्मोल्लड्ड्न मया सत्तामात्रात्मन्यात्पान॑ परमात्मनि वासुदेवाख्ये युयोज तत्रैव च लयमवाप
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6938)
- **Original**: अत्रापि श्रूयते इल्लोको गीतस्सप्तर्षिभि: पुरा । खदताड़्रेन समो नान्‍्य: कश्निदुर्व्या भविष्यति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6939)
- **Original**: 89 येन स्वर्गादिहागम्य मुहूत्त प्राप्प जीवितम्‌ । त्रयोअभिसंहिता छोका सुद्धया सत्येन चैव हि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6940)
- **Original**: 82 खटवाड्भादीर्घयाहु: पुत्रो3भवत्‌
- **Translation**: 

---

