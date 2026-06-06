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

### Verse 1 (Vaivtpuran 13.11722)
- **Original**: होइये और मेरा उद्धार कीजिये। हे नाथ! इस हुए थे। प्रह्मदपर अनुग्रह और वेदोंकी रक्षा गर्दभ-योनि और भवसागरसे मुझे उबारिये। मैं करनेके लिये ही आपने यह अवतार ग्रहण किया
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11723)
- **Original**: मूर्ख हूँ तो भी आपके भक्तका पुत्र हूँ; इसलिये था। दयानिधे! आपने ही राजा मनुको ज्ञान देने,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11724)
- **Original**: आपको मेरा उद्धार करना चाहिये। वेद, ब्रह्मा देवता और ब्राह्मणोंकी रक्षा करने तथा वेदोंके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11725)
- **Original**: आदि देवता तथा मुनीन्र भी जिनकी स्तुति उद्धारके लिये अंशत: मत्स्यावतार धारण क्‍ करनेमें असमर्थ हैं, उन्हीं गुणातीत परमेश्चरकी था। आप ही अपने अंशसे सृष्टिके लिये शेषके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11726)
- **Original**: स्तुति मुझ-जैसा पुरुष क्या करेगा? जो पहले आधारभूत कच्छप हुए थे। सहस्नलोचन! आप
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11727)
- **Original**: दैत्य था और अब गदहा है। करुणासागर। आप ही अंशत: शेषके रूपमें प्रकट हुए हैं और सम्पूर्ण ऐसा कीजिये, जिससे मेरा जन्म न हो। आपके विश्वका भार वहन करते हैं। आप ही जनकनन्दिनी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11728)
- **Original**: चरणारविन्दके दर्शन पाकर कौन फिर जन्म सीताका उद्धार करनेके लिये दशरथनन्दन श्रीराम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11729)
- **Original**: अथवा घर-गृहस्थीके चक्करमें पड़ेगा? ब्रह्मा हुए थे। उस समय आपने समुद्रपर सेतु बाँधा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11730)
- **Original**: जिनकी स्तुति करते हैं, उन्होंका स्तवन आज और दशमुख रावणका वध किया। पृथ्वीनाथ!
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11731)
- **Original**: एक गदहा कर रहा है। इस बातकों लेकर आप ही अपनी कलासे जमदग्रिनन्दन महात्मा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11732)
- **Original**: आपको उपहास नहीं करना चाहिये; क्योंकि परशुराम हुए; जिन्होंने इक्कोस बार क्षत्रिय
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11733)
- **Original**: सच्चिदानन्दस्वरूप एवं विज्ञ परमेश्वरकी योग्य नरेशोंका संहार किया था। सिद्धोंके गुरके भी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11734)
- **Original**: और अयोग्यपर भी समानरूपसे कृपा होती है। गुरु महर्षि कपिल अंशत: आपके ही स्वरूप हैं,, यों कहकर दैत्यराज धेनुक श्रीहरिके सामने जिन्होंने माताकों ज्ञान दिया और योग (एवं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11735)
- **Original**: खड़ा हो गया। उसके मुखपर प्रसन्नता छा रही सांख्य)-शास्त्रकी रचना की। ज्ञानिशिरोमणि
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11736)
- **Original**: थी, वह श्रीसम्पन्न एवं अत्यन्त संतुष्ट जान पड़ता नर-नारायण ऋषि आपके ही अंशसे उत्पन्न हुए
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11737)
- **Original**: था। दैत्यद्वारा किये गये इस स्तोत्रका जो प्रतिदिन हैं। आप ही धर्मपुत्र होकर लोकोंका विस्तार कर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11738)
- **Original**: भक्तिभावसे पाठ करता है, वह अनायास ही रहे हैं। इस समय आप स्वयं परिपूर्णतम परमात्मा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11739)
- **Original**: श्रीहरिका लोक, ऐश्वर्य और सामीष्य प्राप्त कर ही श्रीकृष्णरूपमें प्रकट हैं और सभी अबतारोंके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11740)
- **Original**: लेता है। इतना ही नहीं, वह इहलोकमें श्रीहरिकी सनातन बीजरूप हैं। आप यशोदाके जीवन,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11741)
- **Original**: भक्ति, अन्तमें उनका परम दुर्लभ दास्यभाव, नन्दरायजीके एकमात्र आनन्दवर्धन, नित्यस्वरूप,
- **Translation**: 

---

