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

### Verse 1 (Vishnu Puran 0.1041)
- **Original**: 1291 का ल्वन्या ल्वामृते देवि सर्वयज्ञमयं वपु: । अध्यास्ते देवदेवस्थ योगिचिन्त्यं गदाभृतः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1042)
- **Original**: 122 त्वया देवि परित्यक्त सकल भुवनत्रयम्‌। विनष्टप्रायमभवत्तवयेदानीं. समेधितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1043)
- **Original**: 123 दाराः पुन्नास्तथागारसुहद्धान्यधनादिकम्‌ । भ्रवत्येतन्प्हाभागे नित्य त्वद्गीक्षणात्रणाम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1044)
- **Original**: 124 शरीरारोग्यमैश्वर्यमरिपक्षक्षय: सुखम्‌ । देवि त्वददृष्टिदृष्टानां पुरुषाणां न दुर्लभम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1045)
- **Original**: 125 ते माता सर्वस्लेकानां देवदेवो हरि: पिता । त्वयैतद्विष्णुना चाम्ब जगदव्याप्तै चराचरप्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1046)
- **Original**: 126 मा नः कोहं तथा गो मा गृह मा परिच्छदम्‌ । मरा झरीर॑ कलत्ं च त्यजेथाः सर्वपातलनि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1047)
- **Original**: 127 मा पुत्रात्मा सुहद्वर्ग मा पशुत्मा विभूषणम्‌ । त्यजेथा मम देवस्य विष्णोर्वक्ष: स्थछालये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1048)
- **Original**: 128 स्तन सत्यक्षोत्राभ्यां तथा झील्त्रदिभिर्गुण: । त्यज्यन्ते ते नरा: सह्य: सन्त्यक्ता ये त्ववामले
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1049)
- **Original**: 129 त्क्या विलोकिता: सच्चः शीलाहरखिलैगुणै: । कुलेश्वर्यैश्व युज्यत्ते पुरुषा निर्गुणा अपि
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1050)
- **Original**: 130 स इल्ाध्य: स गुणी धन्य: स कुलीन: स बुद्धिमान्‌ । स शूरः स च विक्रात्तो यस्त्वया देवि वीक्षित:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1051)
- **Original**: 131 सद्यो बैगुण्यमायान्ति शीलाद्या: सकला गुणा: । पराइ्मुखी जगद्धात्री यस्य त्वं विष्णुवल्लभ्े
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1052)
- **Original**: । 132 नते वर्णयितुं शक्ता गुणाझिह्वापि वेधस: । प्रसीद देवि पद्माक्षि मास्मांस्याक्षी: कदाचन
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1053)
- **Original**: 133 अ्रीफाजर उवाच एवं श्री: संस्तुता सम्यक्‌ प्राह्न देवी शतक्रतुम । शृण्वतां सर्वदेवानां सर्वभूतस्थिता द्विज
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1054)
- **Original**: 134 हे शोभने ! यज्ञ-विद्या (कर्म-काण्ट), महाविद्या (उपासना) और गुद्ाविद्या (इन्द्रजाल) तुम्हों हो तथा हे देनि ! तुम्हीं मुक्ति फल-दाबिनी आत्मनिद्या हो
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1055)
- **Original**: है देघि! आन्वीक्षिकों (तर्कक्द्या), वेदत्रयो, चार्ता (हिल्पवाणिज्यादि) और दण्डनीति (राजनीति) भी तुम्हीं हो। तुम्हींति अपने जात्त और उग्र रूपॉसे यह समस्त संसार व्याप्त किया हुआ है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1056)
- **Original**: हे देघि । तुम्हारे बिना और ऐसी कौन स्त्री है जो देवदेव भगवान्‌ गदाधरके योगिजन- चित्तित सर्वयज्ञमय शरीरक्य्र आश्रय पा सके
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1057)
- **Original**: है देचि ! तुम्हारे छोड़ देनेपर सम्पूर्ण त्रिल्लेकी नष्टप्राय हो गयी थी; अब तुम्हीने उसे पुनः जीवन-दान दिया है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1058)
- **Original**: हे सहाभागे ! रबी, पुत्र, गृह, धन, धान्य तथा सुद्दद्‌ ये सब सदा आपहीके दृष्टिपातसे मनुष्योंको मिलते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1059)
- **Original**: हे देथि ! तुष्हारी कृपा दृष्टिके पात्र पुरुषोके लिये शारीरिक आशेग्य, ऐश्वर्य, शत्रु-पक्षका नाश ओर सुख आदि कुछ भी दुर्कभ नहीं हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1060)
- **Original**: तुम सम्पूर्ण लोकॉकी माता हो और देवदेव भगवान्‌ हरि पिता हैं। हे मातः ! तुमसे और श्रोविष्णुभगवानसे यह सकल चराचर जगत्‌ व्याप्त है
- **Translation**: 

---

