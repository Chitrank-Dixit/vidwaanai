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

### Verse 1 (Markende Puran 0.3101)
- **Original**: याबन्तः पत्तितास्तस्य शारीराद्रक्तब्रिन्दवः
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3102)
- **Original**: ताबन्तः पुरुषा जातास्तद्वीरबजलबिक्रमा:
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3103)
- **Original**: ते चापि युयुधुस्तम्न पुरूषा रक्तसम्भवाः। सम॑ पातृषिरत्युग्रशस्त्रपातातिधीषणम्‌
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3104)
- **Original**: +रेक्तयीज-वध+ ह## 7 7377 7 पुनश्च॒ वज़णत्तेन क्षतमस्यथ शिरो यदा। जजाह रक्त पुरुषास्ततों जाता: सहस्रशः
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3105)
- **Original**: जैष्णवी समरे चैन अक्रेणाभिजधान ह। गदया ताडयामास ऐन्द्री तमसुरेश्वरम्‌
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3106)
- **Original**: वैष्णबीचक्रभिनतस्थ रुधिरखावसभ्भवे:। सहस्रशों जगद्धयाप्त॑ तत्प्रपाणैर्महासूँर:
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3107)
- **Original**: शक्तघवा जधान कौपारी याराष्टी च तथासिना। माहेश्वरी विशूलेन रक्तयीज महासुरप्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3108)
- **Original**: स चापि गदया दैत्य: सर्वा एवाहनत्‌ पृथक्‌ । मातृ: कोपसभाविष्टो रक्तबीजो महासुरः
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3109)
- **Original**: तस्याइतस्थ बहुधा शक्तिशूलादिधिभूवि। फ्पात्त यो वे रक्तौघस्तेनासम्छतशोउसुरा:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3110)
- **Original**: तैश्लासुरासक्सम्भूतैरसुरैः सकले जगत्‌। व्याप्तमासीत्ततो देवा भयमाजमण्मुरत्तमम्‌
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3111)
- **Original**: तान्‌विधण्णान्‌ सुगन्‌ दृष्ठा चण्डिका प्राह सत्वरा। उबाच काली चामुण्डे विस्तीर्ण! बदन कुरु
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3112)
- **Original**: भच्छस्त्रपातसम्भूतान्‌ रक्तब्िन्दूल्सहासुरान्‌। रक्तबिन्दो: प्रतीच्छ त्म॑ बक्वेणानेस वेगिना '
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3113)
- **Original**: भक्षयन्ती चर रणे तदुत्पत्रान्महासुरान्‌। एचमेष श्रर्य देत्य: क्षीणरक्तों शधिष्यति
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3114)
- **Original**: भ्रक्ष्यपाणासत्वया चोग़ न चोत्पत्त्थन्ति चापरे । इत्युकत्या तां ततों देवी शूलेताभिजपान तम्‌
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3115)
- **Original**: मुखेन काली जगुहे रक्तजीजस्य शोणितम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3116)
- **Original**: ततोउसायाजघानाथ गदया तत्र घण्डिकाम्‌
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3117)
- **Original**: न क्षास्या चेदनां चक्रे गदापातो5ल्पिक्रापपि
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3118)
- **Original**: तस्वाहतस्य देहात्तु बहु सुर्राव ज्ञोणितम्‌
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3119)
- **Original**: यतस्ततस्तद्वक्त्रेण चामुण्डा सम्प्रतीच्छति। मुखे समुद्गता ये3स्था पक्तपातान्महासुरा:। तांशखादाथ चामुण्डा पपी तस्य थ शोणितप्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3120)
- **Original**: । देवी शूलेन वज्जेणं बराणैरसिभिऋष्टिभि:। जघान रक्तबीजं तं चामुण्डापीतशोणितम्‌ 460 1. पाल-नविस्तरें।, 6. छा0-यांगेता। 3. उसके #. एछा2--चक्रेण। 5. पा--शस्‍स्प्र्सहतिययं! हत;। 3 330 #4-» क 7 $ $ + 1 शो अल 22-30». $.
- **Translation**: 

---

