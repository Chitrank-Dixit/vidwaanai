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

### Verse 1 (Garuda1 0.241)
- **Original**: रागेण_ विगतशव अधघेन परिवर्जितः। शोकेन रहितक्षेव बचसा परिवर्जित:
- **Translation**: 

---

### Verse 2 (Garuda1 0.242)
- **Original**: रजोचियर्जितशैय. विकारैः. घपड़भिरिव जा कामेन वर्जितझव क्रोधेन परिवर्जित:
- **Translation**: 

---

### Verse 3 (Garuda1 0.243)
- **Original**: लोधेनभ विगतश्लैय दम्भेन च॑ विवर्जित:। सूक्ष्कीथ सुसूक्ष्श स्थूलात्स्थुलतरस्तथा
- **Translation**: 

---

### Verse 4 (Garuda1 0.244)
- **Original**: विशारदों खलाध्यक्ष: सर्वस्थ क्षोभकस्तथा। प्रकृते: . क्षोभकजैयवय महतः: . क्षोभकस्तथा
- **Translation**: 

---

### Verse 5 (Garuda1 0.245)
- **Original**: ा भूतातां.. क्षोभकक्षेय बुद्धेश. क्षोभकस्तथा। डन्द्रियणां. क्षोधकश्ष॒ विषयक्षोभकस्तथा
- **Translation**: 

---

### Verse 6 (Garuda1 0.246)
- **Original**: ख्रह्मण:.. क्षोभकक्षेथ रुडस्थ क्षोभकस्तथा। अग्यश्चश्षुरादेश्व ओत्रागम्यस्तथैव च
- **Translation**: 

---

### Verse 7 (Garuda1 0.247)
- **Original**: त्वचा न गध्य: कुर्मश्ष जिह्लाउग्राहस्तथैव च। प्राणेल्ियागस्य एव खाचा5ग्राह्मस्तथैयथ च
- **Translation**: 

---

### Verse 8 (Garuda1 0.248)
- **Original**: अगम्यक्षव. पाणिध्यां. पदागध्यस्तथैव छा अग्राह्यों मनसश्चैव बुद्ष्याउग्राह्यों हरिस्तथा
- **Translation**: 

---

### Verse 9 (Garuda1 0.249)
- **Original**: अहं बुद्धण तथा ग्राह्मक्षेतस्रा ग्राह्म एवं ऋ्। शब्बुपाणिक्षाव्ययक्ष गदापाणिस्तथेव च
- **Translation**: 

---

### Verse 10 (Garuda1 0.250)
- **Original**: शाब्रपाणिश्ष॒ कृष्णश्च॒ ज्ञानमूर्ति: पस्नप:। त़पसवी ज्ञानगष्यो हि ज्ञात्री ज्ञानविदेव च
- **Translation**: 

---

### Verse 11 (Garuda1 0.251)
- **Original**: ज्ञेयश्व ज्ञेयहीनअञ ज़ञप्तिश्ैतन्यकूपक: । भावों भाव्यो भवकरों भावत्रों भवनाशन:
- **Translation**: 

---

### Verse 12 (Garuda1 0.252)
- **Original**: गोविन्दो गोपतिगॉप: सर्वंगोपीसुखप्रदः । गोपालो गोगतिश्षैय गोमतिर्गोंधरस्तथा
- **Translation**: 

---

### Verse 13 (Garuda1 0.253)
- **Original**: उपेन्रश्भ नृसिंहश् शौरिक्षक्ष जनार्दन:। आरणोेयो यहदभानुर्वृहददीप्तिस्तथैव च्य
- **Translation**: 

---

### Verse 14 (Garuda1 0.254)
- **Original**: दामोदरस्थिकालश् कालज्ञ: कालवर्जित:। ब्रिसश्यो द्वापरं ज्रेल्ा प्रज़ाद्ाई त्रिविक्रम:
- **Translation**: 

---

### Verse 15 (Garuda1 0.255)
- **Original**: चिक्रमों दण्ड (2)हस्तश्न होकदण्डी त्रिदण्डधूक्‌। सायधेदस्तथोपाय: सामरूपी च साथगः
- **Translation**: 

---

### Verse 16 (Garuda1 0.256)
- **Original**: सामवेदी हाशर्वश्ष॒ सुकृत: . सुतरूपण:। अशर्ववेदविच्चैव.. ह्ा्थर्वाचार्थ एव... जा। ऋषृपी चैव ऋग्वेद ऋतग्वेदेषु प्रतिष्ठित: । यजुरय्ेत्ता यजुर्वेदो यजुर्वेदविदेकपात्‌
- **Translation**: 

---

### Verse 17 (Garuda1 0.257)
- **Original**: वहुपाच्च सुपाच्चैत तशैय ऊा सहस्पात्‌।
- **Translation**: 

---

### Verse 18 (Garuda1 0.258)
- **Original**: पूस्धों वाक्करणं थैव वाद्य चैव तु जाथकः
- **Translation**: 

---

### Verse 19 (Garuda1 0.259)
- **Original**: वेत्ना व्याकरणं चैज वाक्य चैज॑। च वाक्यवित्‌। वाक्यगम्यस्तीर्थवासी तीर्थस्तीथी ज्ञ तीर्शवित्‌
- **Translation**: 

---

### Verse 20 (Garuda1 0.260)
- **Original**: तीर्थादिभूतः साद्ुघक्ष तिरुक्त त्वधिदेवतम्‌। प्रणव: प्रणवेशश्ष॒ प्रणवेन .प्रवन्दितः
- **Translation**: 

---

