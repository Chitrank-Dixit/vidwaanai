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

### Verse 1 (Vishnu Puran 0.1241)
- **Original**: अफड्लिरा बोले--यदि तू अग्रयस्थानका इच्छुक है तो जिन अव्ययात्मा अच्युतमें यह सम्पूर्ण जगत्‌ ओतप्रोत है उन गोचिच्दकों हो आराधना कर
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1242)
- **Original**: पुलस्त्य बोले--जो परबह्य परमधाम और परस्वरूप हैं उन हस्की आराधना करनेसे मनुष्य अति दुर्कभ मोक्षपदक्त्रे भो प्राप्त कर लेता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1243)
- **Original**: 4 2 0$& 90 अविध्णुपराण [आअ- 19 श्रीविष्णुपुराण ( अ« 11 पूल उवाच ऐज्रमिन्द्र: पर॑ स्थानं यमाराध्य जगत्पतिम्‌ । प्राप यज्ञपतिं विष्णुं तमाराधय सुब्रत
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1244)
- **Original**: 47 अऋतुस्काब यो यज्ञपुरुषो यज्ञों योगेश: परम: पुमान्‌। तस्मिस्तुष्टे यदप्राप्य॑ कि तदस्ति जनार्दने
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1245)
- **Original**: 48 वस्तिष्न उवाच श्राप्नोष्याराधिते विष्णो मनसा यद्यदिव्छसि । अलोक्यात्तर्गत॑ स्थान किमु वत्सोत्तमोत्तमम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1246)
- **Original**: 49 ध्रुव उवाच आराध्य: कथितो देवो भवद्धि: प्रणतस्य मे । मया तत्परितोषाय यज्प्तव्यं तदुच्यताम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1247)
- **Original**: 50 यथा चाराधन॑ तस्य मया कार्य महात्मनः । प्रसादसुमुखास्तन्‍्मे कथयन्तु महर्षयः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1248)
- **Original**: 51 ऋषय ऊचुः राजपुत्र यथा. विष्णोराराधनपरैनरे: । कार्यमाराधन॑ तन्नो यथावच्छोतुमहसि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1249)
- **Original**: 52 बाह्यार्थादखिलाशित्त त्याजयेत्रथमं नरः । तस्मिन्नेव जगद्धाप्नि ततः कुर्बीत निश्चकलम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1250)
- **Original**: 53 एबमेकाग्रचित्तेन तन्मयेन धृतात्मना । जप्तव्य॑ यश्नियोथैतत्तन्न: पार्थिवनन्दन:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1251)
- **Original**: 54 हिरण्यगर्भपुरुषप्रधानाव्यक्तरूपिणे । 3» नमो वासुदेवाय शुद्धज्ञानस्वरूपिणे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1252)
- **Original**: 55 एतज्जजाप भगवान्‌ जप्य॑ स्वायम्मुवो मनुः । पितामहस्तव॒ पुरा तस्थ तुष्टो जनार्दनः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1253)
- **Original**: 56 ददौ यथाभिलपितां सिद्धि त्रैलोक्यदुर्लभाम्‌। तथा त्वमपि गोविन्द तोषयैतत्सदा जपन्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1254)
- **Original**: 57 पुलह बोल्े--हे सुबत ! जिन जगत्पतिकी आराधनासे इन्द्रने अत्युत्तम इद्धपद ग्राप्त किया है तू ठन यज्ञर्पति भगवान्‌ विष्णुकी आराधना कर
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1255)
- **Original**: क्रतु ओले--जो परमपुरुष यज्ञपुरुष, यज्ञ और योगेश्वर हैं उन जनार्दनके सन्तुष्ट होनेपर कौन-सी वस्तु दुर्लभ रह सकती है ?
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1256)
- **Original**: ससिष्ठ खोले--हें कत्स! विष्णुभगवानकी आराधना करनेपर तू अपने मनसे जो कुछ चाहेगा बही प्राप्त कर लेगा, फिर त्रिलेकोके उत्तमोत्तम स्थाक्कों तो बात ही क्या है ?
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1257)
- **Original**: ध्रुबने कहा--हे महर्षिगण ! मुझ विनीतकों आपने आराध्यदेव तो बता दिया। अब उसको प्रसन्न करनेके लिये मुझे क्या जपना चाहिये---यह बताइये । उस महापुरुषव्र मुझे जिस प्रकार आयाधना करनी चाहिये, वह आपलोग मुझसे प्रसन्नतापूर्वक कहिये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1258)
- **Original**: ऋषिगण बोले--हे राजकुमार ! बिष्णु- भगवान्‌की आशशधरनामें तत्पर पुरुषोंकों जिस प्रकार उनकी उपासना करनी चाहिये वह तू हमसे यथावत्‌ श्रवण कर
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1259)
- **Original**: मनुष्यकों चाहिये कि पहले सम्पूर्ण बाह्य विषयोंसे चित्तको हटाबे और उसे एकमात्र उन जगदाधघारमें हो स्थिर कर दे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1260)
- **Original**: हे राजकुमार ! इस प्रकार एकाग्रचित होकर तन्मय-भावसे जो कुछ जपना चाहिये, वह सुन--
- **Translation**: 

---

