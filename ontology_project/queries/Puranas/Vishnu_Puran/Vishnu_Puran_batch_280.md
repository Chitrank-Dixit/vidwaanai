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

### Verse 1 (Vishnu Puran 0.5581)
- **Original**: 9 नोशैहसेत्सशब्द जे न मुझेत्पलनं खुधः । नखान्न खाल्येच्छिस्ाान्न तृं न महीं लिखेत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5582)
- **Original**: 90 ओऔर्य बोले--गृहस्थ पुरुषको नित्यप्रति देवता, गौ, ब्राह्मण, सिद्धगण, वयोवुद्ध तथा आचार्यकी पूजा करनो चाहिये और दोनों समय सब्ध्यावन्दन तथा अमित्ोत्रादि कर्म करने चाहिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5583)
- **Original**: गृहस्थ पुरुष सदा ही संयमपूर्वक रहकर बिना कहींसे कटे हुए दो बख्नर, उत्तम ओषधियाँ और गास्ड (मरकत आदि त्रिष नष्ट करनेवाले) रत घारण करे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5584)
- **Original**: वह केशॉको स्कचछ और चिकना रखे तथा सर्वदा सुगन्धयुक्त सुन्दर वेष और मनोहर श्वेतपुष्प शारण करें
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5585)
- **Original**: किसीका थोड़ा-सा थी घन हरुण न करे और थोड़ा-सा भी अप्रिय भाषण न करें। जो मिथ्या हो ऐसा प्रिय वचन भी कभी न बोले और न कभी दूसरोंके दोषोंको ही कहे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5586)
- **Original**: हे पुरुषश्रेष्ठ ! दूसरोंकी सनी अथवा दूसरोंके साथ लैर करनेमें कभी रुचि न करे, निन्दित सवारोमें कभी 8 चढ़े और नदीतीरकी छायाका कभी आश्रय न ले
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5587)
- **Original**: बुद्धिमान्‌ पुरुष व्लेकविद्विप्ट, पतित, उन्‍्पत्त और जिसके बहुत-से झत्रु हो ऐसे परपीडक मिथ्यायादी अति व्ययशील, निन्दापरायण और दुष्ट पुरुषोंके साथ कभी मित्रता न करे और न कभी मार्गमें अकेला चले
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5588)
- **Original**: है गरेध्वर ! जलप्रवाहके वेगमें सामने पड़कर स्त्रान न करे, जल्ते हुए घरमें प्रलेद्ञा न करे और वृक्षकी चोटोपर न चढ़े
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5589)
- **Original**: दाँतॉंको परस्पर न घिसे, नाकय्त्रे न क्रेदे तथा मुखक्त्रे बन्द किये हुए जमुहाई न ले और न बन्द मुखसे खाँसे या धास छोड़े
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5590)
- **Original**: बुद्धिमान्‌ पुरुष जोरसे न हैसे और झब्द करते हुए अधोवायु न छोड़े; तथा नखोंको न चबावे, तिनका न तीड़े और पृथिवीपर भी न लिखे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5591)
- **Original**: अ* 12 ) न इमश्रु भक्षयग्रेल्ल्प्रेष्ट न मृदनीयाद्विच क्षण: । ज्योतीष्यमेध्यशस्तानि नाभिवीक्षेत च प्रभो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5592)
- **Original**: 19 नआमां परस्तियं चव सूर्य चास्तमयोदये। न हुड्डुर्याच्छव॑ गन्धं शवगन्धो हि सोमजः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5593)
- **Original**: 12 चतुष्पर्थ चैत्यतरू इमशानोपवनानि च। दुष्टख्लीसन्निकर्ष च वर्जयेन्निशि सर्वदा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5594)
- **Original**: 13 पूज्यदेवद्विजज्योतिश्छायां नातिक्रमेद बुध: । नैकइशुन्याटवीं गच्छेत्तथा शुन्यगृहे वसेत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5595)
- **Original**: 14 केशास्थिकण्टकामेध्यबलिभस्मतुषांस्तथा । स्त्रानार्धरणीं चैव दूरत: परिवर्जयेत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5596)
- **Original**: 15 नानार्यानाश्रयेत्कांश्विन्न जिह्म॑ं रोचयेद्‌ बुध: । उपसर्पेन्न वे व्यालं चिरं तिप्ठेन्न वोत्थित:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5597)
- **Original**: 16 अतीव जागरस्वप्रे तहत्स्लानासने बुध: । न सेवेत तथा शय्यां व्यायाम च नरेशर
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5598)
- **Original**: 17 देष्टिणश्थृद्विणश्वैव प्राज्ञो दूरेण वर्जयेत्‌। अबश्याय॑ च राजेन्द्र पुरोवातातपो तथा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5599)
- **Original**: 18 न स्त्रायाज्न स्वपेन्नमो न चैवोपस्पृशेद बुधः । मुक्तकेशश्व नाचामेद्देवाद्र्चां च वर्जयेत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5600)
- **Original**: 19 होमदेवार्चनाद्यासु क्रियास्वाचमने तथा। नैकवस्त्र: प्रवर्तेत द्विजवाचनिके जपे
- **Translation**: 

---

