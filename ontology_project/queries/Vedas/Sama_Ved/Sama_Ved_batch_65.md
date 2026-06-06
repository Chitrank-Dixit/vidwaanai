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

### Verse 1 (Sama Ved 0.1281)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1282)
- **Original**: 487.उपो घु जातमप्तुरं गोभिर्भडूं परिष्कृतम्‌। इन्दुं देवा अयासिषु:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1283)
- **Original**: शत्रु-संहारक, भलीप्रकार से तैयार, जल और गोदुग्ध में मिला हुआ, यह सोमरस देवगणों को तृप्ति देने बाला सिद्ध हो
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1284)
- **Original**: 488.पुनानो अक्रमीदभि विश्वा मृथो विचर्षणि: । शुम्भन्ति विप्रं धीतिपि:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1285)
- **Original**: बुद्धिवर्द्धक, पवित्र डोने के बाद ज्ञानवर्धक यह सोमरस सभी शत्रुओं (विकारों) का शमन करता है । उस सोम की ज्ञानी-जन दिव्य स्तोत्रों से स्तुति करते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1286)
- **Original**: 489. आविशन्कलशं सुतो विश्वा अर्पन्नभि श्रिय:। इन्दुरिन््राय धीयते
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1287)
- **Original**: यह परिष्कृत सोमरस, कलश में भरे जाते समय सुशोभित होता है, जो इन्द्रदेव की प्रसन्‍नता के लिए उन्हें प्रदान किया जाता है
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1288)
- **Original**: 490. असर्जि रथ्यो यथा पवित्रे चम्बोः सुतः
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1289)
- **Original**: कार्ष्मन्वाजी न्यक्रमीत्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1290)
- **Original**: नियच्त रथ के घोड़े की तरह, निचोड़ा गया सोमरस सावधानीपूर्वक पात्र में भरा जाता है । वह बलवान्‌ सोम देवताओं को अपनी ओर आकर्षित करने में समर्थ है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1291)
- **Original**: 491 .प्र यदगावो न भूर्णयस्त्वेघा अयासो अक्रमुः । घ्नन्तः कृष्णामप त्वचम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1292)
- **Original**: प्रकाशयुक्त और तेज गमनशील सोम अपनी काली त्वचा (छाल) को दूर करते हुए, यज्ञ में उसी प्रकार अ्रवेश करता है, जिस प्रकार गौएँ (त्वरित गति से) गोष्ठ में जाती हैं।
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1293)
- **Original**: 492. अपस्नन्पवसे मृथः क्रतुवित्सोम मत्सर: । नुदस्वादेवयुं जनम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1294)
- **Original**: है सोमदेव ! आप आनन्द प्रदायक, यज्ञ विधा के ज्ञाता हैं । जिस प्रकार विकारों का शमन करते हुए आप पवित्र होते हैं, उसी प्रकार देवत्य के विरोधियों का शमन करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1295)
- **Original**: 493. अया पवस्व धारया यया सूर्यमरोचय: । हिन्वानो मानुधीरप:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1296)
- **Original**: हे सोम ! मानवों के (हित सम्पादन के) लिए, पानी को (बरसने के लिए) प्रेरणा देते हुए, जिस प्रकार (अपनी क्षमता से ) आपने सूर्यदेव को आलोकित किया, उसी धारा (क्षमता) से आप पात्र में पवित्र होकर प्रवेश करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1297)
- **Original**: ड94. स पवस्व य आविधेदन्द्रं बृत्राय हन्तवे । बद्विवांसं महीरप:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1298)
- **Original**: है सोमटेव ! आप जल-प्रवाह को (बरसने से) रोकने वाले वृत्र को मारते के लिए, इद्धदेव को प्रोत्साहित करें और (वेगव्ती) धारा के साथ कलश में छनते जाएँ
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1299)
- **Original**: 54 सापवेद-संकिता 495. अया बीती परि स्रव यस्त इन्दो मदेष्वा । अवाहन्नवतीर्नव
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1300)
- **Original**: हे सोम ! इन्द्रदेव के सेवनार्थ आप कलश में स्थित हों । आपका यह रस युद्ध में शत्रुओं के सभी नगरों को नष्ट करने के लिए, इन्द्रदेव को सामर्थ्य प्रदान करता है
- **Translation**: 

---

