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

### Verse 1 (Garuda1 0.181)
- **Original**: सुवर्णवर्णवां झ्षव सुवणाख्यस्तथैव च्च। सुबर्णावयवश्चैव सुबर्ण: स्वर्णमेखल:
- **Translation**: 

---

### Verse 2 (Garuda1 0.182)
- **Original**: सुवर्णस्य प्रदाता च सुवर्णेशस्तथव ( सुव्र्णाशस्तथत च ) च। सुवर्णस्थ प्रियक्षेक सुबर्णाकास्तथैव॒ च
- **Translation**: 

---

### Verse 3 (Garuda1 0.183)
- **Original**: सुपर्णी च महापर्णी सुपर्णस्य च कारणम्‌। वैनतेयस्तशादित्य. आदिरादिकरः शिवः:
- **Translation**: 

---

### Verse 4 (Garuda1 0.184)
- **Original**: कारणं महत्व प्रथाजस्थ चल कारणम्‌। शुद्धीतां कारण चैय कारण पनसस्तथा
- **Translation**: 

---

### Verse 5 (Garuda1 0.185)
- **Original**: __मालाधरो महादेवो महादेवेन पूजित। कारण चेतसश्षेय आहड्भास्‍स्थ कारणम। _ 6-पानतवों पनुजलैबव0। 2-पातार्य: पर0।
- **Translation**: 

---

### Verse 6 (Garuda1 0.186)
- **Original**: आचारकाण्ड ] * विष्णुसहस्वनाम + 37 &%4%#ऋ##ऋ#ऋकऋऋऋ कक कक आभआ ऋऋ कफ फऋक # कक # 7 कक कक फऋऋ ऋऋफऋफ़ऋफऋककककअक्लाआओआआआआआ कफ कक आक आआआआ कक #ऋ कफ कक काक्ाक काका कक भूतातां कारण॑ तहत कारण च॑ विभावसो:
- **Translation**: 

---

### Verse 7 (Garuda1 0.187)
- **Original**: आकाशकारणं तद्गत्‌ पृश्चिव्या: कारण परम्‌। आण्डस्प कारण॑ चैय ॒प्रकृते: “कारणं तथा
- **Translation**: 

---

### Verse 8 (Garuda1 0.188)
- **Original**: देहस्य कारणं अचव चक्षुकक्षैकः कारणम्‌। ओबतरस्य कारण तद्गत्‌ू कारणं क्ष त्वचस्तथा
- **Translation**: 

---

### Verse 9 (Garuda1 0.189)
- **Original**: जिह्डाया: कारण चैय प्राणस्यैठ त्ञ कारणप्‌। हस्तयो: कारण तद्घत्‌ पादयो: कारण तथा
- **Translation**: 

---

### Verse 10 (Garuda1 0.190)
- **Original**: याचश्न कारण तद्धत्‌ पायोञ्जैव तु कारणप्‌। इन्द्स्‍स्यम कारण चैव कुबेरस्थ च कारणम्‌
- **Translation**: 

---

### Verse 11 (Garuda1 0.191)
- **Original**: अमस्य कारणं चैव ईशानस्थ च॒ कारणम्‌। यक्षाणां कारणं चैव रक्षसां कारणं परम्‌
- **Translation**: 

---

### Verse 12 (Garuda1 0.192)
- **Original**: जृपाणां कारण श्रेष्ठ धर्मस्थयैथ तु कारणम्‌। जन्तूनां कारणं चैव वसून्रां कारण परम्‌
- **Translation**: 

---

### Verse 13 (Garuda1 0.193)
- **Original**: मनूनां कारणं चैव पक्षिणां कारण परम्‌। मुत्तीतां कारण श्रेष्ठ योगिनां कारणं परम्‌
- **Translation**: 

---

### Verse 14 (Garuda1 0.194)
- **Original**: प्रिद्धानां कारण चैव यक्षाणां कारणं परम्‌। कारण॑ किनतराणां च गश्धर्वाणां क्ष कारणम्‌
- **Translation**: 

---

### Verse 15 (Garuda1 0.195)
- **Original**: नदानां कारण अैव नदीनां कारणम्‌ परम्‌। कारणं उ पस़मुद्राणां वृक्षाणां कारणं॑ तथा
- **Translation**: 

---

### Verse 16 (Garuda1 0.196)
- **Original**: कारणं वीरुधां चैव लोकानां कारण तथा। पातालकारणं चैंव देवानां कारण तथा
- **Translation**: 

---

### Verse 17 (Garuda1 0.197)
- **Original**: सर्पाणां कारण चैव श्रेयसाँ कारणं तथा। पशूनां कारण च्ैव सर्वेषां कारण तथा
- **Translation**: 

---

### Verse 18 (Garuda1 0.198)
- **Original**: देहात्या चेन्तनियात्पा च आत्मा बुद्धिस्तश्ैव उ। प्रगसभ् जथैयात्पा चार्माहड्डारचेतस:*
- **Translation**: 

---

### Verse 19 (Garuda1 0.199)
- **Original**: जाग्रतः स्वपतश्चात्मा महदात्या परस्तथा। प्रधावस्थ परात्मा थ॑ आकाशात्मा ह्वार्पा ज़शा
- **Translation**: 

---

### Verse 20 (Garuda1 0.200)
- **Original**: प्ृ्चित्या: परमात्मा थ॑ रसस्यात्मा तथैव चना गन्धस्थ पंरमात्या लछ॒ रूपस्थात्मा परस्तथा
- **Translation**: 

---

