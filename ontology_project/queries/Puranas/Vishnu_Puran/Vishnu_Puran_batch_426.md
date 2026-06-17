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

### Verse 1 (Vishnu Puran 0.8501)
- **Original**: जनमेजयक्म पुत्र शतानीक होगा जो याज्ञवल्क्यसे वेदाध्ययनकर, कृपसे दास्त्रविद्या प्राप्तकर विषम विषयोंसे जिरक्तचित्त हो महर्षि ज्ञौनकके उपदेशसे आत्मज्ञानमें निपुण होकर परमनिर्वाण- पद प्राप्त करेगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8502)
- **Original**: झातानौकका पूत्र अश्वमेधदत्त होगा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8503)
- **Original**: उसके मधिसीमकृष्ण तथा अधिसीमकृष्णके निचक्रु नामक पुत्र होगा जो कि गज्जलजीद्वारा हस्तिनापुरके बहा ले जानेपर कौशञाम्बोपुरीमें निजास करेगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8504)
- **Original**: नियक्रुका पुत्र उष्ण होगा, उष्णका बिचित्ररथ, विचित्ररथका शुचिरथ, झुचिस्थका वृष्णिमान्‌, वृष्णियानका सुषरेण, सुधेणका सुनीथ, सुनीथका नृप, नृपका चक्षु, चक्षुका सुख्वालल, सुखाबलका पारिप्रज, पारिप्ठवका सुनय, सुनयकत्र मेधावी, मेधायीका रिपुशञ्नय, रिपुक्रयका मृदु, मुदुका तिग्म, तिम्मका बृहृद्रथ, बुहद्रथका वसुदान, वसुदानका दूसरा झातानीक, शतानीकका
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8505)
- **Original**: 296 श्रीविष्णुपुराण [ अ9ए 22 उदयनादड्डीनरस्ततश्षल॒ दण्डपाणिस्ततो निरमिन्नः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8506)
- **Original**: तस्माश्च क्षेमक:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8507)
- **Original**: अत्राय्य॑ इलोक:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8508)
- **Original**: ब्रह्मक्षत्रस्य यो योनिर्वश्ो राजर्घिसत्कृत: । क्षेमकं प्राप्य राजान॑ संस्थान प्राप्स्यते कलम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8509)
- **Original**: 18 दण्डपाणिका निरमित्र तथा निरमित्रका पुत्र श्ठेमक होगा । इस विषयमें यह इल्जेक प्रसिद्ध है---
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8510)
- **Original**: “जो वंज्ञ बाह्मण और क्षत्रियोंकी उत्पत्तिका कारणरूप तथा नाना या्जर्पियॉसे सभाजित है वह कलियुगमें राजा क्षेमक्े उत्पन्न होनेपर समाप्त हो जायगा'
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8511)
- **Original**: नततत औ कतचतः इति श्रीविष्णुपुराणे चतुर्थेउशे एकविशोउ्ध्याय:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8512)
- **Original**: जज: है $ ता ++ बाईसवाँ अध्याय भकिष्यमें होनेबाल्े इक्ष्वाकुवंशीय राजाओंका वर्णन औपराइशार उकतत अतकश्चेक्षाषकवों भविष्या: पार्थिवा: कथ्यन्ते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8513)
- **Original**: बृहद्लस्य पुत्रों बृहत्क्षण:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8514)
- **Original**: तस्मादुरुक्षयस्तस्माध॒ वत्सव्यूहस्ततश्च॒ प्रति- व्योमस्तस्मादपि दिवाकरः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8515)
- **Original**: तस्मात्सहदेव: सहदेबादबृहृदश्वस्तत्सूनुर्भानुरथस्तस्य च प्रतीताश्च- स्तस्यापि सुप्रतीकस्ततश्च॒ मरुदेवस्ततः सुनक्षत्रस्तस्मात्किन्नरः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8516)
- **Original**: किन्नरादत्तरिक्ष स्तस्मात्सुपर्णस्ततश्चामित्रजित्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8517)
- **Original**: . ततश्च बृहद्राजस्तस्थापि धर्मी धर्मिण: कृत्य:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8518)
- **Original**: कृतझयाद्रणझ्यः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8519)
- **Original**: . रणज्यात्सझय- स्तस्माच्छाक्यश्शाक्याच्छुद्धोदनस्तस्माद्राहुल- सतत: प्रसेनजित्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8520)
- **Original**: ततश्न क्षुद्रकस्ततश् कुण्डकस्तस्मादपि सुरथ:
- **Translation**: 

---

