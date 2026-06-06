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

### Verse 1 (Sama Ved 0.2301)
- **Original**: ययाति नाहुष 872-874 । पवित्र आड्रिस 875-877
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2302)
- **Original**: सोभरि काण्व 878-879 । गोषृक्ति-अश्वसूक्ति काण्वायन 880-882 । तिरश्ली आड्रिस 883-885 । देखता- पवमान सोम 830-843, 856-861, 869-877
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2303)
- **Original**: अग्नि 844-646, 878, 879
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2304)
- **Original**: मित्रावरुण 847-849 ।इन्द्र 850,852,862-868,880-885 । मरुदगण 851 ।इद्धार्नी 853-855 । छन्द- गायत्रो 830-855, 869-8761 । बार्हत प्रगाथ (विषमा बहती, समा सतोबूहती) 856, 857, 862, 863, 867, 868 । द्विपदा विराट गायत्री 858 । ब्रिप्टूप्‌ 859-866 । बृहती 864-866 । अनुष्टुप्‌ 872-874, 883-885 । जगती 875-877 । काकुभ प्रगाथ (विषमा ककुप्‌ समा सतोबृहती) 878, 879 । उष्णिक्‌ू 880-882
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2305)
- **Original**: इति चतुर्थो ध्याय:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2306)
- **Original**: ++3+ कक फरििनन-----
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2307)
- **Original**: अथ पज्चमो< ध्याय:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2308)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2309)
- **Original**: 886.प्र त आश्विनी: पवमान धेनवो दिव्या असुग्रन्ययसा धरीमणि। प्रान्तरिक्षात्स्थाविरीस्ते असुक्षत ये त्वा मृजन्त्यूषिषाण वेधसः
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2310)
- **Original**: हे पवित्र सोमदेव ! दिव्य रस से परिपूर्ण आपकी धाराएँ वाणों के प्रवाह के साथ कलश में पहुँचती हैं । “संस्कारित करने वाले विद्रान्‌ ऋषि आपको ऊपर के पात्र से नीचे के पात्र में डालते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2311)
- **Original**: 887.उभयत: पवमानस्य रश्मयो धुवस्य सतः परि यन्ति केतव:। यदी पवित्रे अधि मृज्यते हरि: सत्ता नि योनौ कलशेषु सीदति
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2312)
- **Original**: पवित्रता को प्राप्त हुआ, संस्कारित, हरिताभ सोम पात्रों में स्थिर होता है । उसकी सुवास चतुर्दिक्‌ फैलती एवं पवित्रता का संचार करती है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2313)
- **Original**: <88.विश्वा धामानि विश्वचक्ष ऋभ्वस: प्रभोष्टे सतः परि यन्ति केतव: । व्यानशी पवसे सोम धर्मणा पतिर्विश्वस्थ भुवनस्य राजसि
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2314)
- **Original**: हे सर्वदर्शी, व्यापक स्वभाव वाले सोमदेव ! आपकी दीर्घ रश्मियों का प्रभाव सर्वत्र फैला हुआ है । अपने स्वाभाविक धर्म से शुद्ध टोने वाले आप अखिल विश्व के स्वामी के रूप में सुशोभित हो रहे हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2315)
- **Original**: 889.पवमानों अजीजनद्विवश्षित्र॑ न तन्यतुम्‌। ज्योतिर्वैश्वानरं बृहत्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2316)
- **Original**: प्रवित्ता को प्राप्ध हुआ सोम, द्युलोक में तेजस्वी वैश्वानर की विलक्षण शक्ति को विद्युत्‌ की तरह प्रकट करता हुआ, देदीप्यमान होता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2317)
- **Original**: हु 890.पवमान रसस्तव मदो राजन्नदुच्छुन:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2318)
- **Original**: वि वारमव्यमर्षति
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2319)
- **Original**: है सुशोभित होने वाले पवित्र सोमट्रेव ! दुराचारियों के लिए दुर्लभ, उत्साह बढ़ाने वाला आपका दिव्य रस ऊन के छन्‍्ने से भलीप्रकार शुद्ध किया जाकर, संगृहीत होता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2320)
- **Original**: 891.पवमानस्य ते रसो दक्षो वि राजति द्युमान्‌। ज्योतिर्विश्व॑ स्वर्दशे
- **Translation**: 

---

