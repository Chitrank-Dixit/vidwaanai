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

### Verse 1 (Vishnu Puran 0.8101)
- **Original**: इस प्रकार इस सम्पूर्ण रहस्यका मैंने तुमसे वर्णन किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8102)
- **Original**: अहो ! थे भगवान्‌ तो द्रेषानुबके कारण भी कीर्तन और स्मरण करनेसे सम्पूर्ण देकता और असुरोंको
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8103)
- **Original**: शा छछछछछ इसलजचतर्थअंश झ 285 बसुदेवस्थ त्वानकदुन्दुभे: पौरवीरोहिणी- मदिराभद्रादेवकीप्रमुखा बह्ढलयः पत्यो5भवन्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8104)
- **Original**: बलभद्रशठसारणदुर्मदादीन्पुत्रा- आहिण्यामानकदुन्दुभिरुत्पादयामास
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8105)
- **Original**: बलदेवो5पि रेवत्यां बिज्वठोल्मुकौ पुत्रावजनयत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8106)
- **Original**: साप्ट्िमाष्टिशिशुसत्यधृत्तिप्रमुखाः सारणात्मजा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8107)
- **Original**: भद्माश्चभद्रबाहु- दुर्दभभूताद्या रोहिण्या:. कुछ॒जा:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8108)
- **Original**: नन्दोपनन्दकृतकाद्या मदिरायास्तनया:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8109)
- **Original**: भ्रद्यायाश्रोपनिधिगदाद्या:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8110)
- **Original**: वैज्ञाल्यां च कौशिकमेकमेबाजनयत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8111)
- **Original**: तांश् स्वानेव कंसों
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8112)
- **Original**: अनन्तरं चर सप्तम गर्भमर्द्धरात्रे भगवत्महिता योगनिद्रा रोहिण्या जठरमाकृष्य नीतवती
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8113)
- **Original**: कर्षणाश्चासावपि सड्डूर्षणाख्या- मगमत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8114)
- **Original**: ततश्च॒ सकलजगन्महा- तरुमूछभूतो भूतभविष्यदादिसकलसुरासुरमुनि- जनमनसामप्यगोचरोउव्जभवप्रमुखैरनलमुख: प्रणम्याबनिभारहरणाय प्रसादितों भगवाननादि- मध्यनिधनो. देवकीगर्भभवततार बासुदेवः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8115)
- **Original**: तग्सादविवर्द्धमानोस्महिमा चल योगनिद्रा नन्दगोपपल्या यशोदाया गर्भ- मधिष्ठितवती
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8116)
- **Original**: सुप्रसन्नादित्यचन्द्रादिग्रह- मव्यालादिभय स्वस्थमानसमखिलमेवैतज्जगद- पास्ताधर्ममभवत्तर्रिमश्च॒ पुण्डीकनयने जायमाने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8117)
- **Original**: जातेन ञ्ञ तेनास्विलमेबैतत्सन्मार्गवर्त्ति जगदक्रियत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8118)
- **Original**: भगवतोउप्यन्न मर्त्यत्लेकेडवतीर्णस्थ घोडझ- सहस्राण्येकोत्तरताधिकानि. भार्याणामभवन्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8119)
- **Original**: तासां चर रुक्मिणीसत्यभामाजाम्बवती- चारुहासिनीप्रमुखा ह्ााष्टो पल्यः प्रधाना बभूवुः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8120)
- **Original**: तासु चाष्टाबयुतानि लक्ष चल पुत्राणां चतुर्थ अंश 285 दुर्लभ परमफल देते हैं, फिर सम्यक्‌ भक्तिसम्पन्न पुरुषोंकी तो बात ही कया है ?
- **Translation**: 

---

