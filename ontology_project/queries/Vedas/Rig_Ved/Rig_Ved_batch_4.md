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

### Verse 1 (Rig Ved 0.61)
- **Original**: हे विश्वेदेवो ! आप सबको रक्षा करने वाले, सभी प्राणियों के आधारभूत और सभी को ऐश्वर्य प्रदान करने वाले हैं। अत: आप इस सोम युक्त हवि देने वाले यजमान के यज्ञ में पधारें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.62)
- **Original**: 26. विश्वे देवासो अप्तुरः सुतमा गन्त तूर्णय:। उस्ना डृव स्वसराणि
- **Translation**: 

---

### Verse 3 (Rig Ved 0.63)
- **Original**: सम्रय-सम्य पर वर्षा करने वाले हे विश्वेदेवो ! आप कर्म - कुशल और द्रुतगति से कार्य करने वाले हैं! आप सूर्य-रश्मियों के सदूश गतिशील होकर हमें प्राप्त हों
- **Translation**: 

---

### Verse 4 (Rig Ved 0.64)
- **Original**: 27. विश्वे देवासो अस्लिध एहिमायासो अद्गुह:। मेध॑ जुषन्त वहय:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.65)
- **Original**: हे विश्वेदेबो ! आप किसी के द्वारा बध न किये जाने वाले, कर्म-कुशल, द्रोहरहित और सुखप्रद हैं। आप हमारे यज्ञ में उपस्थित होकर हि का सेवन करें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.66)
- **Original**: 28. पावका नः सरस्वती वाजेभि्वाजिनीवती
- **Translation**: 

---

### Verse 7 (Rig Ved 0.67)
- **Original**: यज्ञं वष्ट धियावसु:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.68)
- **Original**: पवित्र बनाने वाली, पोषण देने वाली, बुद्धिमत्तापूर्वक ऐश्वर्य प्रदान करने बाली देवी सरस्वती ज्ञान और कर्म से हमारे यज्ञ को सफल बनायें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.69)
- **Original**: 29. चोदयियत्री सूनृतानां चेतन्ती सुमतीनाम्‌। यज्ञ दधे सरस्वती
- **Translation**: 

---

### Verse 10 (Rig Ved 0.70)
- **Original**: सत्यप्रिय (वचन) बोलने की प्रेरणा देने वाली, मेधावी जनों को यज्ञानुष्ठान की प्रेरणा (मति) प्रदान करने वाली देवी सरस्वती हमारे इस यज्ञ को स्वीकार करके हमें अभीष्ट वैभव प्रदान करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.71)
- **Original**: 30. महो अर्ण: सरस्वती प्र चेतयति केतुना। धियो विश्वों वि राजति
- **Translation**: 

---

### Verse 12 (Rig Ved 0.72)
- **Original**: जो देवी सरस्वती नदी-रूप में प्रभूत जल को प्रवाहित करती हैं । वे सुमति को जगाने वाली देवी सरस्वती सभी याजकों की प्रज्ञा को प्रखर बनाती हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.73)
- **Original**: [ सूक्त - 4 [ऋषि-मधुच्छन्दा वैश्वापित्र । देवता-इन्द्र । छन्द-गायत्री
- **Translation**: 

---

### Verse 14 (Rig Ved 0.74)
- **Original**: ] 31. सुरूपकूलुमूतये सुदुघामिव गोदुहे । जुहूमसि द्यविद्यवि
- **Translation**: 

---

### Verse 15 (Rig Ved 0.75)
- **Original**: (गो दोहन करने वाले के द्वारा) प्रतिदिन मधुर दूध प्रदान करने वाली गाय को जिस प्रकार बुलाया जाता है, उसी प्रकार हम अपने संरक्षण के लिये सौन्दर्यपूर्ण यज्ञकर्म सम्पनन करने वाले इन्द्रदेव का आवाहन करते हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.76)
- **Original**: 32. उप न: सबना गहि सोमस्य सोमपा: पिब
- **Translation**: 

---

### Verse 17 (Rig Ved 0.77)
- **Original**: गोदा इद्रेवतों मद:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.78)
- **Original**: सोमरस का पान करने वाले हे इद्धदेव ! आप सोम ग्रहण करने हेतु हमारे सवन-यज्ञों में पधार कर, सोमरस पौने के बाद प्रसन्‍न होकर याजकों को यश, वैभव और गौएँ प्रदान करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.79)
- **Original**: 33. अथा ते अन्तमानां विद्याप सुपतीनाम्‌। मा नो अति ख्य आ गहि
- **Translation**: 

---

### Verse 20 (Rig Ved 0.80)
- **Original**: सोमपान कर लेने के अनन्तर हे इन्द्रदेव ! हम आपके अत्यन्त समापकत्तों श्रेष्ठ प्रज्ञायान्‌ पुरुषों की उपस्थिति में रहकर आपके विषय में अधिक ज्ञान प्राप्त करें । आप भो हमारे अतिरिक्त अन्य किसो के समक्ष अपना स्वरूप प्रकट न करें (अर्थात्‌ अपने विषय में न बताएँ)
- **Translation**: 

---

