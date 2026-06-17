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

### Verse 1 (Markende Puran 0.1861)
- **Original**: आरूदक्की बात है।! तदरुन्तर कुछ कालके पश्षात्‌ पेरी यह ठात सुल्कर सूनिकों आँखें क्रोधसे मृगोवे उत्तम लक्षणोंसे सम्पन्न पुत्रकी जन्प दिया। * पितर्व्यसाँते ना गीभिजियते हि पति! स्तत्म्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1862)
- **Original**: सर्ति तातें रूथ॑ चाएं दुपोपिं सुनिम्तत्तम। (74। 34-55)
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1863)
- **Original**: ब्रैयत मन्‌की उत्पत्ति और उनके पन्यन्तरकां वर्णन + श्र 54174 7 #% 4 3 अधाजां # 62-55
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1864)
- **Original**: 5-32#4 #1062 2:37 » * 2 हा85:5%2-+ 7 55 » #0 न हु: » 0 + हज 22:52 जज, 664 #070 हूँ उसके उत्पन्न होनेपर सम्पूर्ण भूत आनन्दका
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1865)
- **Original**: किग्रे। अस्त्र-शस्त्रोंका ज्ञाता होकर उसने सामूण अनुभव करने लगे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1866)
- **Original**: बिशेषतः एजाको बड़ी प्रसन्नता
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1867)
- **Original**: शत्षुऑको परास्त किया और उन्हें पिताके पास ले हुई। मृगी भी झूपसे छूटकर उश्मम लोकॉकों
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1868)
- **Original**: आकर उनकी आज्ञा सिलनेपर छुटकारा दिया।। बह चल्ली गवी। तदतन्तर सब ऋषियोंने आकर की
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1869)
- **Original**: सदा अपने धर्मके पालनमें लगा रहता था। उसके भ्राचों सर्मुद्धि देख उस यालकका नापकरण किया--
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1870)
- **Original**: फ्ता भी शरीर त्यामनेके पशात्‌ तप और यहसे “तापसो थोनिमें पड़ी हुई माततके गर्भसे इसकः
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1871)
- **Original**: ठपार्जित पुण्वलोकॉंमें गये। साथ गृथ्वीको जीतकर जन्म हुआ है, इसलिये यह ज्रालक संसारपें तामस
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1872)
- **Original**: तामस राजा हुआ और फिर मगुके पदपर प्रतिध्ित आमसे चिस्यात होगा।' तत्पश्चात्‌ पिल अपने पुत्र
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1873)
- **Original**: हुआ। अब तामस मन्वस्तस्का वर्णन सुनों। उसपें तामसका लालन-मालत करते लगे। जब तामसकों
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1874)
- **Original**: सत्य, सुधी, सुरूप और हरि-ये चोर देवगण हुए। कुछ समझ हुई तो उसने पितासे पूछा--' वात!
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1875)
- **Original**: इसमेंसे एक-एक गणपें सत्ताईस-सत्नाईमस देखता हैं। आप कौन हैं? मैं आपका पुत्र किस्त प्रव्णार हुआ ?
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1876)
- **Original**: उन देवताओंके इन्द्रका नाम शिखी था। वे अत्वन्त मेरी माता कौन हैं और आप किरलिये यहाँ आये
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1877)
- **Original**: बली और महापराक्रमी थे। उन्होंने सौ चज्ञोक्ठी हैं? यह सत्र सच-सरूच बबाइये।' अनुष्लनन करके इस पदल्ो प्राप्त किया था। ज्योतिर्धर्या, तब पिताने अपने ग़ज्यसे च्युते होने आदिसे
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1878)
- **Original**: परंथु, काव्य, चैन्न, अग्रि, बलक आर पोबर--ये हो णेकर सब बृक्तान्त पुत्रक्ो बतलाया। ये सब बातें
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1879)
- **Original**: स्त उस समयके सप्तर्षि थे। नर, क्षान्ति, शान्त, सुसकर तामसने भगवात्‌ सूर्यकों आऋणएधना को और
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1880)
- **Original**: कन्त, जानु और जछ्ू जादि भमहावली राजा तामस उनसे उपसंहास्सहित सम्पूर्ण दिव्य अस्त्र प्राप्त
- **Translation**: 

---

