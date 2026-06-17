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

### Verse 1 (Sama Ved 0.2221)
- **Original**: <55.हथो वृत्राण्यार्या हथो दासानि सत्पती
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2222)
- **Original**: हथो विश्वा अप द्विष:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2223)
- **Original**: भद्र पुरुषों के पालनकर्तता हे श्रेष्ठ इन्द्र और अग्निदेवों ! आप विघ्नों को दूर करें, कर्महीनों और द्वेष करने वालों का विनाश करें और समस्त शत्रुओं को नष्ट करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2224)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2225)
- **Original**: क्र के के
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2226)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2227)
- **Original**: 856.अभि सोमास आयव: पवन्ते मद्य॑ मदम्‌ । समुद्रस्याधि विष्टपे मनीषिणो मत्सरासो मदच्युत:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2228)
- **Original**: ड.ड सामवेद-संहिता - पनन्‍्दवर्द्धक, स्फूर्तिदायक सोमरस को, आनन्द प्राप्त करने तथा उत्साह बढ़ाने के लिए, याजकगण, जलपात्र पर स्थापित छले में से छानते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2229)
- **Original**: 857.तरत्समुद्रं पवमान ऊर्मिणा राजा देव ऋतं बृहत्‌ । अर्पा मित्रस्थ वरुणस्य धर्मणा प्र हिन्चान ऋत॑ बृहत्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2230)
- **Original**: ग्रेरणादायी दिव्य सोमरस शुद्ध होकर, प्रकृति में स्थित विशाल सोम (ऋु्त) के समुद्र में मित्र और व्ररुणदेवों द्वारा प्रयुक्त किये जाने के लिए स्थापित किया जाता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2231)
- **Original**: [ फित्र (सूर्प) के और वरुण (जल) के पाध्यम से ही प्राणरस (सोम का) संचार होता है।] <58.नृभियेंमाणों हर्यतो विचक्षणो राजा देव: समुद्र्य:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2232)
- **Original**: ऋि्विजों द्वारा शोधित, सबका प्रेम पात्र, विशेष ज्ञानवर्द्धक, धजा दिव्य सोम, इन्द्रदेव के निमित्त शोधित होकर जल में मिलता है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2233)
- **Original**: 859.तिस््रो वाच ईरयति प्र वह्निर्ईतस्य धीर्ति ब्रह्मणो मनीषाम्‌। गावो यन्ति गोपति पृच्छमाना: सोम॑ यन्ति मतयो बावशाना:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2234)
- **Original**: ब्राह्मण-मनीषी याजकगण तीन वाणियों (क्रक्‌, यजु, साम) का यज्ञीय रीति से उच्चारण करते हैं । सोम की कामना करने वालो बुद्धियाँ शब्द करती हुई (उन्हें पूछतो हुई), उनके पास जाने का प्रयास उसी प्रकार करती हैं, जैसे गौएँ (रैभाती हुई) गोपाल के पास जाती हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2235)
- **Original**: [जिस प्रकार गौओं का पालक गोपाल होता है, वैसे हो बुद्धियों का पोषक सोम है ।] 860.सोम॑ गावो धेनवो बावशानाः सोम॑ विप्रा मतिभिः पृच्छमाना: । सोम: सुत ऋच्यते पूयमान: सोमे अर्कास्त्रिष्टुभ: सं नवन्ते
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2236)
- **Original**: निकालने के बाद शोधित हुआ सोम पात्र में गिरता है । ज्ञानौजन अपनी बुद्धियों द्वारा त्िष्॒प्‌ छन्द के मंत्र से उसकी स्तुति करते हैं । दुधारू गौएँ ( परमार्थनिष्ठ बुद्धियाँ) सोम को इच्छा करती हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2237)
- **Original**: <69.एवा नः सोम परिधिच्यमान आ पवस्व पूयमान: स्वस्ति। इन्द्रमा विश बृहता मदेन वर्धवा वाच॑ जनया पुरंधिम्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2238)
- **Original**: है सोमदेव ! जल मिश्रित तथा शुद्ध होते हुए आप हमारे कल्याण के लिए शोधित हों , आनन्दपूर्वक इन्द्रदेव को तृप्त करें । हमारी प्रार्थना को स्वीकार करते हुए सद्‌बुद्धि प्रदान करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2239)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2240)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

