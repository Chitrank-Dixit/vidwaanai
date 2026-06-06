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

### Verse 1 (Vaivtpuran 4.8887)
- **Original**: हुए इन सातों द्वारॉको पार करनेपर वह आश्रम वे मड्गलकलश उभयपार्श्वनें उस राजमार्गकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8888)
- **Original**: सोलह द्वारोंसे युक्त है। देवताओंने देखा--ठसकी शोभावृद्धि करते थे। क्रौडामें तत्पर हुई झुंड-की-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8889)
- **Original**: चहारदीवारी सहस्न धनुष ऊँची है। उत्तम रज्नोंके झुंड गोपिकाएँ उस मार्गको घेरे खड़ी थीं।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8890)
- **Original**: बने हुए अत्यन्त मनोहर छोटे-छोटे कलशोंके उपर्युक्त मनोरम प्रदेश चन्दन, अगुरु, कस्तूरी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8891)
- **Original**: समुदाय अपने तेजसे उस परकोटेको उद्धासित और कुंकुमके द्रवसे चर्चित थे। बहुमूल्य रत्रोंस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8892)
- **Original**: कर रहे हैं। उसे देखकर देवताओंको बड़ा यहाँ मणिमय स़ोपानोंका निर्माण किया गया था।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8893)
- **Original**: विस्मय हुआ। वे उसकी परिक्रमा करते हुए बड़ी कुल मिलाकर सोलह द्वार थे, जो अग्निशुद्ध प्रसन्नताके साथ कुछ दूर और आगे गये। सामने रमणीय चिन्मय बस्त्रों, श्वेत चामरों, दर्पणों,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8894)
- **Original**: चलते हुए वे इतने आगे बढ़ गये कि वह आश्रम रज्ममयी शय्याओं तथा विचित्र पुष्पमालाओंसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8895)
- **Original**: उनसे पीछे हो गया। मुने! तदनन्तर उन्होंने गोपों शोभायमान थे। बहुत-से द्वारपाल उन प्रदेशोंकी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8896)
- **Original**: और गोपिकाओंके उत्तम आश्रम देखे, जिनमें रक्षा करते थे। उनके चारों ओर खाइयाँ थीं और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8897)
- **Original**: बहुमूल्य रत्न जड़े हुए हैं। उनकी संख्या सौ लाल रंगके परकोटोंसे जे घिरे हुए थे। इन मनोरम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8898)
- **Original**: करोड़ है। इस प्रकार सब ओर गोपों और प्रदेशोंका दर्शन करके देवता वहाँसे आगे बढ़नेको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8899)
- **Original**: गोपिकाओंके सम्पूर्ण आश्रमको तथा अन्य नये- उद्यत हुए। वे जल्दी-जल्दी कुछ दूरतक गये।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8900)
- **Original**: नये रमणीय स्थलोंको देखते-देखते उन देवेश्वरोंने तब वहाँ उन्हें रासेश्वरी श्रीराधाका आश्रम दिखायी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8901)
- **Original**: समस्त गोलोकका निरीक्षण किया। वह सब दियां। नारद! देवताओंकी आदिदेवी गोपीशिरोमणि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8902)
- **Original**: देखकर उनके शरीरमें रोमाश्न हो आया। तदनन्तर श्रीकृष्णप्राणाधिका राधिकाका बह निवासस्थान
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8903)
- **Original**: फिर वही गोलाकार रम्य वृन्दावन, शतश्ृंग पर्वत बड़ा ही सुन्दर बनाया गया था। रमणीय द्रव्योंक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8904)
- **Original**: तथा उसके बाहर विरजा नदी दिखायी दी। विरजा कारण उसकी मनोहरता बहुत बढ़ गयी थी।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8905)
- **Original**: नदीके बाद देवताओंने सब कुछ सूना ही देखा। वहाँका सब कुछ सबके लिये अनिर्वचनीय था।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8906)
- **Original**: वह अद्भुत गोलोक उत्तम रत्रोंसे निर्मित तथा बड़े-से-बड़े विद्वान्‌ भी उस स्थानका सम्यक्‌
- **Translation**: 

---

