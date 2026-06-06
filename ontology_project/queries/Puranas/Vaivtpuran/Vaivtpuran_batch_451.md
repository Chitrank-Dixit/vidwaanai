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

### Verse 1 (Vaivtpuran 23.1982)
- **Original**: करता है, उसके द्वारा भगवती प्रकृतिकी पूजा 'सुरभि', दैत्योंकी माता 'दिति', 'कद्ठ', 'बिनता'
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1983)
- **Original**: सम्पन्न होती है। जिसने ब्राह्मणकी अष्टवर्षा और '“दनु'-ये सभी देवियाँ सृष्टिका कार्य
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1984)
- **Original**: कुमारीका बस्त्र, अलंकार एवं चन्दन आदिसे सँभालती हैं। इन्हें भगवती प्रकृतिकी 'कला'
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1985)
- **Original**: अर्चन कर लिया, उसके द्वारा भगवती प्रकृति कहा जाता है। अन्य भी बहुत-सी कलाएँ हैं।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1986)
- **Original**: स्वयं पूजित हो गयीं। उत्तम, मध्यम और कुछ कलाओंका परिचय कराता हूँ, सुनों।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1987)
- **Original**: अधम--सभी स््रियाँ भगवती प्रकृतिके अंशसे चन्द्रमाकी पत्नी 'रोहिणी” और सूर्यको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1988)
- **Original**: उत्पन्न हैं। जो श्रेष्ठ आचरणवाली तथा पतिब्रता 'संज्ञा' हैं। मनुकी भारयाका नाम 'शतरूपा' है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1989)
- **Original**: स््रियाँ हैं, इन्हें प्रकृतिदेवीका सत्त्वांश समझना “शी ' इन्द्रकी धर्मपत्नी हैं। बृहस्पतिकी सहरधर्मिणी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1990)
- **Original**: चाहिये। इनको “उत्तम” माना जाता है। जिन्हें “तारा' हैं। 'अरुन्धती' वसिष्ठमुनिकी धर्मपत्नी हैं।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1991)
- **Original**: भोग ही प्रिय है, वे राजस अंशसे प्रकट स्त्रियाँ *अहल्या' गौतमकी, ' अनसूया' अत्रिकी, 'देवहूति'
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1992)
- **Original**: “मध्यम ' श्रेणीकी कही गयी हैं। वे सुख-भोगमें कर्दममुनिकी और 'प्रसूति' दक्षकी पत्नियाँ हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1993)
- **Original**: आसक्त होकर सदा अपने कार्यमें लगी रहती हैं। पितरोंकी मानसी कन्या “मेनका ' पार्वतीकी जननी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1994)
- **Original**: प्रकृतिदेवीके तामस अंशसे उत्पन्न स्त्रियाँ 'अधम' हैं।लोपामुद्रा', 'आदूति', कुबेरकी पत्नी, वरुणकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1995)
- **Original**: कहलाती हैं। उनके कुलका कुछ पता नहीं रहता। पत्नी, यमकी पत्नी, 'बलिकी भार्या विन्ध्यावली',
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1996)
- **Original**: वे मुखसे दुर्बववचन बोलनेवालोी, कुलटा, धुूर्त,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1997)
- **Original**: श्र *+ संक्षिक्तअद्ाबैज्तंपुराण + %$#%##%#%#%%##%#### 66% #&## #### 66% ##%##ऋ## #%& कक कक ऋऊ कक कक 4488 66#6##&%%%$% स्वेच्छाचारिणी और कलहप्रिया होती हैं। भूमण्डलकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1998)
- **Original**: सम्मान किया। इसके बाद ये देवी तीनों लोकोंमें कुलटाएँ, स्वर्गकी अप्सराएँ तथा व्यभिचारिणी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1999)
- **Original**: देवताओं और मुनियोंकी पूजनीया हो गयीं। स्त्रियाँ प्रक्तिका तामस अंश कही गयी हैं। नारद! इस प्रकार प्रकृतिके सम्पूर्ण रूपका वर्णन कर दिया। वे सभी देवियाँ पृथ्वीपर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.2000)
- **Original**: पुण्यक्षेत्र भारतमें पूजित हुई हैं। दुर्गा दुर्गतिका नाश करती हैं। राजा सुरथने सर्वप्रथम इनकी उपासना की है। इसके पश्चात्‌ रावणका वध करनेकी इच्छासे भगवान्‌ श्रीरामने देवीकौ पूजा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.2001)
- **Original**: सर्वप्रथम गोलोकमें रासमण्डलके भीतरे परमात्मा
- **Translation**: 

---

