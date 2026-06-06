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

### Verse 1 (Vaivtpuran 543.16074)
- **Original**: कमलोंकी मनोहर पंक्ति आदि सभी वैभव विद्यमान बिहार हो सकेगा? और कया श्रोनन्दनन्दनके हैं (यह सब है); परंतु मेरे प्राणनाथ कहाँ हैं? शरीरमें पुनः: चन्दन लगा पाऊँगी? हा कृष्ण! हा रमानाथ! हा मेरे प्राणवल्लभ! तुम उद्धव बोले--सुमुखि! मैं क्षत्रिय हूँ। मेरा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16075)
- **Original**: कहाँ हो? मुझ दासीसे कौन-सा अपराध हो गया नाम उद्धव है। तुम्हारा शुभ समाचार जाननेके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16076)
- **Original**: है? हुआ ही होगा; क्योंकि यह दासी तो पग- लिये परमात्मा श्रीकृष्णने मुझे भेजा है; इसीलिये
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16077)
- **Original**: पगपर अपराध करनेवाली है। मैं तुम्हारे पास आया हूँ। मैं श्रीहरिका पार्षष
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16078)
- **Original**: इतना कहकर राधिका देवी पुनः मूच्छित भी हूँ। इस समय श्रीकृष्ण, बलदेव और नन्दजी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16079)
- **Original**: हो गयीं। तब उद्धवने पुनः उन्हें चैतन्य कराया। कुशलसे हैं। उनकी उस दशाको देखकर क्षत्रियश्रेष्ठ उद्धबको श्रीराधिकाने कहा--उद्धव ! इस समय भी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16080)
- **Original**: परम आश्चर्य हुआ। उस समय सात सखियाँ अग्रौ दाहस्वरूपाय भद्रायू॑च नमो. नमः । शोभाय पूर्णचन्द्रे च शरत्पद्चे नमो तमः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16081)
- **Original**: नास्ति भेदों यथा देवि दुग्धधावल्ययो: सदा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16082)
- **Original**: यथैव गन्धभूम्योध यधथैव जलशैत्ययो:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16083)
- **Original**: यथैव शब्दनभसोज्योंति:सूर्यकयोर्यथा । लोके वेदे पुराणे च राधामाधवयोस्तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16084)
- **Original**: चेतन॑ कुरु कल्याणि देहि मामुत्तर सति । इत्युक्त्वा चोद्धवस्तत्र प्रणनाम पुनः: पुनः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16085)
- **Original**: इत्युद्यकृत॑ स्तोग्नं यथः पठेद भक्तिपूर्वकम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16086)
- **Original**: इह लोके सुख भुकत्वा यात्यन्ते हरिमन्दिरम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16087)
- **Original**: न भवेद्‌ बन्धुविच्छेदोी रोग: शोक: सुदारुण: । प्रोषिता स्त्रो लभेत्‌ कान्त॑ं भार्याभेदी लभेतू प्रियाम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16088)
- **Original**: अपुत्रो लभते पुत्नान निर्धो लभते धनम्‌ । निर्भूमिर्लभले भूमि प्रजाहीनो लभेत्‌ प्रजाम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16089)
- **Original**: रोगाद पिमुच्यते रोगी बद्धां सुच्येत बन्धनात्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16090)
- **Original**: भयान्मुच्येत भौतस्तु मुच्येतापन्न आपदः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16091)
- **Original**: अस्पष्टकीर्ति: सुयशा मूर्खो भवति पण्डित:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16092)
- **Original**: 63-93)
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16093)
- **Original**: 702 * संक्षिम ब्रह्मवैवर्तपुराण + 42888 #& 99869 ### 5 85865 9 # 6 9 66 $ 5 95 65% $ $5 # 5 # 55 558 5## #ऋ 5 55 4 ऋ 4 5 ऋहछ 85 5 5 ध ऊ# 5 5 858 88 लगातार श्रीराधापर श्वेत चँबर डुला रही थीं और
- **Translation**: 

---

