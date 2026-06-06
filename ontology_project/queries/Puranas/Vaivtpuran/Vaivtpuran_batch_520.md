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

### Verse 1 (Vaivtpuran 31.7571)
- **Original**: तेजस्विनां रवियों हि. सर्वजातिषु. ब्राह्मण:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.7572)
- **Original**: नक्षत्राणां च यश्चद्धस्त॑ नमामि जगत्प्रभुम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.7573)
- **Original**: रुद्राणां वैष्णवानां च ज्ञानिनां यो हि शंकर:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.7574)
- **Original**: नागानां यो हि शेषश्चव॒ त॑ नमामि जगत्पतिम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.7575)
- **Original**: प्रजापतीनां यो ब्रह्मा सिद्धानां कपिल: स्वयम्‌। सनत्कुमारों मुनिषु त॑ नमामि जगदुगुरुम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.7576)
- **Original**: देवानां यो हि विष्णुश्व देवीनां प्रकृति: स्वयम्‌। स्वायम्भुवों मनूनां यो मानवेषु च वैष्णव:। नारीणां शतरूपा च॑ बहुरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.7577)
- **Original**: ऋतूनां यो वसन्तश्च॒ मासानां मार्गशीर्षकफ:। एकादशी तिथीनां च नमामि सर्वरूपिणम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.7578)
- **Original**: सागर; सरितां यश्ष पर्वतानां हिमालय: । वसुन्धाा सहिष्णूनां त॑ सर्व॑ प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.7579)
- **Original**: पत्राणां तुलसोपत्रं दारुरूपेषू चन्दनम्‌ । वृक्षाणां कल्पवृक्षो यस्त॑ नमामि जगत्पतिम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.7580)
- **Original**: पुष्पाणां पारिजातक्ष शस्यानां धान्यमेव च। अपृ्त भक्ष्यवस्तूनां. नानारूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.7581)
- **Original**: ऐराबतो.. गजेद्राणां. चैनतेयश्च पक्षिणाम्‌ू । कामधेनुश धेनूतां. सर्वरूप॑. नमाम्यहम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.7582)
- **Original**: तेजसानां सुबण॑ च धान्यानां यव एवं च। यः: केश्री पशूनां च वररूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.7583)
- **Original**: यक्षाणां च कुबेरो यो ग्रहाणां च बृहस्पति:। दिकृपालानां महेनद्धश्व॒ त॑ नमामि पर वरम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.7584)
- **Original**: वेदसंघक्ष॒ शास्त्राणां. पण्डितानां. सरस्वती । अक्षराणामकारों यस्त॑ प्रधान॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.7585)
- **Original**: म्न्त्राणां विष्णुमत्रश्ध॒तीर्धानां जाह॒बी स्वयम्‌ । इन्द्रियाणां मनो यो हि सर्वश्रेष्ठ नमाम्यहम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.7586)
- **Original**: सुदर्श॑ च शस्त्राणां व्याधीनां वैष्णबों ज्वःः। तेजसां ब्रह्मतेजक्ष वरेण्ये॑ त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.7587)
- **Original**: निषेकश् बलवतां मनश्च॒ शीघ्रगामिनाम्‌ू । काल: कलयतां यो हि त॑ नमामि विलक्षणम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.7588)
- **Original**: ज्ञादाता गुरूणां च॒ मातृर्पश्ष॒ अन्धुषु। मित्रेषु जन्मदाता यस्तं सार प्रणमाध्यहम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.7589)
- **Original**: शिल्पीनां विश्वकर्मा यः: कामदेवश्च रूपिणाम्‌ । पतित्रता च पत्नीनां नमस्यं॑ त॑ नमास्यहम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.7590)
- **Original**: प्रियेषू.. पृत्रपो यो नृपरूपों नरेषु च। शालग्रामश्चव॒ यन्त्राणां त॑ विशिष्ट नमास्यहम्‌
- **Translation**: 

---

