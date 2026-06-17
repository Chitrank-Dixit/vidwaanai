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

### Verse 1 (Vaivtpuran 32.7717)
- **Original**: संहार करता है और काल ही पालन करता है। हैं, वे निरन्तर अपने अंदर वर्तमान हैं; परंतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.7718)
- **Original**: काल भगवान्‌ जनार्दनका स्वरूप है; परंतु श्रीकृष्ण आपको बुद्धि मोहाच्छन्न हो गयी है; अत: आप
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.7719)
- **Original**: उस कालके भी काल और विधाताके भी ब्रह्मा उन्हें नहीं देखते हैं। नरेश! उत्तम धर्मात्माओंके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.7720)
- **Original**: हैं। सृष्टिका आविर्भाव और तिरोधान उन्हींकी जो-जो स्त्री-पुत्र आदि तथा समस्त ऐश्वर्यकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.7721)
- **Original**: आज्ञासे होता है। मनुष्यके सारे कार्य उन्हींकी वस्तुएँ हैं, वे सभी जलके बुलबुलेके सदृश
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.7722)
- **Original**: आज्ञासे होते हैं, अपनी इच्छासे कुछ भी नहीं अनित्य और विनाशशील हैं। इसीलिये इस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.7723)
- **Original**: होता। महाबली भगवान्‌ परशुराम नारायणके अंश भारतमें संतलोग संसारकों स्वप्र-सदृश मानकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.7724)
- **Original**: हैं। यदि उन्होंने ऐसी प्रतिज्ञा कर ली है कि निरन्तर धर्मका ध्यान करते हैं और भक्तिपूर्वक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.7725)
- **Original**: मैं इक्कीस बार पृथ्वीको राजाओंसे शून्य कर दूँगा तपस्यामें रत रहते हैं। राजन्‌! मालूम होता है,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.7726)
- **Original**: तो उनकी वह प्रतिज्ञा कभी विफल नहीं हो दत्तात्रेयजीने जो ज्ञान दिया था, वह सब आप भूल
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.7727)
- **Original**: सुब्रते! साथ ही मैं यह निश्चित रूपसे गये। यदि है तो फिर आपका मन ब्राह्मणकी हत्या जानता हूँ कि मैं उनका वध्य हूँ। तब भला, करनेमें कैसे प्रवृत्त हुआ? आप तो मनोविनोदके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.7728)
- **Original**: भविष्यकी सारी बातें जानकर भी मैं उनकी लिये शिकार खेलने गये थे। वहाँ ब्राह्मणके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.7729)
- **Original**: शरणमें कैसे जा सकता हूँ? क्‍योंकि प्रतिष्ठित आश्रममें ठहरकर आपने अपूर्व मिष्टान्नका भोजन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 32.7730)
- **Original**: पुरुषोंकी अपकीर्ति मृत्युसे भी बढ़कर किया और व्यर्थ ही ब्राह्मणको मार डाला। जो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 32.7731)
- **Original**: दुःखदायिनी होती है। इतना कहकर सम्राट्‌ गुरु, ब्राह्मण और देवताका अपमान करता है,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 32.7732)
- **Original**: कार्तवीर्यने समरभूमिमें जानेके लिये उद्यत हो उसके इष्टदेव उसपर रुष्ट हो जाते हैं और बिपत्ति
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.7733)
- **Original**: बाजा बजवाया और मालिक कार्य सम्पन्न उसे आ घेरती है। अतः राजेन्द्र! आप दत्तात्रेयजीके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.7734)
- **Original**: करवाये। वह असंख्य राजाओंको, तीन लाख चरणकमलोंका स्मरण कीजिये; क्योंकि गुरु- राजाधिराजोंको, महान्‌ बल-पराक्रमसे सम्पन्न भक्ति सबके सम्पूर्ण विश्लोंका विनाश करनेवाली
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.7735)
- **Original**: एक सौ अक्षौहिणी सेनाओंको तथा असंख्यों है। अब आप गुरुदेवकीं भलीभाँति अर्चना करके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.7736)
- **Original**: घोड़े, हाथी, पैदल सिपाही और रथोंको साथ उन भृगुनन्दनकी शरण ग्रहण कौजिये। परम
- **Translation**: 

---

