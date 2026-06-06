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

### Verse 1 (Vaivtpuran 7.6185)
- **Original**: यह तेज अन्तर्धान हो गया। तब देवताओंने थी। उसके ललाटपर चन्दनकी खौर लगी थी।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.6186)
- **Original**: कृपापरवश हो सनत्कुमारकों समझाया और वैष्णवाश्व साकारं॑ कमनीय॑ मनोहरम्‌ । द्विपुज॑ कमनीय॑ च किशोर श्यामसुन्दरम्‌ । एवं तेजस्विनं भक्ता: सेवन्ते सततं मुदा । तत्‌ तेजो बिभ्रतां देव देवानां तेजसा पुरा । नित्या तेज:स्वरूपाहं विधृत्य विग्रह॑ विभो । मायया त़ब मायाहं मोहयित्यासुरानू पुरा । ततो5ह॑. संस्तुता देवैस्तारकाक्षेण. पीडितै: । त्वक्वा देह दक्षयज्ञे शिवाह. शिवनिन्दया '/ अभवव शैलजायायां शैलाधीशस्य कर्मणा। अनेकतपसा प्राप्ःः शिवश्षात्राप जन्मनि ।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.6187)
- **Original**: । श्रुत्वा सर्व कृपासिन्धो कृषां मां कर्तुमहसि भारते पार्व॑तीस्तोत्रं यः सृणोति सुसंयतः संवत्सर ह॒विष्याशी हरिमध्यर्व्य भक्तित: विष्णुस्तोत्रमिदं ब्रह्मन्‌ सर्वसम्पत्तिवर्धनम्‌ सर्वसौन्दर्यबीजं च यशोराशिविवर्धनम्‌ सुखरद॑ मोक्षद॑ सार॑ स्वामिसौभाग्यवर्धनम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.6188)
- **Original**: हरिभक्तिप्रदं तत्त्नज्ञानबुद्धिविवर्धनम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.6189)
- **Original**: (गणपतिखण्ड 7। 109-131)
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.6190)
- **Original**: *+ गणपतिखएण्ड « करे 144
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.6191)
- **Original**: 0004 04 । 4 44
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.6192)
- **Original**: . 444 40404 4 4 44.44. 44 340440304%030550%333444%%%334<<>न >> >> कक ### # कक 8 #####%%% उन्होंने उन उमारहित दिगम्बर शिवको प्रसन्नचित्तताली
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.6193)
- **Original**: मु्त शरणागतकी रक्षा करों। माता! ओ माता! पार्वतीको लौटा दिया। फिर तो विश्वकों आनन्दित
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.6194)
- **Original**: तुम तो जगत्‌की माता हो, फिर मैं जगत्से बाहर करनेवाली दुर्गाने ब्राह्मणोंको अनेक प्रकारके रत्न
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.6195)
- **Original**: थोड़े ही हूँ; अतः शीघ्र आओ। भला, अपनी तथा भिक्षुओं और बन्दियोंको सुवर्ण दान किये।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.6196)
- **Original**: माताके रहते हुए मैं किस कारण तृष्णासे पीड़ित ब्राह्मणों, देवताओं तथा पर्वतोंकों भोजन कराया।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.6197)
- **Original**: हो रहा हूँ? ब्राह्मणकी दीन वाणी सुनकर शिव- सर्वोत्तम उपहारोंद्वारा शंकरजीकी पूजा की, बाजा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.6198)
- **Original**: पार्वती उठे। इसी समय शिवजीका शुक्रपात हो बजवाया, माड्लिक कार्य कराये और श्रीहरिसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.6199)
- **Original**: गया। बे पार्वतीके साथ द्वारपर आये। वहाँ उन्होंने सम्बन्ध रखनेवाले सुन्दर गीत गवाये। इस प्रकार
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.6200)
- **Original**: उस वृद्ध तथा दीन ब्राह्मणको देखा जो वृद्ध- दुर्गाने ब्रतकों समाप्त करके परम उल्लासके साथ
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.6201)
- **Original**: अवस्थासे अत्यन्त पीड़ित था। उसके शरीरमें दान देकर सबको भोजन कराया। तत्पश्चात्‌ अपने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.6202)
- **Original**: झुर्रियाँ पड़ गयी थीं। वह डंडा लिये हुए था स्वामी शिवजीके साथ स्वयं भी भोजन किया।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.6203)
- **Original**: और उसकी कमर झुक गयी थी। वह तपस्वी इसके बाद उत्तम पानके सुन्दर बीड़े, जो कपूर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.6204)
- **Original**: होते हुए भी अशान्त था। उसके कण्ठ, ओठ आदिसे सुवासित थे, क्रमशः सबको देकर
- **Translation**: 

---

