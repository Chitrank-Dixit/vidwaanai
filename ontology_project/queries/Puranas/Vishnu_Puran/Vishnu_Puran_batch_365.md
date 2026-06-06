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

### Verse 1 (Vishnu Puran 0.7281)
- **Original**: सुमत्तुके अजक, अजकके बल्त्रकाश्च, बल्प्रकाश्के कुडा और कुशके कुझाम्ब, कुशनाभ, अधूर्त्तजा और वसु नामक चार पुत्र हुए
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7282)
- **Original**: उनमेंसे कुशाम्बने इस इच्छासे कि. मेरे इन्द्रके समान पुत्र हो, तपस्या की
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7283)
- **Original**: उसके उग्र ठफ्को देखकर 'बलमें कोई अन्य मेरे समान न हो जाय' इस भयसे इन्द्र स्वय ही इनका पुत्र हो गया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7284)
- **Original**: वह गाधि नामक पुत्र कौशिक कहलाया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7285)
- **Original**: गाघिने सत्यवती नामकी कन्याको जन्म दिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7286)
- **Original**: 260 ऑविष्णुपुराण ([ आ* 7 तांच भार्गव ऋचीको वब्रे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7287)
- **Original**: गाधिरप्यति- रोषणायातिवृद्धाय ब्राह्मणाय दातुपनिच्छत्रेकतरश्याम- कण्णानामिन्दुवर्चससामनिलरंहसामधानां.. सह कन्याशुल्कमयाकत्तत
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7288)
- **Original**: तेनाप्यृषिणा वरुणसकाझादुपलध्याश्रतीर्थोत्पन्ने तादुझ- मश्वसहर्त्नं दत्तम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7289)
- **Original**: ततस्तायृचीक: कन्यामुपयेमे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7290)
- **Original**: ऋचीकशञ्न॒ तस्याश्ररुमपत्यार्थ चकार
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7291)
- **Original**: तत्प्रसादितश्ष तन्मात्रे क्षत्रवरपुत्रोत्फ्तये चरुमपरं साधयामास
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7292)
- **Original**: एप चरुभवत्या अब- मपस्रुस्त्वन्मात्ना सम्यगुपयोज्य डइत्युक्त्वा वर्न जगाम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7293)
- **Original**: उपयोगकाले ञ्व॒ तां मांता सत्यवतीमाह
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7294)
- **Original**: पुत्रि सर्व एबात्मपुत्रमतिगुणमभिलषति नात्मजायाश्रातृगुणेघ्रतीबादृतो भवतीति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7295)
- **Original**: अतोडहसि ममात्मीयं चरूं दातुं मदीयं चरुमात्मनोप- योक्तुम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7296)
- **Original**: मत्पुत्रेण हि सकलभूमण्डल- परिपालन कार्य॑ कियद्वा ब्राह्मणस्थ बलवीर्य- सम्पदेत्युक्ता सा स्वचरूं मात्रे दत्ततती
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7297)
- **Original**: अथ् बनादागत्य सत्यवतीमृषिरपक्यत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7298)
- **Original**: आह चैनामतिपापे किमिदमकार्य भवत्या कृतमतिरौद्र ते बपुर्लक्ष्यते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7299)
- **Original**: नूने त्वया त्वन्यातृसात्कृतश्वरुुपयुक्तो न युक्तमेतत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7300)
- **Original**: मया हि तत्र चरो सकलैश्नर्यवीर्यशौर्य- बलसम्पदारोपिता त्वदीयचरावष्यसिलशान्ति- ज्ञानतितिक्षादिब्राह्मणगुणसम्पत्‌
- **Translation**: 

---

