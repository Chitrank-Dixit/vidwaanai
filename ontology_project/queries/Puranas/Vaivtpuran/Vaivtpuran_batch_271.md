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

### Verse 1 (Vaivtpuran 13.11562)
- **Original**: सिंहासनपर आसीन हैं। सबके प्रसञ्नमुखपर मन्द ; हास्यथकी छटा छा रही है और सभी भक्तोंपर $
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11563)
- **Original**: अनुग्रह करनेके लिये कातर दिखायी देते हैं। उन कर )"
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11564)
- **Original**: सबके सभी अड्भ चन्दनसे चर्चित हैं। समस्त 4
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11565)
- **Original**: चराचर जगत्‌को इस परम अद्भुत रूपमें देखकर वहाँ इन्द्र तत्काल मूच्छित हो गये। पूर्वकालमें *.
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11566)
- **Original**: गुरुने उन्हें जिस मन्त्रका उपदेश दिया था, उसका 33 04 वे वहीं जप करने लगे। उस समय उन्होंने दृदयमें 8 रु असल क 5
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11567)
- **Original**: सहस्तदल-कमलपर विराजमान उग्र ज्योतिःपुञझ भाँति धारण कर लिया। इसी समय उस नगरमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11568)
- **Original**: देखा। उस तेजोराशिके भीतर दिव्य रूपधारी, रब्रमय तेजसे प्रकाश होनेपर भी सहसा अन्धकार
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11569)
- **Original**: अत्यन्त मनोहर तथा नूतन जलधरके समान उत्कृष्ट छा गया। सारा नगर धूलसे ढक गया। मुने ! हवाके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11570)
- **Original**: श्यामसुन्दर विग्रहवाले श्रीकृष्ण दिखायी दिये। वे साथ बादलोंके समूहने आकर आकाशको घेर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11571)
- **Original**: उत्तम रत्नोंके सारतत्त्वसे निर्मित एवं प्रकाशमान लिया और वृन्दावनमें निरन्तर अतिवृष्टि होने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11572)
- **Original**: मकराकृति कुण्डलोंसे अलंकृत थे, अत्यन्त उद्दी्त लगी। शिलावृष्टि, वज़रकी वृष्टि और अत्यन्त भयानक
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11573)
- **Original**: एवं श्रेष्ठ मणियोंके बने हुए मुकुटसे उनका मस्तक उल्कापात--ये सब-के-सब गोवर्धन पर्वतका स्पर्श
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11574)
- **Original**: उद्धासित हो रहा था। प्रकाशमान उत्तम कौस्तुभरत्नसे होते ही दूर जा पड़ते थे। मुने! असमर्थ पुरुषके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11575)
- **Original**: कण्ठ और वक्ष:स्थल जगमगा रहे थे। मणिनिर्मित उद्यमकी भाँति इन्द्रका वह सादा उद्योग विफल हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11576)
- **Original**: केयूर, कंगन और मजञ्जीरसे उनके हाथ-पैरोंकी गया। वह सब कुछ व्यर्थ होता देख इन्द्र उसी क्षण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11577)
- **Original**: बड़ी शोभा हो रही थी। भीतर और बाहर समान रोपसे भर गये और उन्होंने दधीचिकी हड्डियोंसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11578)
- **Original**: रूपमें ही देखकर परमेश्वर श्रीकृष्णका उन्होंने बने हुए अपने अमोघ वज्रास्त्रको हाथमें ले लिया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11579)
- **Original**: स्तवन किया। इन्द्रकों वज्र हाथमें लिये देख मधुसूदन हँसने लगे। इचख्र बोले--जो अविनाशी, परत्रह्म, ज्योति:- उन्होंने इन्द्रके हाथसहित अत्यन्त दारुण वज़्को ही
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11580)
- **Original**: स्वरूप, सनातन, गुणातीत, निराकार, स्वेच्छामय स्तम्भित कर दिया। इतना ही नहीं, उन सर्वव्यापी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11581)
- **Original**: और अनन्त हैं; जो भक्तोंके ध्यान तथा आराधनाके परमात्माने देवगणोंसहित मेघको भी स्तब्ध कर
- **Translation**: 

---

