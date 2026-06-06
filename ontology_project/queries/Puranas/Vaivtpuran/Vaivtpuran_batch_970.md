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

### Verse 1 (Vaivtpuran 675.5686)
- **Original**: उपाख्यान सुनाया है। (अध्याय 65) 34050“ #द252825..050050 *मा भुक्त क्षीयते कर्म कल्पकोटिशतैरपि । अवश्यमेव भोक्तव्य॑ कृत॑ कर्म शुभाशुभम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 675.5687)
- **Original**: (प्रकृतिखण्ड 675। 47)
- **Translation**: 

---

### Verse 3 (Vaivtpuran 1216.17715)
- **Original**: छ्8ड * संक्षिम ब्रह्मवैयर्तपुराण *
- **Translation**: 

---

### Verse 4 (Vaivtpuran 1216.17716)
- **Original**: श्रीराधाकृतं॑ गण्णेशस्तोत्रम्‌ ] श्रीराधिकोबाच परं॑ धाम परे बहा परेशं परमीश्वरम्‌ । विंध्ननिप्नकरं शान्त पुष्टे कान्तमनन्तकम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 1216.17717)
- **Original**: सुरासुरेन्द्र: सिद्धेन्द्रै: स्तुतं स्तौमि परात्परम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 1216.17718)
- **Original**: सुरपछादिनेशं च गणेश मड्ुलायनम्‌ू
- **Translation**: 

---

### Verse 7 (Vaivtpuran 1216.17719)
- **Original**: डुदं स्तोत्र महापुण्यं विप्नशोकहरं परम्‌ । यः पठेत्‌ प्रातरुत्थाय सर्वविप्नात्‌ प्रमुच्यते
- **Translation**: 

---

### Verse 8 (Vaivtpuran 1216.17720)
- **Original**: इति श्रीब्रह्मबैवर्ते श्रएधाकृतं यणेशस्तरोत्र सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 1216
- **Translation**: 

---

### Verse 9 (Vaivtpuran 1216.17721)
- **Original**: 103-105) _--अथ्च:य 22700
- **Translation**: 

---

### Verse 10 (Vaivtpuran 1216.17722)
- **Original**: शनैश्वरं प्रति विष्णुनोपदिष्टे संसारमोहनं गणेशकवचम्‌ ल्‍ विष्णुर्वाच संसारमोहनस्यास्थ कवचस्य प्रजापति: । ऋषिश्ठन्दश्ष बृहती देवों लम्बोदर: स्वयम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 1216.17723)
- **Original**: धर्मार्थकाममोक्षेपु. विनियोग: . प्रकीर्तित: । सर्वेषां कवचानां चर सारभूतमिदं मुने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 1216.17724)
- **Original**: 3» गं हुँ श्रीगणेशाय स्वाहा में पातु मस्तकम्‌ । द्वात्रिंशदक्षगों मनत्रों ललार्ट में सदावतु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 1216.17725)
- **Original**: 3 हीं क्लीं श्रीं गमितिच संत्त पातु लोचनम्‌ । तालुर्क॑ पातु विघ्लेश: संतर्त धरणीतले
- **Translation**: 

---

### Verse 14 (Vaivtpuran 1216.17726)
- **Original**: 3» हुं श्री कलीमिति च संततं पातु नासिकाम्‌ । 3* गाँ ग॑ शूर्पकर्णाय स्वाहा पात्वधरं मम्त
- **Translation**: 

---

### Verse 15 (Vaivtpuran 1216.17727)
- **Original**: दन्तानि तालुकां जिह्नां पातु मे घोडशाक्षर:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 1216.17728)
- **Original**: 3» ल॑ श्रीं लम्बोदरायेति स्वाहा गणएडं सदावतु । 30 क्लीं ह्रीं विघ्ननाशाय स्वाहा कर्ण सदावतु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 1216.17729)
- **Original**: 3» श्रीं ग॑ गजाननायेति स्वाहा स्कन्ध॑ सदावतु । 40 ह्रीं विनायकायेति स्वाहा पृष्ठ सदावतु
- **Translation**: 

---

### Verse 18 (Vaivtpuran 1216.17730)
- **Original**: 3» क्लीं ह्ीमिति कड्जाल॑ पातु वक्ष:स्थलं च गम्‌ । करौ पादौ सदा पातु सर्वाड्रं विप्ननिश्नकृत्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 1216.17731)
- **Original**: प्राच्यां लम्बोदरः पातु आग्रेय्यां विघ्ननायक: । दक्षिणे पातु विप्लेशों नैक्रत्यां तु गजानन:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 1216.17732)
- **Original**: पश्चिमे पार्वतीपुत्रों खायव्यां शंकरात्मज: । कृष्णस्यांशश्रोत्ते च॑ परिपूर्णतमस्य च
- **Translation**: 

---

