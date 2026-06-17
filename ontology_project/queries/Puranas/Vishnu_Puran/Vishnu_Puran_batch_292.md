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

### Verse 1 (Vishnu Puran 0.5821)
- **Original**: 210 अविष्णुपुराण [ अ* 15 प्रथमेषहि बुधइशस्ताउ्छोजियादीज्िमन्त्रयेत्‌ । कथवेश्व॒ तथैतैधां नियोगान्पितृुदैविकान्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5822)
- **Original**: 9 ततः क्रोधव्यवायादीनायासं तैर्िजैस्सह। यजमानो न कुर्बीत दोषस्तत्र महानवयम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5823)
- **Original**: 190 अब कप गत गज कयाक सर वा भोजयित्वा चच। व्यवायी का ज मज्जयत्यात्मनः पत्र
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5824)
- **Original**: 19 तस्मात्मथममन्रोक्ते द्विजाग्रयाणां निमनत्रणम्‌। अनिमनन्‍्रय. द्विजानेबमागतान्भोजयेदतीन
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5825)
- **Original**: 12 पादशौचादिना गेहमागतान्पूजयेद्‌ ्विजान्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5826)
- **Original**: 13 पविन्नपाणिराचान्तानासनेषृप्वेशयेत्‌ू. । पितृणामयुओो युग्मान्देवानामिच्छया ट्विजान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5827)
- **Original**: 14 देवानामेकमेकं वा पितृ्णां च नियोजयेत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5828)
- **Original**: 15 तथा मातामहश्राद्ध॑ वैश्वदेवसमन्वितम्‌ । कुर्वीत भक्तिसम्पन्नस्तन््नें वा वैश्वदैविकम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5829)
- **Original**: 16 प्राइमुखान्भोजयेद्विप्रान्देवानामुभयात्मकान्‌ । पितृमातामहानां च भोजयेचाप्युदडमुखान्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5830)
- **Original**: 97 पृथक्तयो: केचिदाहु: श्राद्धस्य करणं नृप । एकत्रैेकेन पाकेन वल्यन्ये महर्षय:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5831)
- **Original**: 18 विष्टरार्थ कुशं दत््वा सम्पूज्याध्ये विधानत: । कुर्यादावाहन प्राज्ञो देवानां तदनुज्या
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5832)
- **Original**: 19 यवाम्यबुना ञ्ञ देवानां स्ययादध्य त्रधानवित्‌। उ्रगगन्धथूपदीपांश्न तेभ्यो द्याद्यथाविधि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5833)
- **Original**: 20 पितृणामपसव्य॑ तत्सर्वभेवोपकल्पयेत्‌ । अनुज्ञां च्रतत: प्राप्य दत्त्वा दर्भान्द्रिधाकृतान्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5834)
- **Original**: 21 मन्त्रपूर्व पितृणां तु कुर्याधावाहन बुध:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5835)
- **Original**: तिलाम्बुना चापसत्य दद्यादर्ध्यादिक नृप
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5836)
- **Original**: 22 काले तत्रातिथिं प्राप्तमन्नकार्म नृपाध्वगम्‌। ब्राह्मणैरभ्यनुज्ञात: कार्म तमपि भोजयेत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5837)
- **Original**: 23 + ग्रज्ञोपयलोतकों दायें क-धेपर काके
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5838)
- **Original**: श्राझुके पहले दिन बुद्धिमान्‌ पुरुष श्रोत्रिथ आदि बिहित ब्राह्मणोंको निमन्लित को और उनसे यह कह दे कि 'आपको पितृ श्राद्धमें और आपको विश्वेदेव-श्राद्धमें नियुक्त होता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5839)
- **Original**: उन निमन्त्रित ब्राह्मणोके सहित श्राद्ध करनेवाल्थ पुरुष उस दिन क्रोधादि तथा स््रीगमन और परिश्रम आदि न करे, क्योंकि बद्ध करनेमें यह महान्‌ दोष माना गया है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5840)
- **Original**: श्राद्धमें निमश्च्नित होकर या भोजन करके अथजा निमनन्‍त्रण करके या भोजन कराकर जो पुरुष स्त्री-प्रसंग करता है व अपने पित॒गणको मानों यीर्यके कुण्डमें डुबोता है
- **Translation**: 

---

