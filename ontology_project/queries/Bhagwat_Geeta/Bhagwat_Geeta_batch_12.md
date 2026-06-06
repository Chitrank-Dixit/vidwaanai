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

### Verse 1 (Bhagwat_Geeta 2.221)
- **Original**: स्वधर्ममपि चावेक्ष्य न विकम्पितुमरहसि। धर्म्याद्धि युद्धाच्छेयोन्यत्क्षत्रियस्थ न विद्यते
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 2.222)
- **Original**: तथा अपने धर्मको देखकर भी तू भय करनेयोग्य नहीं है अर्थात्‌ तुझे भय नहीं करना चाहिये; क्योंकि क्षत्रियके लिये धर्मयुक्त युद्धसे बढ़कर दूसरा कोई कल्याणकारी कर्तव्य नहीं है
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 2.223)
- **Original**: यदृच्छया चोपपन्न॑ स्वर्गद्वारमपावृतम्‌ । सुखिन: क्षत्रिया: पार्थ लभन्ते युद्धमीदृशम्‌
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 2.224)
- **Original**: । हे पार्थ! अपने-आप प्राप्त हुए और खुले हुए + जिसका वध नहीं किया जा सके।
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 2.225)
- **Original**: * अध्याय 2* 37 स्वर्गके द्वाररूप इस प्रकारके युद्धको भाग्यवान्‌ क्षत्रियलोग ही पाते हैं
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 2.226)
- **Original**: अथ चेत्त्वमिमं धर्म्य सड़्ग्प्रामं न करिष्यसि। ततः स्वधर्म कीर्ति चर हित्वा पापमवाप्स्यसि
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 2.227)
- **Original**: किन्तु यदि तू इस धर्मयुक्त युद्धको नहीं करेगा तो स्वधर्म और कीर्तिको खोकर पापको प्राप्त होगा
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 2.228)
- **Original**: अकीर्ति चापि भूतानि कथयिष्यन्ति तेडव्ययाम्‌। सम्भावितस्य चाकीर्ति- मरणादतिरिच्यते
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 2.229)
- **Original**: तथा सब लोग तेरी बहुत कालतक रहनेवाली अपकीर्तिका भी कथन करेंगे और माननीय पुरुषके लिये अपकीर्ति मरणसे भी बढ़कर है
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 2.230)
- **Original**: भयाद्रणादुपरतं मंस्यन्ते त्वां महारथाः। येषां च त्वं बहुमतो भूत्वा यास्यसि लाघवम्‌
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 2.231)
- **Original**: और जिनकी दृष्टिमें तू पहले बहुत सम्मानित होकर अब लषघुताको प्राप्त होगा, वे महारथीलोग तुझे भयके कारण युद्धसे हटा हुआ मानेंगे
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 2.232)
- **Original**: अवाच्यवादांश्व बहून्वदिष्यन्ति तवाहिता: । निन्दन्तस्तव सामर्थ्य ततो दुःखतरं नु किम्‌
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 2.240)
- **Original**: * अध्याय 2* 37 बन्धनको भलीभाँति त्याग देगा अर्थात्‌ सर्वथा नष्ट कर डालेगा
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 2.241)
- **Original**: नेहाभिक्रमनाशो5स्ति प्रत्यवायो न विद्यते। स्वल्पमप्यस्य धर्मस्य त्रायते महतो भयात्‌
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 2.242)
- **Original**: इस कर्मयोगमें आरम्भका अर्थात्‌ बीजका नाश नहीं है और उलटा फलरूप दोष भी नहीं है, बल्कि इस कर्मयोगरूप धर्मका थोड़ा-सा भी साधन जन्म- मृत्युरूप महान्‌ भयसे रक्षा कर लेता है
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 2.243)
- **Original**: व्यवसायात्मिका बुब्द्विकेह कुरुनन्दन। बहुशाखा हानन्ताश्च बुद्धयो5व्यवसायिनाम्‌
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 2.244)
- **Original**: हे अर्जुन! इस कर्मयोगमें निश्चयात्मिका बुद्धि एक ही होती है; किन्तु अस्थिर विचारवाले विवेकहीन सकाम मनुष्योंकी बुद्धियाँ निश्चय ही बहुत भेदोंवाली और अनन्त होती हैं
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 2.245)
- **Original**: यामिमां पुष्पितां वाचं प्रवदन्त्यविपश्चित: । वेदवादरताः पार्थ नान्यदस्तीति वादिनः
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 2.246)
- **Original**: कामात्मानः स्वर्गपरा जन्मकर्मफलप्रदाम्‌। क्रियाविशेषबहुलां भोगैश्वर्यगतिं प्रति
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 2.247)
- **Original**: भोगैश्वर्यप्रसक्तानां._ तयापहतचेतसाम्‌। व्यवसायात्मिका बुदर्द्विः समाधौ न विधीयते
- **Translation**: 

---

