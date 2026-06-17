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

### Verse 1 (Vaivtpuran 22.6959)
- **Original**: क्षससागरके तटपर गये। वहाँ उन्होंने अमूल्य गुरु बृहस्पति तथा अन्यान्य देबॉकों साथ लेकर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.6960)
- **Original**: रत्नकी गुटिकासे युक्त कवचको गलेमें बाँधकर लक्ष्मीकी प्राप्तिके लिये प्रसन्न-मनसे शीघ्र ही
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.6961)
- **Original**: पुन:-पुनः उस दिव्य स्तोत्रका मन-ही-मन स्मरण * नारायण उवाच-- देवि त्वां स्तोतुमिच्छामि न क्षमा: स्तोतुमीश्वरा:।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.6962)
- **Original**: बुद्धेरगोचरां सूक्ष्म तेजोरूपां. सनातनीम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.6963)
- **Original**: अत्यनिर्ववनीयां च को वा निर्वक्तुमीश्चर:। स्वेच्छामयीं निराकारां. भक्तानुग्रहविग्रहाम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.6964)
- **Original**: स्तौमि वाड्मनसो: पारां कि बाहं जगदम्बिके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.6965)
- **Original**: परां चतुर्णाँ बेदानां पारबीज॑ धवार्णवे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.6966)
- **Original**: सर्वशस्याधिदेवीं च॒ सर्वासामपि योगिनां चैव योगानां ज्ञानानां ज्ञानिनां तथा । वेदानां च वेदविदां जननी वर्णयामि किमू
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.6967)
- **Original**: यया बिना जगतू सर्वमवस्तु निष्फल॑ ध्रुवम्‌ । यथा स्तनान्थबालानां बिना मात्रासुखं भवेत्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.6968)
- **Original**: प्रसीद जगतां माता रक्षास्मानतिकातरानू । बय॑ त्वच्चरणाम्भोजे प्रपन्ना: शरणं गता:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.6969)
- **Original**: नमः शक्स्वरूपाये॑ जगन्मात्रे नमो नमः । ज्ञानदायै बुद्धिदाये सर्वदाये नमो नमः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.6970)
- **Original**: हरिभक्तिप्रदायिन्ये मुक्तिदाया. नमो. नमः । सर्वज्ञायेसर्वदाये॑ महालक्ष्म्ये॑ नमो. नमः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.6971)
- **Original**: कुपुत्रा: कुत्रचितू सन्ति न कुजत्रचितू कुमातर:। कुत्र माता पुत्रदोषे त॑ विहाय च गच्छति
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.6972)
- **Original**: है मातर्दर्शी देहि स्ततान्थान्‌ू बालकानिव । कृपां कुरू कृपासिन्धुप्रियेडस्मान्‌ भक्तबत्सले
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.6973)
- **Original**: इत्येव कथित वत्स इ ञ,»ायाक्ष शुभावहम्‌ । सुखद मोक्षद॑ सारं शुभद॑ सम्पद: पदम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.6974)
- **Original**: इदं स्तोत्र महापुण्य॑ पूजाकाले च यः पठेत्‌। महालक्ष्मीगृंहं तस्थ न जहाति कदाचन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.6975)
- **Original**: इत्युक्चा. श्रीहरिस्त॑ च॒ त्रैवान्तरधीयत । देवों जगाम क्षीरोद॑सुरैः साध॑ तदाज्ञया
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.6976)
- **Original**: (गणपतिखण्ड 22। 27-39)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.6977)
- **Original**: किया। फिर सब लोगोंने भक्तिभावपूर्वक कमल-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.6978)
- **Original**: मुस्कराहट थी। उन्होंने अनेक प्रकारकी पूजा- वासिनी लक्ष्मीका स्तवन किया। उस समय उनके
- **Translation**: 

---

