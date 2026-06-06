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

### Verse 1 (Sama Ved 0.1301)
- **Original**: 496. परि झुक्ष॑ सनद्रयिं भरद्वाजं नो अन्धसा । स्वानो अर्थ पवित्र आ
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1302)
- **Original**: (हे सोम !) प्रखरता, बल और श्रेष्ठ धन अपने पुष्टिकारक रस सहित हमें प्रदान करें । आपका पवित्र रस छनने के बाद कलश में स्थिरता प्राप्त करे
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1303)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1304)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1305)
- **Original**: 497. अचिक्रददवृषा हरिर्महान्मित्रो न दर्शत:। सं सूर्येण दिद्युते
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1306)
- **Original**: मित्र के समान प्रिय शक्तिमान्‌ हरिताभ सोम, निचोड़े जाते समय शब्द करता हुआ, उसी प्रकार प्रकाशित होता है, जिस प्रकार से सूर्य प्रकाशित होता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1307)
- **Original**: 498.आ ते दक्ष मयोभुव॑ वह्िमद्या वृणीमहे । पान्तमा पुरुस्पृहम्‌ 2
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1308)
- **Original**: हे सोम्देव ! आपके हर्ष प्रदान करने वाले, सम्पत्ति देने वाले, रिपुओं से रक्षा करने वाले, अनेक लोगों द्वारा कामना किये जाने बाले बल क्घे, हम धारण करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1309)
- **Original**: 499. अध्वर्यो अद्विभि: सुतं सोम॑ पवित्र आ नय । पुनाहीन्द्राय पातवे
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1310)
- **Original**: है होताओ ! इद्धदेव के लिए पीने योग्य बनाने हेतु निचोड़े गये सोमरस को पवित्र करके, पात्र (कलश) के पास ले आओ।
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1311)
- **Original**: 500, तरत्स मन्दी धावति धारा सुतस्यान्धस: । तरत्स मन्दी धावति
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1312)
- **Original**: निकाली गई सोमरस की पृष्टिकारी धारा आनन्द प्रदान करने वाली है । वह निकृष्ट संस्कारों से रहित और उपासकों को ऊर्ध्वगति प्रदान करने वाली है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1313)
- **Original**: 501. आ पवस्व सहस्त्रिणं रयिं सोम सुवीर्यम्‌। अस्मे श्रवांसि धारय
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1314)
- **Original**: है सोम ! आप सहसों प्रकार की श्रेष्ठ, शक्तिवर्द्धक दिव्य सम्पदा तथा पोषक आहार हमें प्रदान करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1315)
- **Original**: 502. अनु प्रलास आयव: पद नवीयो अक्रमु:। रुचे जनन्त सूर्यम्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1316)
- **Original**: प्राचीनकाल में लोगों ने प्रखरता को प्राप्त करने के लिए आदित्य के समान तेजस्वी सोम को प्रकट किया और अभुपम श्रेष्ठ स्थान प्राप्त किया
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1317)
- **Original**: 503. अर्षा सोम द्युमत्तमो5भि द्रोणानि रोरुवत्‌ । सीदन्योनौ वनेष्वा
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1318)
- **Original**: हे तेजस्वी सोम ! आप शब्द करते हुए (यज्ञ) पात्र (कलश) में शुद्ध होकर स्थित हों । आप तपोवन में स्थित इस यज्ञ मण्डप में पधारें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1319)
- **Original**: 504. यृषा सोम द्ुमाँ असि वृषा देव वृषत्रतः । वृषा धर्माणि दक्षिषे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1320)
- **Original**: हे सोमदेव ! आप पराक्रमी और तेजस्वी हैं । बल बढ़ाने की क्षमता से युकत आप सदैव अपने इस धर्म (गुण) को धारण किये रहते हैं
- **Translation**: 

---

