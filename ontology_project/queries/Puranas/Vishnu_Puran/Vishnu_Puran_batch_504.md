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

### Verse 1 (Vishnu Puran 0.10061)
- **Original**: जिनक्य्र सौ बज्ञोंसे यजन करके इन्द्रने देखयाज-पदवी प्राप्त की है, आज में उन्हीं अनादि और अनन्त केशबका दर्शन करूँगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10062)
- **Original**: जिनके स्वरूपको ब्रह्मा, इन्द्र, रुद्र, अश्विनीकुमार, बसुगण, आदित्य और परद्ण आदि कोई भी नहीं जानते आज वे ही हरि मेरे नेत्रोंके विषय होंगे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10063)
- **Original**: जो। सर्बात्या, सर्वज्ञ, सर्वस्वरूप और सब भूतोंमें अवस्थित हैं तथा जो अच्िन्य, अव्यय और सर्वव्यापक हैं, अहो ! आज ख्वयं वे ही मेरे साथ बातें करेंगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10064)
- **Original**: जिग अजन्माने मत्स्य, कूर्म, वराह, हंयग्रीव और नृसिंह आदि रूप घारणकर जगतकी रक्षा की है, आज वे ही मुझसे जार्तालाप करेंगे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10065)
- **Original**: । 'इस्र समय उन अव्ययात्मा जगत्मभुने अपने मनमें सोचा हुआ कार्य करनेके लिये अपनी ही इच्छासे मनुष्य- कर्तु मनुष्यतां प्राप्तस्स्वेच्छादेहधृगव्यबः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10066)
- **Original**: 11 । देह धारण किया है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10067)
- **Original**: जो अनत्त (दोषजी) अपने योअनन्तः पृथिवीं घत्ते शेखरस्थितिसंस्थिताम्‌।
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10068)
- **Original**: मस्तकपर रस्त्री हुई पृथिवीकों धारण करते हैं, संसारके सोउबतीर्णो जगत्यर्थे मामक्रूरेति त्रक्ष्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10069)
- **Original**: कहकर णोलेंगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10070)
- **Original**: केपड श्रीविष्णुपुराण [ अ* 17 “जिनकी इस पिता, पुत्र, सुद्ददू, भ्राता, माता और पितृपुत्रसुहृद्भातृमातृब-शुमयीमिमाम्‌ बन्यायां नालमुत्ततुँ जगत्तस्मै नमो नमः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10071)
- **Original**: बन्धुरूपिणी मायाको पार करनेमें संसार सर्वथा असमर्थ है तरत्यविद्यां बिततां हृदि यस्मिन्निवेशिते । बोगमायाममेयाय तस्मै विद्यात्मने नमः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10072)
- **Original**: 14 यज्वभिर्यज्ञपुरुषो वासुदेवश्च॒सात्वतै: । वेदात्तवेदिभिर्िष्णु: प्रोच्चते यो नतोउस्मि तम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10073)
- **Original**: 15 यथा यत्र जगद्धाप्नि धातर्येतत्पतिष्ठितम्‌ । सदसत्तेन सत्येन मय्यसौ यातु सौम्बताम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10074)
- **Original**: 16 स्मृते सकलकल्याणभाजनं यत्र जायते। पुरुषस्तमर्ज नित्य॑ं ब्रज्ञामि शरणं हरिम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10075)
- **Original**: 17 अ्रीपराशर उवाच इत्थ सश्लित्तयन्तिष्णुं भक्तिनग्रात्ममानस: । अक़ूरो गोकुल॑ प्राप्त: किख्नित्सूर्ये विराजति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10076)
- **Original**: 18 स॒ दरदर्श तदा कृष्णमादाबादोहने गवाम्‌। खत्समध्यगत फुल्लनीलोत्पलदलच्छविम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10077)
- **Original**: 19 प्रफुल्लपद्ापत्राक्ष. श्रीवत्साद्ितवक्षसम्‌ । प्रलम्बजाहुमायामतुझेर:स्थलूमुज़सम्‌_
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10078)
- **Original**: 20 सबिलासस्मिताधारं बिश्रां मुखपज्भूजम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10079)
- **Original**: तुडरक्तनर्ख पदभ्यां धरण्यां सुप्रतिष्ठितम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10080)
- **Original**: 29 बिश्राणं वाससी पीते ब्न्यपुष्पविभूषितम्‌। सेन्चुनीलाचलाभं त॑ सिताम्भोजावतंसकम्‌
- **Translation**: 

---

