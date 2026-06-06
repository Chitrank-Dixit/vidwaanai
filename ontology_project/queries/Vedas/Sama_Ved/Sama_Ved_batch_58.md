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

### Verse 1 (Sama Ved 0.1141)
- **Original**: यह मय एक अच्य से प्रश्नवावक है तथा दूसरे अन्यय से समाधान वाचक है- 433. क ईँ व्यक्ता नर: सनीडा रुद्रस्य मर्या अथा स्वश्वा:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1142)
- **Original**: अ्रष्ज्हें व्यक्त करने वालो / (जानकारी देने वालों) एक ही आवास में (एक साथ) निवास करने वाले श्रेष्ठ अश्यों से युक्त मरुद्गणों का रुद्र से क्या सम्बन्ध है ? समाथार एक ही आवास (शरीर में रहने वाले श्रेष्ठ अश्वों (इन्द्रियों) से युक्त मरुद्गण ( प्राण, उदान, व्यान, समान, अपान आदि पंच प्राण) विशेष गतिशील शरीर के नेता रुद्र (महाप्राण) के सहचर हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1143)
- **Original**: 434. अग्ने तम्द्याएवं न स्तोमे: क्रतुं न भद् हरिस्पृशम्‌। ऋषध्यामा त ओहै:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1144)
- **Original**: है अग्निदेव ! आज हम याजकगण यज्ञ के समान (हिंतकारी), अश्व के समान गतिशील, आपके यश को बढ़ाने के लिए ऊह नामक हृटय-स्पर्शी स्तोत्रों का प्रयोग करते हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1145)
- **Original**: 435. आविर्मर्या आ वाजं बाजिनो अग्मन्‌ देवस्य सवितु: सवम्‌ ! स्वर्गाँ अर्वन्तो जयत
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1146)
- **Original**: श्र सापवेद-संहिता मानवों का कल्याण करने वाले तेजस्वी तथा शक्तिशाली सवितादेवता ने तैयार किये गये सोमरस रूपी अन्न (पोषण) को प्राप्त कर लिया है । अतएव हे याजक ! उनसे विजव प्राप्ति के लिए अश्वों तथा स्वर्ग की प्राप्ति करो
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1147)
- **Original**: 436. पवस्व सोम द्युम्नी सुधारों महाँ अवीनामनुपूर्व्य:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1148)
- **Original**: है सोमदेव ! गप्रकाशयुकत, भली-भाँति सरल धारा से पात्र में गिरते हुए, आप पूर्ववत्‌ श्रेष्ठ ही हैं । आप (यज्ञशाला में रखे हुए) पात्र में स्वतः हो भर जाएँ
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1149)
- **Original**: ड्तति त्रयस्तरिश: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1150)
- **Original**: के के के
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1151)
- **Original**: चतुर््रिश: खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1152)
- **Original**: 437. विश्वतोदावन्विश्वतो न आ भर य॑ त्वा शविष्ठमीमहे
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1153)
- **Original**: शत्रुओं को पूर्णरूप से विनष्ट करने वाले है इद्धदेव ! आप हमें सभी प्रकार की अभीष्ट सम्पत्ति प्रदान करें, जिसको प्राप्त करने के लिए हम शक्तिशाली की स्तुति करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1154)
- **Original**: 438. एप ब्रह्मा य ऋत्विय इन्द्रो नाम श्रुतों गृणे
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1155)
- **Original**: कऋतुओं के अनुकूल कार्य करने वाले, ज्ञानयुक्त, इन्द्रदेव नाम से जो प्रख्यात हैं, उनकी हम प्रार्थना करते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1156)
- **Original**: 439. ब्रह्माण इन्द्र महयन्तो अर्कैरवर्धयन्नहये हन्तवा उ
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1157)
- **Original**: अहि नाप्रक असुर के संहार के लिए विवेकयुक्त मंत्रों से अर्चना किये जाने वाले इन्द्र के यज्ञ का हम विस्तार करते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1158)
- **Original**: 440. अनवस्ते रथमश्वाय तक्षुस्त्वष्टा वच्र पुरुहूत द्युमन्‍्तम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1159)
- **Original**: हे इद्धदेव ! ऋ्भु देवों ने आपके अश्वों के लिए (अनुकूल) रथ का निर्माण किया है । अनेक त्रग्रपियों द्वारा आवाहन किये जाने बाले हे इद्धदेव ! टेवशिल्पी त्वष्टा ने आपके लिए चमकते हुए बद्र की रचना को है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1160)
- **Original**: 441. शं पद मघं रयीधिणों न काममत्रतो हिनोति न स्पृशद्रयिम्‌
- **Translation**: 

---

