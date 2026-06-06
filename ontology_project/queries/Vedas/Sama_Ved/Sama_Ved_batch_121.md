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

### Verse 1 (Sama Ved 0.2401)
- **Original**: धर्मणा वायुमारुहः
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2402)
- **Original**: भली- भाँति विचारपूर्वक स्थापित किये गये, हे संस्कारित सोम ! आप अपने स्वाभाविक गुण से वायुदेव के साथ संयुक्त होकर, कलश में प्रतिष्ठित हों
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2403)
- **Original**: 922.तवाहं सोम रारण सख्य इन्दो दिवेदिवे । पुरूणि बश्चो नि चरन्ति मामव परिधी रति ताँ इहि
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2404)
- **Original**: हे दीप्तिमान्‌ सोम ! आपसे मित्रता करने के लिए हम निरन्तर प्रयललशील हैं । दुष्ट-दुराचारी हमें पीड़ित कर रहे हैं। आप उन शत्रुओं का विनाश करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2405)
- **Original**: 923-तवाहं नक्तमुत सोम ते दिवा दुहानो बश्च ऊधनि। घृणा तपन्तमति सूर्य पर: शकुना इब पप्तिम
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2406)
- **Original**: हे समुज्ज्वल सोम ! हमें दिन-रात आपका सामीष्य प्राप्त हो । हम, सुदूर चमकने वाले सूर्यदेव तथा आपको, पक्षो की भाँति (प्रत्यक्ष गतिशील) देखते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2407)
- **Original**: 924.पुनानो अक्रमीदभि विश्वा मृधो विचर्षणि: । शुम्भन्ति विप्र॑ धीतिभि:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2408)
- **Original**: याजकगण, शुद्ध होने वाले, सबकी समीक्षा करके शत्रुओं का विनाश करने वाले, सोमदेव की विभिन्‍न स्तुतियों से शोभा बढ़ाते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2409)
- **Original**: 925. आ योनिमरुणो रुहह्रमदिन्द्ों वृषा सुतम्‌। धरुवे सद्सि सीदतु
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2410)
- **Original**: विधिवत्‌ तैयार किया गया अरुणाभ सोम, कलश में स्थिर होता है । इसके बाद सभा मण्डप में श्रेष्ठ स्थान चर बैठने वाले शक्तिमान्‌ इन्द्रदेव, उस सोमरस के पास (पीने के लिए) जाते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2411)
- **Original**: 926.नू नो रचखिं महामिन्दो5स्मभ्यं सोम विश्वतः । आ पवस्व सहस्रिणम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2412)
- **Original**: हे तृप्तिदायक सोम ! आप हमें शीघ्र ही, हजारों प्रकार का महान्‌ वैभव, सभी ओर से प्रदान करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2413)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2414)
- **Original**: 5.6 सामठेद-संहिता
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2415)
- **Original**: पंचम: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2416)
- **Original**: 927.पिबा सोममिद् मन्दतु त्वा य॑ ते सुषाव हर्यश्राद्धि: । सोतुर्बाहुभ्यां सुयतो नार्वा
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2417)
- **Original**: है अश्वपति इन्द्रदेव ! याजक द्वारा अपने हाथों से, पत्थर के सहयोग से निकाला गया सोमरस, आपके लिए अश्व-शक्ति जैसे गुणों से युक्त एवं आनन्दवर्द्धक सिद्ध हो । आप इसका पान करें
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2418)
- **Original**: 928.वस्ते मदो युज्यश्नारुरस्ति येन वृत्राणि हर्यश्व हंसि । स त्वामिन्द्र प्रभूवसो ममत्तु
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2419)
- **Original**: घोड़ों के स्वामी, हे समृद्धिशाली इन्द्रदेव ! जिस सोमरस के उत्साह द्वारा आप वृत्रासुर (दुष्टों) का हनन करते हैं, वह श्रेष्ठ रस आपको आनन्द प्रदान करें
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2420)
- **Original**: 929.बोधा सु मे मघवन्वाचमेमां यां ते वसिष्ठो अर्चति प्रशस्तिम्‌ । इमा ब्रह्म सधमादे जुघस्व
- **Translation**: 

---

