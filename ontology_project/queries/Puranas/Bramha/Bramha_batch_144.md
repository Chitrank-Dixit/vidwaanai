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

### Verse 1 (Bramha 0.2861)
- **Original**: शिव-इन देवताओंसे हुआ है। इसी प्रकार है--यह बात सत्य है, सत्य है, सत्य है। समुद्रके
- **Translation**: 

---

### Verse 2 (Bramha 0.2862)
- **Original**: दक्षिणसमुद्र तथा विन्ध्यपर्वतके बीचमें भी छः जलसे घिरे हुए पुरुषोत्तमतीर्थका एक बार भी
- **Translation**: 

---

### Verse 3 (Bramha 0.2863)
- **Original**: देवसम्भव नदियाँ हैं। ये बारह नदियाँ प्रधानरूपसे दर्शन कर लेनेपर तथा ब्रह्मविद्याका एक बार बोध
- **Translation**: 

---

### Verse 4 (Bramha 0.2864)
- **Original**: बतलायी गयी हैं। गोदावरी, भीमरथी, तुड्डभद्रा, हो जानेपर मनुष्य फिर गर्भमें नहीं आता। जहाँ
- **Translation**: 

---

### Verse 5 (Bramha 0.2865)
- **Original**: कृष्णबेणी, तापी और पयोष्णी--ये विन्ध्यपर्वतके भगवान्‌ विष्णुका संनिधान है, उस उत्तम
- **Translation**: 

---

### Verse 6 (Bramha 0.2866)
- **Original**: दक्षिणकी नदियाँ हैं। भागीरथी, नर्मदा, यमुना, पुरुषोत्तमक्षेत्रमें एक वर्ष अथवा एक मासतक
- **Translation**: 

---

### Verse 7 (Bramha 0.2867)
- **Original**: सरस्वती, विशोका और वितस्ता--ये विन्ध्याचल भगवान्‌की उपासना करे। ऐसा करनेवाले पुरुषने
- **Translation**: 

---

### Verse 8 (Bramha 0.2868)
- **Original**: और हिमालय पर्वतसे सम्बन्ध रखनेवाली नदियाँ जप, होम तथा भारी तपस्या की है। वह उस
- **Translation**: 

---

### Verse 9 (Bramha 0.2869)
- **Original**: हैं। इन पुण्यमयी नदियोंको देवतीर्थ बताया गया परम धाममें जाता है, जहाँ साक्षात्‌ योगेश्वर श्रीहरि
- **Translation**: 

---

### Verse 10 (Bramha 0.2870)
- **Original**: है। गय, कोह्लासुर, वृत्त, त्रिपुर, अन्धक, हयमूर्धा, विराजमान रहते हैं। लवण, नमुचि, थृज्जक, यम, पातालकेतु, मय तथा सुनियोने कहा--भगवन्‌! हमें तीर्थकी महिमाका
- **Translation**: 

---

### Verse 11 (Bramha 0.2871)
- **Original**: पुष्कर-इनके द्वारा आबृत तीर्थ आसुर कहलाते विस्तारपूर्वक श्रवण करनेपर भी तृप्ति नहीं होती।
- **Translation**: 

---

### Verse 12 (Bramha 0.2872)
- **Original**: हैं। प्रभास, भार्गव, अगस्ति, नर-नारायण, जसिष्ठ, आप पुनः किसी गोपनीय तीर्थका वर्णन करें।
- **Translation**: 

---

### Verse 13 (Bramha 0.2873)
- **Original**: भरद्वाज, गौतम और कश्यप--इन ऋषि-मुनियोंद्वारा ब्रह्मजी बोले-- श्रेष्ठ ब्राह्मणो ! पूर्वकालमें देवर्षि
- **Translation**: 

---

### Verse 14 (Bramha 0.2874)
- **Original**: सेवित तीर्थ ऋषितीर्थ हैं। अम्बरीष, हरिश्वचन्द्र, नारदने मुझसे यही प्रश्न पूछा था। उस समय मैंने
- **Translation**: 

---

### Verse 15 (Bramha 0.2875)
- **Original**: मान्धाता, मनु, कुर, कनखल, भद्राश्व, सगर, प्रयत्रपूर्वक जो कुछ उनसे कहा था, वही तुम्हें भी
- **Translation**: 

---

### Verse 16 (Bramha 0.2876)
- **Original**: अश्वयूप, नचिकेता, वृषाकपि तथा अरिन्दम आदि बतलाता हूँ।
- **Translation**: 

---

### Verse 17 (Bramha 0.2877)
- **Original**: मानवोद्वारा निर्मित तीर्थ मानुष कहलाते हैं। ये नारदजीने पूछा--जगत्पते ! स्वर्गलोक, मर्त्वलेक
- **Translation**: 

---

### Verse 18 (Bramha 0.2878)
- **Original**: सब॒ यश तथा उत्तम फलकी सिद्धिके लिये और रसातलमें कुल कितने तीर्थ हैं तथा सब
- **Translation**: 

---

### Verse 19 (Bramha 0.2879)
- **Original**: निर्मित हुए हैं। तीनों लोकोंमें कहीं भी जो स्वतः तीथाँमें सदा कौन सबसे बढ़कर है? प्रकट हुए दैव तीर्थ हैं, उन्हें पुण्यतीर्थ कहा गया ब्रह्मजी बोले--देवपषे ! स्वर्गलोक, मर्त्यलोक
- **Translation**: 

---

### Verse 20 (Bramha 0.2880)
- **Original**: है। इस प्रकार मैंने तीर्थ-भेद बतलाये हैं। और रसातलमें चार प्रकारके तीर्थ हैं-दैव,
- **Translation**: 

---

