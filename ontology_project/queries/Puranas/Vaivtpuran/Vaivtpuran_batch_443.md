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

### Verse 1 (Vaivtpuran 23.1822)
- **Original**: चिन्तन करो। तुम और हम उन भगवान्‌ूकी रुद्र, शेष, ब्रह्मा आदि देवता, मनु, मुनीन्द्रगण, कलाकी कलाके अंशमात्र हैं। मनु और मुनीन्द्र सरस्वती, पार्वती, गड्ा और लक्ष्मी आदि देवियाँ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1823)
- **Original**: भी उनकी कलाके कलांश ही हैं। महादेव और भी जिनका सेवन करती हैं, उन भगवान्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1824)
- **Original**: ब्रह्माजी भी कलाविशेष हैं और महान्‌ विराट्‌- गोविन्दके चरणारविन्दका चिन्तन करना चाहिये।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1825)
- **Original**: पुरुष भी उनकी विशिष्ट कलामात्र हैं। सहस्र जो अत्यन्त गम्भीर और भयंकर दावाग्रिरूपी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1826)
- **Original**: सिरोंवाले शेषनाग सम्पूर्ण विश्वको अपने मस्तकपर सर्पसे आवेष्टित हो छटपटाते अद्भवाले संसार-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1827)
- **Original**: सरसोंके एक दानेके समान धारण करते हैं, परंतु सागरको लाँघकर उस पार जाना चाहता है और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1828)
- **Original**: कूर्मके पृष्ठभागमें वे शेषनाग ऐसे जान पड़ते हैं, श्रीहरिके दास्य-सुखको पानेकी इच्छा रखता है,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1829)
- **Original**: मानो हाथीके ऊपर मच्छर बैठा हो। वे भगवान्‌ बह भगवान्‌ श्रीकृष्णके चरणारविन्दका चिन्तन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1830)
- **Original**: कूर्म (कच्छप) श्रीकृष्णजी कलाके कलांशमात्र करे। जिन्होंने गोवर्धन पर्वतको हाथपर उठाकर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1831)
- **Original**: हैं। नारद! गोलोकनाथ भगवान्‌ श्रीकृष्णका निर्मल ब्रजभूमिको इन्द्रके कोपसे बचानेकी कीर्ति प्राप्त
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1832)
- **Original**: यश वेद और पुराणमें किह्निन्मात्र भी प्रकट नहीं कौ है, वाराहावतारके समय एकार्णवके जलमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1833)
- **Original**: हुआ। ब्रह्मा आदि देवता भी उसका वर्णन करनेमें गली जाती हुई पृथ्वीको अपनी दाढ़ोंके अग्रभागसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1834)
- **Original**: समर्थ नहीं हैं। ब्रह्मपुत्र नारद! तुम उन सर्वेश्वर उठाकर जलके ऊपर स्थापित किया तथा जो
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1835)
- **Original**: श्रीकृष्णका ही मुख्यरूपसे भजन करो। अपने रोमकृषपोंमें असंख्य विश्व-ब्रह्माण्डकों धारण जिन विश्वाधार परमेश्वरके सम्पूर्ण लोकोंमें करते हैं, उन आदिपुरुष भगवान्‌ गोविन्दके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1836)
- **Original**: सदा बहुत-से ब्रह्मा, विष्णु तथा रुद्र रहा ही चरणारविन्दका चिन्तन करना चाहिये। जो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1837)
- **Original**: करते हैं तथा श्रुतियाँ और देवता भी उनकी नियत गोपाड्नाओंके मुखारविन्दके रसिक भ्रमर हैं और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1838)
- **Original**: संख्याको नहीं जानते हैं, उन्हीं परमेश्वर श्रीकृष्णकी वृन्दावनमें विहार करनेवाले हैं, उन द्रजवेषधारी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1839)
- **Original**: तुम आराधना करो। वे विधाताके भी विधाता विष्णुरूप परमपुरुष रसिक-रमण रासेश्वर श्रीकृष्णके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1840)
- **Original**: हैं। वे ही जगत्प्रसविनी नित्यरूपिणी प्रकृतिको चरणारविन्दका चिन्तन करना चाहिये। वत्स
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1841)
- **Original**: प्रकट करके संसारकी सृष्टि करते हैं। ब्रह्मा आदि नारदमुने! जिनके नेत्रोंकी पलक गिरते ही
- **Translation**: 

---

