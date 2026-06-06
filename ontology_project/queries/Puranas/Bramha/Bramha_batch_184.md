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

### Verse 1 (Bramha 0.3661)
- **Original**: बह धीरे-धीरे राजाको अम्बिका-वनतक खींच ले पत्नीसे बोला--' कान्ते! इस राजाका मन मृगयाके
- **Translation**: 

---

### Verse 2 (Bramha 0.3662)
- **Original**: गयी। जब घोड़ेपर बैठे-हो-बैठे उमावनमें प्रविष्ट
- **Translation**: 

---

### Verse 3 (Bramha 0.3663)
- **Original**: + इलातीर्धके आविरभावकी कथा + 177 हो गये, तब यक्षिणीने मृगीका रूप छोड़कर दिव्य
- **Translation**: 

---

### Verse 4 (Bramha 0.3664)
- **Original**: स्मरण करती हुई स्त्रीस्वभावके अनुसार ही चेष्टा रूप धारण कर लिया और अशोक वृक्षके नीचे
- **Translation**: 

---

### Verse 5 (Bramha 0.3665)
- **Original**: करती थी। एक दिन जब इला नृत्य कर रही थी, खड़ी हो राजाकों देखकर हँसने लगी। पतिको
- **Translation**: 

---

### Verse 6 (Bramha 0.3666)
- **Original**: बुधने उसे देखा। बे अपने पिताकों नमस्कार कही हुई बातोंको याद करके वह राजासे
- **Translation**: 

---

### Verse 7 (Bramha 0.3667)
- **Original**: करनेके लिये जा रहे थे। इलापर दृष्टि पड़ते ही बोली-'सुन्दरी इला ! तुम अकेली अबला
- **Translation**: 

---

### Verse 8 (Bramha 0.3668)
- **Original**: उन्होंने यात्रा स्थगित कर दी और उसके पास घोड़ेपर चढ़कर पुरुषके वेषमें कहाँ जाती हो,
- **Translation**: 

---

### Verse 9 (Bramha 0.3669)
- **Original**: आकर कहा--'देवि ! तू स्वर्गमें रहकर मेरी प्रिया किसके पास जाओगी ?' उसके मुखसे 'इला'
- **Translation**: 

---

### Verse 10 (Bramha 0.3670)
- **Original**: भार्या हो जा।' इलाने भक्तिपूर्वक बुधकी आज्ञाका शब्द सुनकर राजा क्रोधसे मूर्च्छित हो उठे और
- **Translation**: 

---

### Verse 11 (Bramha 0.3671)
- **Original**: अभिनन्दन करके उसे स्वीकार कर लिया। बुध यक्षिणीकों डॉटकर मृगीका पता पूछने लगे। अपने उत्तम स्थानपर ले जाकर इलाके साथ यक्षिणीने पुनः कहा-'इले! इले! अपने-
- **Translation**: 

---

### Verse 12 (Bramha 0.3672)
- **Original**: प्रेमपूर्वक्ष विहार करने लगे। उसने भी सब आपको अच्छी तरह देख तो लो, फिर मुझे
- **Translation**: 

---

### Verse 13 (Bramha 0.3673)
- **Original**: प्रकारकी सेवाओंसे पतिको संतुष्ट किया। इस मिथ्यावादिनी या सत्यवादिनी कहना।' तब राजाने
- **Translation**: 

---

### Verse 14 (Bramha 0.3674)
- **Original**: प्रकार बहुत समय व्यतीत हो जानेपर बुधने प्रसन्न देखा-उनकी छातीमें दो ऊँचे-ऊँचे स्तन उभर
- **Translation**: 

---

### Verse 15 (Bramha 0.3675)
- **Original**: हो अपनी प्रियासे कहा-“कल्याणी ! मैँ तुझे आये धे। 'यह मुझे क्या हो गया' यह कहते हुए
- **Translation**: 

---

### Verse 16 (Bramha 0.3676)
- **Original**: क्‍या दूँ ? तेरे मनमें जो प्रिय वस्तु हो, उसे माँग राजा चकित हो गये। उन्होंने यक्षिणीसे पूछ--
- **Translation**: 

---

### Verse 17 (Bramha 0.3677)
- **Original**: ले।' इला सहसा बोल उठी--'पुत्र दीजिये।' *सुब्रते ! यह मुझे क्या हो गया-इस बातको आप
- **Translation**: 

---

### Verse 18 (Bramha 0.3678)
- **Original**: बुधने कहा--यह मेरा वीर्य अमोघ तथा ठीक-ठीक जानती हैं। अत: बताइये। आप कौन
- **Translation**: 

---

### Verse 19 (Bramha 0.3679)
- **Original**: प्रेमसे प्रकट हुआ है। अतः तेरे गर्भसे विश्वविख्यात हैं ? इसका भी परिचय दीजिये।' क्षत्रिय-पुत्र उत्पन्न होगा। उससे चन्द्रवंशकी वृद्धि यक्षिणी बोली--हिमालयकी श्रेष्ठ गुफामें मेरे
- **Translation**: 

---

### Verse 20 (Bramha 0.3680)
- **Original**: होगी। वह तेजमें सूर्य, बुद्धिमें बृहस्पति, क्षमामें पति यक्षराज समन्यु निवास करते हैं। मैं उन्हींकी
- **Translation**: 

---

