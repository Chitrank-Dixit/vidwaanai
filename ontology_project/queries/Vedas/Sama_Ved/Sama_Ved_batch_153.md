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

### Verse 1 (Sama Ved 0.3041)
- **Original**: तृतीय॑ धाम महिषः सिघासन्त्सोमो विराजमनु राजति प्टुप्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3042)
- **Original**: ऋद्षियों की भाँति संस्कार वाला, ऋषित्व प्रदान करने वाला, स्तुत्य, ज्ञानदायी, सोम स्वयं महान्‌ है। यह तृतीय धाम (घ्युलोक) स्वर्गलोक में रहने वाले तेजस्वी इद्धदेव को और अधिक तेज सम्पन्न बनाता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3043)
- **Original**: 1177, चमूषच्छ््चेनः शकुनो विभृत्वा गोविन्दुर्द्रपप आयुधानि बिभ्रत्‌ । अपामूर्मि सचमान:ः समुद्र तुरीयं धाम महिषो विवक्ति
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3044)
- **Original**: यह प्रशंसनीय, सभी सामर्थ्यों से युक्त, शक्तिमान्‌ समुद्र को तरंगों के समान गतिमान्‌, गो -दुग्ध में मिलाया जाने वाला, प्रवाही सोम चतुर्थ (मह:) लोक में विराजित होता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3045)
- **Original**: 1978, एते सोमा अभि प्रियमिन्द्रस्थ काममक्षरन्‌ । वर्धन्तो अस्य वीर्यम्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3046)
- **Original**: इन्द्रदेव की सामर्थ्य में वृद्धि करने बाला यह सोम इन्द्रदेव को प्रिय लगने वाले रसों की वर्षा करता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3047)
- **Original**: 1179. पुनानासश्चमूषदो गच्छन्तो वायु मश्विना । ते नो धत्त सुवीर्यम्‌ ।
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3048)
- **Original**: हे शुद्ध सोम ! आप वायु और अश्वनीकुमारों के साथ मिलकर हमें वीरोचित श्रेष्ठता प्रदान करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3049)
- **Original**: 1180, इन्द्रस्य सोम राधसे पुनानो हार्दि चोदय । देवानां योनिमासदम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3050)
- **Original**: हे पवित्र सोमदेव ! आप इन्द्रदेव की आराधना के लिए हमारे हृदय में प्रेरणा उत्पन्न करें । हम देवों के अनुकूल यज्ञ कर्म हेतु प्रस्तुत हुए हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3051)
- **Original**: 1181. मृजन्ति त्वा दश क्षिपो हिन्वन्ति सप्त धीतय:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3052)
- **Original**: अनु विप्रा अमादिषुः
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3053)
- **Original**: हे सोमदेव ! आपको दसों अँगुलियाँ संयुक्‍त होकर परिशोधित करती हैं । सात होतागण आपको तृप्त करते हैं । श्रेष्ठ पुरुष आपके अनुगामी बन कर आपकी प्रसनता प्राप्त करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3054)
- **Original**: 1182. देवेभ्यस्त्वा मदाय क॑ सृजानमति मेष्य:। सं गोभिवासयामसि
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3055)
- **Original**: शोधित होने वाले सुखदाता, आनन्दवर्द्धक हे सोमदेव ! आपको देवताओं को आनन्दित करने के लिए हम गो-दुग्ध में मिलाते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3056)
- **Original**: 9.2 सामवेद-संहिता 1183. पुनानः कलशेष्वा वस्त्राण्यरुषो हरि: । परि गव्यान्यव्यत
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3057)
- **Original**: शुद्ध होकर कलश में स्थापित होने वाले हरिताभ सोम को गो-दुग्ध धारण कर लेता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3058)
- **Original**: 1184. मघोन आ पवस्व नो जहि विश्वा अप द्विष: । इन्दों सखायमा विश ।
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3059)
- **Original**: हे सोमदेव ! आप हमें धन-ऐश्वर्य से युक्त करने के लिए पवित्र हों । द्वेष करने वालों का नाश करें और साथी इन्द्रदेव के साथ एकाकार हो जाएँ
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3060)
- **Original**: 1185. नृचक्षसं त्वा वयमिद्धपीतं स्वर्विदम्‌। भक्षीमहि प्रजामिषम्‌
- **Translation**: 

---

