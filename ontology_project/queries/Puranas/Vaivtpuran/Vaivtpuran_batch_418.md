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

### Verse 1 (Vaivtpuran 22.18201)
- **Original**: ध्यानेनानेन देवेन्द्र ध्यात्वा लक्ष्मीं मनोहराम्‌ । भक्त्या दास्यसि तस्यै च चोपचाराणि घोड़श
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.18202)
- **Original**: स्तुत्वनेनः स्तवेनैव वक्ष्याणेन यासव । नत्वा बरं गृहीत्वा च लभिष्यसि क्ष निर्वुतिम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.18203)
- **Original**: स्तवन श्रृणु देवेन्द्र महालक्ष्या: सुखप्रदम्‌ । कथवामि सुगोप्य॑ च त्रिषु लोकेषु दुर्लभम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.18204)
- **Original**: इति श्रीब्रह्मवैवर्ते मन्त्रध्यानसहिर्त लक्ष्म्या ध्यार्न सम्पूर्णम्‌। (गणपत्तिखण्ड 22। 18--26) नारायण उवबाच देवि त्वां स्तोतुमिच्छामि न क्षमा: स्तोतुमीश्चरा: । बुद्धेरगोचरां सूक्ष्म तेजोरूपां सनातनीम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.18205)
- **Original**: अत्यनिर्वचनीयां च को वा निर्वक्तुमी भ्वरः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.18206)
- **Original**: स्वेच्छामयी निराकारां भक्तानुग्रहविग्रहमम्‌ । स्तौमि बाइमनसो: पारां किं बाहं जगदम्बिके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.18207)
- **Original**: परां चतुर्णां वेदानां पारबीज॑ भवार्णवे । सर्वशस्याधिदेवीं च सर्वासामपि सम्पदाम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.18208)
- **Original**: योगिनां चैब योगानां ज्ञानानां ज्ञानिनां तथा । बेदानां च्र वेदविदां जननीं वर्णयामि किम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.18209)
- **Original**: यया विना जगत्‌ सर्वमवस्तु निष्फलं श्रुवम्‌ । यथा स्तनान्थबालानां विना मात्रासुखं भवेत्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.18210)
- **Original**: प्रसीद जगतां माता रक्षास्मानतिकातरान्‌ । वबयं त्वच्चरणाम्भोजे प्रपन्ना: शरणं गता:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.18211)
- **Original**: नमः शक्तिस्वरूपाय जगम्मात्रे नमो नमः । ज्ञानदायै बुद्धिदाये सर्वदाये॑ नमो नमः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.18212)
- **Original**: हरिभक्तिप्रदायिन्ये मुक्तिदाय॑य नमो. नमः । सर्यज्ञाये॑सर्वदाये॑ महालक्ष्म्मे॑नमो नमः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.18213)
- **Original**: कुपुत्रा: कुत्रचित्‌ सन्ति न कुत्रचित्‌ कुमातरः । कुत्र माता पुत्रदोषे त॑ विहाय चर गच्छति
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.18214)
- **Original**: है मातर्दर्शन॑ देहि स्तनान्धान्‌ू बालकानिव
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.18215)
- **Original**: कृपां कुरु कृपासिश्धुप्रियेउस्मान्‌ भक्तयत्सले
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.18216)
- **Original**: इत्येष॑ कथित वत्स पद्मायाश्न शुभावहम्‌ । सुखद मोक्षदं सारं शुभदं सम्पदः: पदम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.18217)
- **Original**: इद स्तोत्न॑ महापुण्यं पूजाकाले च यः पठेत्‌ । महालक्ष्मीगृंहँ तस्यथ न जहाति कदाचन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.18218)
- **Original**: इत्युक्सा श्रीहरिस्त॑ च्॒ तत्रैवान्तधीयत । देवो जगाम क्षीरोद सुँरेः साथ तदाज्ञया
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.18219)
- **Original**: इति श्रीब्रह्मवैवते मन्त्रध्यानसहित लक्ष्य्या: स्तोत्र सम्पूर्णम्‌। (गणपतिखण्ड 22। 27-39) 220 पद. 900+0+
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.18242)
- **Original**: भर श्रीलक्ष्म्या: स्तोत्राणि « <03 4. 4 4 4 8 4
- **Translation**: 

---

