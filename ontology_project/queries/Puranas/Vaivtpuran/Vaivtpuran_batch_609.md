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

### Verse 1 (Vaivtpuran 55.5165)
- **Original**: दक्षिणावर्त्शइखस्थ॑ सदूर्वापुष्पचन्दनम्‌। अनुलेपन, धूप, दीप, सुन्दर पुष्प, स्नानीय, रत्रभूषण,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.5166)
- **Original**: पूतं युक्त तीर्थतोयै राधेउर्घ्य॑प्रतिगृह्मताम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.5167)
- **Original**: विविध नैवेद्य, सुवासित ताम्बूल, जल, मधुपर्क। राधे! दक्षिणाबर्त शड्खमें रखा हुआ दूर्वा, तथा रत्रमयी शय्या--ये सोलह उपचार हैं। राजाने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.5168)
- **Original**: पुष्प, चन्दन तथा तीर्थजलसे युक्त यह पवित्र इनमेंसे प्रत्येकको वेदमन्त्रके उच्चारणपूर्वक भक्तिभावसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.5169)
- **Original**: अर्घ्य प्रस्तुत है। इसे स्वीकार करो। अर्पित किया। शिवे! इन उपचारोंके समर्पणके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.5170)
- **Original**: (5) गन्ध लिये जो सर्वसम्मत मन्त्र हैं, उन्हें सुनो।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.5171)
- **Original**: पार्थिवद्रब्यसम्भूतमतीवसुरभीकृतम्‌ । (1) आसन मड्ूलाहँ पवित्र च॒ राधे गन्ध॑ गृहाण मे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.5172)
- **Original**: सत्रसारविकार च॒ निर्मित विश्वकर्मणा। राधे! पार्थिव द्रव्योंसे सम्भूत अत्यन्त सुगन्धित बर॑ सिंहासन रम्यं राधे पूजासु गृह्ताम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.5173)
- **Original**: मज्जलोपयोगी तथा पवित्र गन्ध मुझसे ग्रहण करो। राधे! पूजाके अवसरपर विश्वकर्मद्वारा रचित (6 ) अनुलेपन ( चन्दन ) रमणीय श्रेष्ठ सिंहासन, जो रत्नसारका बना हुआ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.5174)
- **Original**: श्रीखण्डचूर्ण सुस्त्रिग्ध कस्तूरीकुड्डुमान्वितम्‌। है, ग्रहण करो।* सुगन्धयुक्त देवेशि .गृह्मतामनुलेपनम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.5175)
- **Original**: (2) बसन देवेश्वरि! कस्तूरी, कुड्डूम और सुगन्धसे युक्त अमूल्यरत्रखचितममूल्य॑. सूक्ष्मेव. च।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.5176)
- **Original**: यह सुख्त्रिग्ध चन्दनचूर्ण अनुलेपनके रूपमें तुम्हारे वहिशुद्ध॑ निर्मल॑ च्व बसन॑ देवि गृहाताम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.5177)
- **Original**: सामने प्रस्तुत है। इसे स्वीकार करो। देवि! बहुमूल्य रत्रोंसे जटित सूक्ष्म वस्त्र, (7) धूप जिसका मूल्य आँका नहीं जा सकता, -आपकौ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.5178)
- **Original**: बृक्षनिर्याससंयुक्त पार्थिवद्रव्यसंयुतम्‌। सेवामें प्रस्तुत है। यह अग्रिसे शुद्ध किया
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.5179)
- **Original**: अग्निखण्डशिखाज़ातं भूप॑ देवि गृहाण मे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.5180)
- **Original**: गया, चिन्मय एवं स्वभावत: निर्मल है। इसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.5181)
- **Original**: देवि! वृक्षकी गोंद (गुग्गुल) तथा पार्थिव स्वीकार करो। द्रव्योंसे संयुक्त यह धूप प्रज्थलित अग्निशिखासे (3) पाद्य निर्गत धूमके रूपमें प्रस्तुत है। मेरी इस वस्तुको सद्रत्नसारपात्रस्थ॑ सर्वतीर्शोंदक॑ शुभम्‌।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.5182)
- **Original**: ग्रहण करो। पादप्रक्षालनार्थ चर राधे पाहां च गृह्मताम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.5183)
- **Original**: (8 ) दीप राधे! उत्तम रब्नसारद्वारा निर्मित पात्रमें सम्पूर्ण अन्धकारे भयहरममूल्यमणिशोभितम्‌। तीर्थोंका शुभ जल तुम्हारी सेवामें अर्पित किया
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.5184)
- **Original**: रक्रप्रदीष॑ शोभाद्य॑ं गृहाण परमेश्वरि
- **Translation**: 

---

