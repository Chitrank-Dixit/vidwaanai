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

### Verse 1 (Vishnu Puran 0.8481)
- **Original**: योउयं साम्प्रतमेत- द्धूमण्डलमख्ण्डितायतिधर्मेण पाल्यतीति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8482)
- **Original**: तदनन्तर, कुरुकुलके क्षीण हो जानेपर जो अश्वत्यामाके प्रहार किये हुए ब्रह्मास्रद्वारा गर्भमें ही भस्मीभूत हो चुका था किन्तु फिर, जिन्होंने अपनी इच्छासे ही माया-मानव-देह धारण किया है उन सकल सुगसुरबन्दितचरणारविन्द श्रीकृष्णचन्द्रके प्रभावसे पुनः जीबित हो गया; ठस परीक्षितने अभिमन्युके द्वारा उत्तराके गर्भसे जन्म छिया जो कि इस समय इस प्रकार धर्मपूर्वक सम्पूर्ण भूमप्डलका शासन कर रहा है कि जिससे भविष्यमें भी उसकी सम्पत्ति क्षीण न हो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8483)
- **Original**: वूूूू-- भू ल्‍ल्‍न्‍
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8484)
- **Original**: -ूू इति श्रीविष्णुपुराणे चतुर्थेडशे बिंशोडघ्याय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8485)
- **Original**: नी जब विन इक्कीसवाँ अध्याय अभविष्यमें होनेवाले राजाओंका वर्णन औफपराशर उवाच अतः पर भविष्यानहं भूपालान्कीर्तयिष्यामि
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8486)
- **Original**: योउय॑ साम्प्रतमवनीपतिः परीक्षित्तस्यापि जनमेजयश्रुतसेनोअसेनभीमसेनाअ्रत्वार: पुत्रा भविष्यन्ति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8487)
- **Original**: जनमेजयस्थापि ज्तानीको भ्रविष्यति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8488)
- **Original**: योउसौ याज्ञवल्क्याद्वेदमधीत्य कृपादस्थाण्यवाप्प विषमविषयविरक्तचित्त- वृत्तिश्न शौनकोपदेशादात्मज्ञानप्रवीण: पर निर्वाण- मवाप्स्थति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8489)
- **Original**: झातानीकादश्रमेथद्ततो भविता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8490)
- **Original**: तस्मादप्यधिसीमकृष्ण:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8491)
- **Original**: अधिसीमकृष्णात्निच्क्कु:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8492)
- **Original**: यो गड्ढयापहते हस्तिनापुरे कौशाम्ध्यां निवत््यति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8493)
- **Original**: तस्याप्युष्ण: पुत्रो भविता
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8494)
- **Original**: उष्णाद्विचित्ररथ:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8495)
- **Original**: ततः. शुचिरथः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8496)
- **Original**: तस्मादवृष्णिमास्ततस्सुषेणस्तस्यापि सुनीथस्मुनीधान्रुप्चक्षुस्तस्मादपि सुखावलःस्तस्य अ॒पारिप्नवस्ततश्च॒ सुनयस्तस्यापि मेधावी
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8497)
- **Original**: मेथधाविनो रिपुझ्अयस्ततो मृदुस्तस्माद्च तिग्मस्तस्मादब॒हद्रथो बृहद्रथाइसुदानः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8498)
- **Original**: ततो5परइशतानीक:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8499)
- **Original**: . तस्माश्चोदयन श्रीपराशरजी ओोले--अब मैं भविष्यमें होनेवाले राजाओंका वर्णन करता हूँ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8500)
- **Original**: इस समय जो परोक्षित्‌ नामक महाराज हैं इनके जनमेजय, श्रुतसेन, उग्रसेन और भीमसेन नामक चार पुत्र होंगे
- **Translation**: 

---

