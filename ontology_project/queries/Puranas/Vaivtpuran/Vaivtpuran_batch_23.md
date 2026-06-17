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

### Verse 1 (Vaivtpuran 3.325)
- **Original**: कुबेरके हवाले किया और भूत-प्रेतादि भगवान्‌ दीप प्रकाश फैलाते थे और लाखों घोड़े उस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.326)
- **Original**: शह्डरको अर्पित कर दिये। रथकी शोभा बढ़ाते थे। भाँति-भाँतिके विचित्र. तदनन्तर श्रीकृष्णके चरणारविन्दोंसे द्विभुज चित्र उनमें अड्धित थे। सुन्दर रत्रमय कलश [पार्षद प्रकट हुए, जो श्यामबर्णक थे और उनकी उज्ज्वलता बढ़ा रहे थे। रत्रमय दर्पणों
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.327)
- **Original**: हाथोंमें जपमाला लिये हुए थे। वे श्रेष्ठ पार्षद और आभूषणोंसे वे सभी रथ (विमान) भरे हुए
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.328)
- **Original**: निरन्तर आनन्दपूर्वक भगवान्‌के चरणकमलोंका थे। श्वेत चँवर उनकी शोभा बढ़ा रहे थे। अग्रिमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.329)
- **Original**: ही चिन्तन करते थे। श्रीकृष्णने उन्हें दास्यकर्ममें तपाकर शुद्ध किये गये सुनहरे वस्त्र, विचित्र-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.330)
- **Original**: नियुक्त किया। बे दास यत्रपूर्वक अर्ध्य लिये विचित्र माला, श्रेष्ठ मणि, मोती, माणिक्य तथा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.331)
- **Original**: प्रकट हुए थे। वे सभी श्रीकृष्णपरायण वैष्णव हीरोंके हारोंसे वे सभी रथ अलंकृत थे। कुछ-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.332)
- **Original**: थे। उनके सारे अड्भ पुलकित थे, नेत्रोंसे अश्रु कुछ लाल रंगके असंख्य सुन्दर कृत्रिम कमल,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.333)
- **Original**: झर रहे थे और वाणी गद्द थी। उनका चित्त जो श्रेष्ट रत्नोंके सारभागसे निर्मित हुए थे, उन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.334)
- **Original**: केवल भगवच्चरणारविन्दोंके चिन्तनमें ही संलग्र रथोंको सुशोभित कर रहे थे। रहता था। द्विजश्रेष्ठ! भगवान्‌ श्रीकृष्णने उनमेंसे एक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.335)
- **Original**: इसके बाद श्रीकृष्णके दाहिने नेत्रसे भयंकर रथ तो नारायणकों दे दिया और एक राधिकाको
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.336)
- **Original**: गण प्रकट हुए, जो हाथोंमें त्रिशूल और पट्टिश देकर शेष सभी रथ अपने लिये रख लिये।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.337)
- **Original**: लिये हुए थे। उन सबके तीन नेत्र थे और तत्पश्चात्‌ श्रीकृष्णके गुह्ादेशसे पिड्नलवर्णवाले
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.338)
- **Original**: मस्तकपर चन्द्राकार मुकुट धारण करते थे। वे पार्षदोंक साथ एक पिड्भुल पुरुष प्रकट हुआ।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.339)
- **Original**: सब-के-सब विशालकाय तथा दिगम्बर थे। गुह्मदेशसे आविर्भूत होनेके कारण वे सब गुद्दाक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.340)
- **Original**: प्रज्जलित अग्नरिशिखाके समान जान पड़ते थे। कहलाये और वह पुरुष उन गुह्यकोंका स्वामी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.341)
- **Original**: वे सभी महान्‌ भाग्यशाली भैरव कहलाये। वे कुबेर कहलाया, जो धनाध्यक्षके पदपर प्रतिष्ठित
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.342)
- **Original**: शिवके समान ही तेजस्वी थे। रुरुभैरव, है। कुबेरके बामपार्श्से एक कन्या प्रकट हुई,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.343)
- **Original**: संहारभैरव, कालभैरब, असितभैरव, क्रोधभैरव, जो कुबेरकी पत्नी हुई। वह देवी समस्त
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.344)
- **Original**: भीषणभैरव, महाभैरव तथा खट्वाज्भभैरव-ये सुन्दरियोंमें मनोरमा थी, अत: उसी नामसे प्रसिद्ध
- **Translation**: 

---

