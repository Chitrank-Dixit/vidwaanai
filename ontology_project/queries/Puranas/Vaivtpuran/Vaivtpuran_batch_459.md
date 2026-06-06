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

### Verse 1 (Vaivtpuran 23.2142)
- **Original**: पिण्ड बिलकुल खाली था। दूसरी कोई भी वस्तु विद्यमान हैं। पातालसे लेकर ब्रह्मलोकतक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.2143)
- **Original**: वहाँ नहीं थी। उसके मनमें चिन्ता उत्पन्न हो अनगिनत ब्रह्माण्ड बताये गये हैं। अत: उनकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.2144)
- **Original**: गयी। भूखसे आतुर होकर वह बालक बार- संख्या कैसे निश्चित की जा सकती है? ऊपर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.2145)
- **Original**: बार रुदन करने लगा। फिर जब उसे ज्ञान हुआ, बैकुण्ठलोक है। यह ब्रह्माण्डसे बाहर है। इसके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.2146)
- **Original**: तब उसने परम पुरुष श्रीकृष्णका ध्यान किया। ऊपर पचास करोड़ योजनके विस्तारमें गोलोकधाम है। श्रीकृष्णे समान ही यह लोक भी नित्य और चिन्मय सत्यस्वरूप है। पृथ्वी सात द्वीपोंसे सुशोभित है। सात समुद्र इसकी शोभा बढ़ा रहे हैं। उनचास छोटे-छोटे द्वीप हैं। पर्बतों और बनोंकी तो कोई संख्या ही नहीं है। सबसे ऊपर सात स्वर्गलोक हैं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.2147)
- **Original**: ब्रह्मलोक भी इन्हींमें सम्मिलित है। नीचे सात पाताल हैं। यही ब्रह्माण्डका परिचय तब वहाँ उसे सनातन ब्रह्मज्योतिके दर्शन प्राप्त हुए। वे ज्योतिर्मय श्रीकृष्ण नवीन मेघके समान
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.2148)
- **Original**: श्याम थे। उनके दो भुजाएँ थीं। उन्होंने पीताम्बर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.2149)
- **Original**: पहन रखा था। उनके हाथमें मुरली शोभा पा रही थी। मुखमण्डल मुस्कानसे भरा था। भक्तोंपर अनुग्रह करनेके लिये वे कुछ व्यस्त-से जान पड़ते थे। पिता परमेश्वको देखकर वह बालक संतुष्ट होकर हँस पड़ा। फिर तो वरके अधिदेवता है। पृथ्वीसे ऊपर भूलोंक, उससे परे भुवरलोंक,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.2150)
- **Original**: श्रीकृष्णने समयानुसार उसे वर दिया। कहा-- भुवर्लोकसे परे स्वलोक, उससे परे जनलोक,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.2151)
- **Original**: 'बेटा! तुम मेरे समान ज्ञानी बन जाओ। भूख जनलोकसे परे तपोलोक, तपोलोकसे परे सत्यलोक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.2152)
- **Original**: और प्यास तुम्हारे पास न आ सके। प्रलयपर्यन्त और सत्यलोकसे परे ब्रह्मलोक है। ब्रह्मसोक ऐसा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.2153)
- **Original**: यह असंख्य ब्रह्माण्ड तुमपर अवलम्बित रहे। तुम प्रकाशमान है, मानो तपाया हुआ सोना चमक
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.2154)
- **Original**: निष्कामी, निर्भभ और सबके लिये वरदाता बन रहा हो। ये सभी कृत्रिम हैं। कुछ तो ब्रह्माण्डके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.2155)
- **Original**: जाओ। जरा, मृत्यु, रोग और शोक आदि तुम्हें भीतर हैं और कुछ बाहर। नारद! ब्रह्माण्डके [कष्ट न पहुँचा सकें।! यों कहकर भगवान्‌ नष्ट होनेपर ये सभी नष्ट हो जाते हैं; क्योंकि
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.2156)
- **Original**: श्रीकृष्णने उस बालकके कानमें तीन बार षडक्षर पानीके बुलबुलेकी भाँति यह सारा जगतू अनित्य
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.2157)
- **Original**: महामन्त्रका उच्चारण किया। यह उत्तम मन्त्र है। गोलोक और बैकुण्ठलोकको नित्य, अविनाशी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.2158)
- **Original**: वेदका प्रधान अड्ग है। आदिमें '3&' का स्थान एवं अकृत्रिम कहा गया है। उस विराट्मय
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.2159)
- **Original**: है। बीचमें चतुर्थी विभक्तिके साथ “कृष्ण' ये बालकके प्रत्येक रोमकूपमें असंख्य ब्रह्माण्ड दो अक्षर हैं। अन्तमें अग्निकी पत्नी 'स्वाहा' निश्चितरूपसे विराजमान हैं। एक-एक ब्रह्माण्डमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.2160)
- **Original**: सम्मिलित हो जाती है। इस प्रकार ' 37 कृष्णाय
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.2161)
- **Original**: + प्रकुसिसिफ्ड + 99 81525 24684£4£4+:4££2624888468#85:82480848£8080808(86:7][7:680+:0888]8::]442£8
- **Translation**: 

---

