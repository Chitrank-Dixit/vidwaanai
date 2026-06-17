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

### Verse 1 (Garuda1 0.201)
- **Original**: शब्दात्मा चैय वबागात्मा स्पशात्पा पुरुषस्तथा। ओ्रोत्रात्मा थे त्वगात्मा च॑ जिद्धात्मा परमस्तथा
- **Translation**: 

---

### Verse 2 (Garuda1 0.202)
- **Original**: घ्राणात्मा चैव हस्तात्मा पादात्या परमस्तथा। उपस्थस्थ तथैवात्मा . पाय्यात्मा . परमस्तखा
- **Translation**: 

---

### Verse 3 (Garuda1 0.203)
- **Original**: इन्द्रात्मा चैव स्रह्मात्मा रुद्रा ( शान्ता ) स्पा च मत्रोस्तथा। दक्षप्रजापतेरात्मा सत्या ( स्त्रष्टा )त्मा परमस्तथ्ा
- **Translation**: 

---

### Verse 4 (Garuda1 0.204)
- **Original**: 1-बाह्लाहकार0 । 2-प्यणिपादायिगि पा । उशात्मा परमात्मा त्ञ रौव्रात्मा मोक्षविद्यति:। यलवांध् तथा यलक्षमी खड़गी मुरात्तक: ( असुव्रस्तक: )
- **Translation**: 

---

### Verse 5 (Garuda1 0.205)
- **Original**: ड्रीफ्रवर्तनशीलभ्र - शत्तीनाँ छा. हिते रतः। यतिरूपी लव ग्रोमी च योगिध्येयो हरि: शित्ति:
- **Translation**: 

---

### Verse 6 (Garuda1 0.206)
- **Original**: संविस्मेधा च कालक्ष ऊष्पा वर्षा म (मर) तिस्तथा। संवल्सरो मोक्षकरो मोहप्रध्यंसकस्तथा
- **Translation**: 

---

### Verse 7 (Garuda1 0.207)
- **Original**: मोहकर्ता उ्ञ दुष्टानां माण्डव्यो वड़वामुखः:। संघर्तः. कालकर्ता थ॑ गौतमो भृगुरड्निराः
- **Translation**: 

---

### Verse 8 (Garuda1 0.208)
- **Original**: अन्रिव॑सिप्ठ: पुलहः पुलस्त्य: कुल्स एवं चा। याज़वल्कयो देवलक्ष॒ व्यासश्ैव पराशरः:
- **Translation**: 

---

### Verse 9 (Garuda1 0.209)
- **Original**: शर्मदक्षव गाड्डेयो इृषीकेशो बृहच्छुवा:। केशव: क्लेशहन्ता अर सुकर्ण: कर्णवर्जित:
- **Translation**: 

---

### Verse 10 (Garuda1 0.210)
- **Original**: तारायणो महाभाग: प्राणस्थ पतिव च। अपानस्थ पतिश्व स्यानस्थ पत्तिरेव चा
- **Translation**: 

---

### Verse 11 (Garuda1 0.211)
- **Original**: उदानस्थ पति: श्रेष्ठ. समागस्यथ पतिस्तथा। शब्दस्य च पतिः श्रेष्ठ: स्पर्शस्थ पतिरेव च्च
- **Translation**: 

---

### Verse 12 (Garuda1 0.212)
- **Original**: रूपाणां थ॒ पतिक्षाद्यः खड्गपाणिईलायुध:। अक्रपाणि: कुण्डली अर श्रीवत्साड्डस्तथैव चल
- **Translation**: 

---

### Verse 13 (Garuda1 0.213)
- **Original**: प्रकृति: कॉौस्तुधग्रीव:.. पीताम्बरधरस्तथा। सुषुो दुर्भुखड्ैथ पुखेन तु विवर्जित:
- **Translation**: 

---

### Verse 14 (Garuda1 0.214)
- **Original**: अपनन्तोउजलरूपक्ष सुतज: सुस्मच्दर:। सुकपोलो विधुर्जिष्णुभ्राजिष्णुक्षेषुधीस्तथा
- **Translation**: 

---

### Verse 15 (Garuda1 0.215)
- **Original**: हिरण्यकशिपोहन्ता हिएण्याक्षविमर्टक:। विह्ता पूततायाक्ष भास्करानविनाशत:
- **Translation**: 

---

### Verse 16 (Garuda1 0.216)
- **Original**: केशिनो दलनश्जैव मुष्टिकस्थ विमर्दकः। कंसदानव्धेत्ता च चाणूरस्य ( ग्रेनुकस्थ ) प्रमर्दकः
- **Translation**: 

---

### Verse 17 (Garuda1 0.217)
- **Original**: अरिटटस्थ विहन्‍्ता अर अक़्रप्रिय एवं च। अक्ूरः क्र्ररूपश्ष अक्कूरप्रियवन्दित:
- **Translation**: 

---

### Verse 18 (Garuda1 0.218)
- **Original**: भगहा भगवान्‌ भानुस्तशा भागवत: स्वयम्‌। उद्धवश्ोद्धबस्पेशों. ह्ुद्धवेन: . विचिन्तित:
- **Translation**: 

---

### Verse 19 (Garuda1 0.219)
- **Original**: अक्रधूझक चशललक्षेव चलाचलविवर्जित:। अहक्लरोपमश्चित्त गगन पृथ्चिवी जलप्‌
- **Translation**: 

---

### Verse 20 (Garuda1 0.220)
- **Original**: वायुअक्षुस्तशा अ्रोज्॑ जिह्मा थ॒ प्राणमेष च। वाक्याणिपादजवन:'. पायूपस्थस्तथैव च
- **Translation**: 

---

