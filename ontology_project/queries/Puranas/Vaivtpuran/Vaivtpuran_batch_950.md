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

### Verse 1 (Vaivtpuran 543.17314)
- **Original**: श्रीकृष्णको आते देखा। उनका परम सौन्दर्यशाली माधवने यादवों, देवों, मुनियों तथा अन्यान्य
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17315)
- **Original**: सुन्दर बालक-बेष था। बे मन्द-मन्द मुस्करा रहे व्यक्तियों और देवियोंके साथ गणेश-पूजनका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17316)
- **Original**: थे। उनके शरीरकी कान्ति नवीन मेघके समान कार्य सम्पन्न किया। तत्पश्चात्‌ वे अपने एक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17317)
- **Original**: श्याम थी; वे रेशमी पीताम्बर धारण किये हुए अंशसे रुक्मिणी आदि देवियोंके साथ रमणीय
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17318)
- **Original**: थे; उनका सर्वाज्भ चन्दनसे अनुलिप्त था; रत्नोंके ट्वारकापुरीको चले गये; किंतु स्वयं साक्षात्रूपसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17319)
- **Original**: आभूषण उन्हें सुशोभित कर रहे थे; उनकी सिद्धाश्रममें ही ठहर गये। वहाँ वे गोलोकवासी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17320)
- **Original**: शिखामें मयूर-पिच्छ शोभा दे रहा था; वे गोप-सखाओं, नन्‍्द तथा माता यशोदा-गोपीके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17321)
- **Original**: मालतीकी मालासे विभूषित थे; उनका प्रसन्नमुख साथ प्रेमपूर्वक वार्तालाप करके पुन: माता, पिता,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17322)
- **Original**: मन्द हास्यकी छटा बिखेर रहा था; वे साक्षात्‌ गोकुलवासी गोषों तथा बन्धुवर्गोंसे नीतियुक्त
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17323)
- **Original**: भक्तानुग्रहमूर्ति थे तथा मनोहर प्रफुल्ल क्रोडाकमल यथोचित वचन बोले। लिये हुए थे; उनके एक हाथमें मुरली और दूसरे श्रीभगवानने कहा--पिताजी ! अब अपने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17324)
- **Original**: हाथमें सुप्रशस्त दर्पण शोभा पा रहा था। उन्हें भ्रजको लौट जाओ। परम श्रेष्ठ यशस्विनी माता
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17325)
- **Original**: देखकर राधा तुरंत ही गोपियोंके साथ उठ खड़ी यशोदे! तुम भी उत्तम गोकुलको जाओ और वहाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17326)
- **Original**: हुईं और परम भक्तिपूर्वक उन परमेश्वरको सादर आयुके शेष कालपर्यन्त भोगोंका उपभोग करो।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17327)
- **Original**: प्रणाम करके उनकी स्तुति करने लगीं। इतना कहकर भगवान्‌ श्रीकृष्ण माता-पिताकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17328)
- **Original**: राधिका बोलीं--नाथ ! तुम्हारे मुखचन्द्रको आज्ञा ले राधिकाके स्थानको चले गये तथा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17329)
- **Original**: देखकर आज मेरा जन्म लेना सार्थक और नन्दजी गोकुलको प्रस्थित हुए। वहाँ पहुँचकर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17330)
- **Original**: जीवन धन्य हो गया तथा मेरे नेत्र और मन श्रीकृष्णने मुस्कराती हुई सुन्दरी राधाकों देखा।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17331)
- **Original**: परम प्रसन्न हो गये। पाँचों प्राण स्नेहाद्दर और उनकी तरुणता नित्य स्थिर रहनेबाली थी, जिससे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17332)
- **Original**: आत्मा हर्षविभोर हो गया; दुर्लभ बन्धुदर्शन उनकी अवस्था द्वादश वर्षकी थी। मोतियोंका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17333)
- **Original**: दोनों (द्रष्टा और दृश्य)-के हर्षका कारण होता हार उनको शोभा बढ़ा रहा था; वे रलनिर्मित
- **Translation**: 

---

