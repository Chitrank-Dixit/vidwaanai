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

### Verse 1 (Rig Ved 0.1841)
- **Original**: 844. त्वोतो वाज्यहुयो$भि पूर्वस्मादपर:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.1842)
- **Original**: प्र दाश्वाँ अग्ने अस्थात्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.1843)
- **Original**: है अग्निदेव ! पहले असुरक्षित रहने वाला हविदाता यज़मान आपकी साउपर्थ्य द्वारा रक्षित होकर बल सम्पन्न बना तथा होनता से मुक्त हुआ
- **Translation**: 

---

### Verse 4 (Rig Ved 0.1844)
- **Original**: 845. उत झुमत्सुवोय॑ बृहदग्ने विवाससि। देवेभ्यो देव दाशुधे
- **Translation**: 

---

### Verse 5 (Rig Ved 0.1845)
- **Original**: है महान्‌ अग्निदिव ! आप देवों को हवि प्रदान करते वाले यजमान को अतिशय तेज और श्रेष्ठ बल प्राप्त कराते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.1846)
- **Original**: सिक्त - 75
- **Translation**: 

---

### Verse 7 (Rig Ved 0.1847)
- **Original**: ] [ऋषि - गोतम राहूगण । देवता - अग्नि । छन्‍्द -गायत्री । ] 846. जुषस्व सप्रथस्तमं वचो देवप्सरस्तमम्‌। हव्या जुद्दान आसनि
- **Translation**: 

---

### Verse 8 (Rig Ved 0.1848)
- **Original**: हे अग्निदेव ! म्रुख में हकियों को ग्रहण करते हुए हमारे द्वारा देवों को अत्यन्त प्रसन्‍न करने वाले स्तुति बचनों को आप स्वीकार करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.1849)
- **Original**: 847. अथा ते अड्विरस्तमाग्ने वेधस्तम प्रियम्‌। वोचेम ब्रह्म सानसि
- **Translation**: 

---

### Verse 10 (Rig Ved 0.1850)
- **Original**: ” अंगिरा(आंगों में स्थापित देवों ) में श्रेष्ठ मेधावियों में उत्कृष्ट हे अग्तिदेव ! अब हम आपके निमित्त अति प्रिय मंत्र युक्त स्तोत्रों का पाठ करते हैं
- **Translation**: 

---

### Verse 11 (Rig Ved 0.1851)
- **Original**: 848. कस्ते जामिर्जनानामग्ने को दाश्वध्वर:। को ह कस्मिन्नसि श्रित:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.1852)
- **Original**: है अग्निदेव ! में आपका बन्धु कौन है ? श्रेष्ठ दान से.कौन आपका यजन करता है ? आपके स्वरूप को कौन जानता कह ब आपका आश्रय स्थल कहाँ है ?
- **Translation**: 

---

### Verse 13 (Rig Ved 0.1853)
- **Original**: 849. त्व॑ जार्मिर्जनानामग्ने मित्रो असि प्रिय:। सखा सखिभ्य ईड्य:
- **Translation**: 

---

### Verse 14 (Rig Ved 0.1854)
- **Original**: हे अम्निदिव ! आप मनुष्यों से भातृभाव रखने वाले, यजमानों की रक्षा करने वाले, स्तोताओं के लिए प्रिय मित्र के तुल्य हैं
- **Translation**: 

---

### Verse 15 (Rig Ved 0.1855)
- **Original**: में0 9 सृ0 76 श्07 850. यजा नो मित्रावरुणा यजा देवाँ ऋतं बृहत्‌। अग्ने यक्षि स्व॑ं दमम्‌
- **Translation**: 

---

### Verse 16 (Rig Ved 0.1856)
- **Original**: है अग्निदेव ! हमारे निर्ित्त मित्र और वरुण का यजन करें । विशाल यज्ञ सम्यादित करें तथा यत्ञशाला में पूजा योग्य भाव से रहें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.1857)
- **Original**: सिक्त - 76 ] [ऋषि - गोतम राहुगण । देवता - अग्नि । छन्द - त्रिए्प । ] 851. का त उपेतिर्मनसों बराय भुबदग्ने शंतमा का मनीषा । को वा यज्ै: परि दक्ष त आप केन वा ते मनसा दाशेम
- **Translation**: 

---

### Verse 18 (Rig Ved 0.1858)
- **Original**: है अग्निदिव ! आपके मन को सन्तुष्ट करने का हम क्या उपाय करें ? किस यज्ञ से यजमान बल बृद्धि करें ? कौन सी स्तुति आपके लिए सुखप्रद है ? किस मन से हम आपको हवि श्रदान करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.1859)
- **Original**: 852. एह्नाग्न इह होता नि षीदादब्ध: सु पुरएता भवा नः । अवतां त्या रोदसी विश्वमिन्वे यजा महे सौमनसाय देवान्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.1860)
- **Original**: है अभ्निदेव ! आप हमारे इस यज्ञ में आकर होता रूप में अधिष्ठित हों । आप अधिचलित होकर इसमें अप्रणो हों । सर्वव्यापक आकाश और पृथ्वी आपकी रक्षा करें । हमारे लिए अभीष्ट फल- प्राप्ति के निघित्त आप देवकार्य (यज्ञ) सम्पन्न करायें
- **Translation**: 

---

