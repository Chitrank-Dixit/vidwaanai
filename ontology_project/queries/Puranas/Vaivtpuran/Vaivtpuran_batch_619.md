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

### Verse 1 (Vaivtpuran 55.19196)
- **Original**: गोलोके राधिका त्व॑ च सर्वगोपषालकेश्वरी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.19197)
- **Original**: त्ववा विनाहँ निर्जीवों हाशक्त: सर्वकर्मसु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.19198)
- **Original**: शिव: शक्तस्त्वया शक्त्या शवाकारस्त्वया विना
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.19199)
- **Original**: वेदकर्ता स्वयं ब्रह्मा वेदमात्रा त्ववा सह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.19200)
- **Original**: नारायणस्त्वया लक्ष्म्या जगत्पाता जगत्पति:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.19201)
- **Original**: फलं॑ ददाति यज्ञश्न॒ त्ववया दक्षिणया सह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.19202)
- **Original**: विभर्ति सृष्टि शेषश्ष त्यां कृत्वा मस्तके भुवम्‌। विभर्ति गड्जारूपां त्वां मूर्खि गड्भाधर: शिव:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.19203)
- **Original**: शक्तिमच्च जगत्‌ सर्व शवरूपं त्वया विना। वक्ता सर्वस्त्वया वाण्या सूतो मृकस्त्वया बिना
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.19204)
- **Original**: + श्रीराधास्तोत्राणि * 835 5$%%$%$%$$%$%$$%$%$%$%$$$$%$%$$$%#% 55 #% 55555 ##%###%%#%########6##%#####6&##6#####&####&#
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.19205)
- **Original**: $%क्कऋ%$%$%%$%$%$%% 55% # 55% #% 5 ###%##### 4 ########%####### 686 #&# &#%#&#& # यथा मृदा घट कर्तुं कुलाल: शक्तिमान्‌ सदा । सुष्टिं र्रष्टं तथाहं चर प्रकृत्या च॒ त्वया सह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.19206)
- **Original**: त्वया बिना जडश्षाहं सर्वत्र च न शक्तिमान्‌। सर्वशक्तिस्वरूपा त्व॑ समागच्छ मप्रान्तिकम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.19207)
- **Original**: बह्नौ त्वं दाहिका शक्तिर्नांग्रि: शक्तस्त्ववा विना । शोभास्वरूपा चनद्रे त्वं त्वां बिना न स सुन्दरः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.19208)
- **Original**: प्रभारूपा हि सूर्ये त्वं त्वां विना न स भानुमानू । न काम: कामिनीबन्धुस्त्वया रत्या बिना प्रिये
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.19209)
- **Original**: इत्येब॑ स्तवन कृत्वा तां सम्प्राप जगत्प्रभु;। देवा बभूबु: सश्रीका: सभायाँ: शक्तिसंयुता:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.19210)
- **Original**: सस्त्रीक॑ च जगत्‌ सर्व॑ बभूव शैलकन्यके । गोपीपूर्णक्ष गोलोको बभूब तत्प्रसादत:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.19211)
- **Original**: राजा जगाम गोलोकमिति स्तुत्वा हरिप्रियाम्‌ । श्रीकृष्णेन कृर्त स्तोत्र राधाया यः पठेन्नर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.19212)
- **Original**: कृष्णभक्ति च तददास्यं स प्राप्रोतिन संशय: । स्त्रीविच्छेदे यः श्रृणोति मासमेकमिर्द शुत्तिः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.19213)
- **Original**: अचिराल्लभते भायाँ सुशीलां सुन्दरीं सतीम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.19214)
- **Original**: भार्याहीनों भाग्यहीनो वर्षमेक॑ श्रूणोति यः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.19215)
- **Original**: अचिराल्लभते भायाँ सुशीलां सुन्दरी सतीम्‌ । पुरा मया च॒ त्वं प्राप्ता स्तोत्रेणानेन पार्वति
- **Translation**: 

---

