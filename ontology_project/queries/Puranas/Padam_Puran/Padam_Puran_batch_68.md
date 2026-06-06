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

### Verse 1 (Padam Puran 7.1341)
- **Original**: ये प्राप्य जीवन्ति सुरादिस्मेकाल्त बासुदेवे झरणं प्रपष्षे
- **Translation**: 

---

### Verse 2 (Padam Puran 7.1342)
- **Original**: यो भाति सर्वत्र रविप्रभावै: करोति शोष॑ थ रस ददाति
- **Translation**: 

---

### Verse 3 (Padam Puran 7.1343)
- **Original**: य: फ्राणिनामत्तरग: सर खायुस्ते कासुदेय फरणं प्रपश्षे
- **Translation**: 

---

### Verse 4 (Padam Puran 7.1344)
- **Original**: ज्येहस्तु रूपेण स देवदेजों ब्रिभर्ति स्गोकान्‌ सकत्मन्‌ महात्मा । एक्पर्णये नौरिय यर्तते यस्त आसुदेज शरण प्रपे
- **Translation**: 

---

### Verse 5 (Padam Puran 7.1345)
- **Original**: अच्तर्गतोी लोकमयः: सदेय भवत्यसौ स्थावरजड्भमानाम्‌
- **Translation**: 

---

### Verse 6 (Padam Puran 7.1346)
- **Original**: स्वाहासुख्लों देखगणस्थ हेतुस्त॑ खासुदेवे दारणे प्रपद्चे
- **Translation**: 

---

### Verse 7 (Padam Puran 7.1347)
- **Original**: रसेः सुपुण्यै: सकलैस्तु पुष्ट: ससौम्यरूपैर्गुणबित्‌ स स्रेके
- **Translation**: 

---

### Verse 8 (Padam Puran 7.1348)
- **Original**: रज्नाधिपों निर्मलतेजसैब त॑ बासुदेव शरण प्रप्चे
- **Translation**: 

---

### Verse 9 (Padam Puran 7.1349)
- **Original**: तेजःस्वरूपेण विभर्ति ल्मरेकान्‌ सत्तात्‌ समस्तान्‌ स चशचरस्प । निष्केवल्ते झ्ानमय: सुशुद्धस्तै वासुदेव झरण॑ प्रपद्षे
- **Translation**: 

---

### Verse 10 (Padam Puran 7.1350)
- **Original**: दैत्यान्तक॑ दु:खिनाव्रामूछे जानते पर॑ दक्तिमय विशालम्‌। संप्राप्प देवा जिलय॑ प्रयात्ति ते जासुदेय दारणं प्रषे
- **Translation**: 

---

### Verse 11 (Padam Puran 7.1351)
- **Original**: सुख॑ सुख्ाओ सुदहदे सुरेत्ना ज्ञानार्णत ते सुहिते हिते च। सत्याश्नय॑ सत्यगुणोपत्रिएं ते खासुदेख दारणं प्रपद्यो
- **Translation**: 

---

### Verse 12 (Padam Puran 7.1352)
- **Original**: यकस्वरूप पुरुषार्धरूपे॑ सत्यान्यित मापतिमेय पुष्यप्‌ । खिज्ञानसेते जगतो निवास ते खासुदेले करण प्रपद्ये
- **Translation**: 

---

### Verse 13 (Padam Puran 7.1353)
- **Original**: अम्भोधिमष्ये शयने हि यत्य न्यगाकुभोगे झयने विज्ञाले
- **Translation**: 

---

### Verse 14 (Padam Puran 7.1354)
- **Original**: श्रो: पादफडाड्रयमेव सेखते ते बासुदेवे झरणं ग्रपद्े
- **Translation**: 

---

### Verse 15 (Padam Puran 7.1355)
- **Original**: पुण्यान्यित शद्भरसेज नित्ये लीथैंगनेके: परिसेज्यमानम्‌। तत्पादपद्मद्रयपेज तस्थ औवासुदेवस्थ नमामि मित्यम्‌
- **Translation**: 

---

### Verse 16 (Padam Puran 7.1356)
- **Original**: अल्लापह जा यदि खाब्बुजं तद्॒त््वेत्पल्थर्भ ध्वजवायुयुक्तम्‌
- **Translation**: 

---

### Verse 17 (Padam Puran 7.1357)
- **Original**: अलंकृत॑ नृपुरमुद्धिकाभि; औीवासुदेवस्थ नमामि पादम्‌
- **Translation**: 

---

### Verse 18 (Padam Puran 7.1358)
- **Original**: देवैस्तु सिद्धैरमुनिभि: सदैज जुते सुभकत्या भुजगाधिपैक्ष । तत्पादपड्भेस्‍्हमेव पुण्य॑ श्रोकासुदेवस्थ नमामि नित्यम्‌
- **Translation**: 

---

### Verse 19 (Padam Puran 7.1359)
- **Original**: यस्यापि पादाष्पसि मज्जसाजा; पूते दिवे यान्ति विकल्मपासते । मोक्ष छभन्‍ते मुनयः सुतुष्टास्त॑ वासुदेव शरण प्रपद्दे
- **Translation**: 

---

### Verse 20 (Padam Puran 7.1360)
- **Original**: परादोदके तिछति यत्र किष्णोर्मड्रादितौर्थानि सदैव तत्र । पिबत्ति येज्यापि सपापदेश्यः प्रयात्ति शुद्धा: सुगृहँ मुसरें:
- **Translation**: 

---

