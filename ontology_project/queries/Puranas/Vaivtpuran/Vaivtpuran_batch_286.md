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

### Verse 1 (Vaivtpuran 13.11862)
- **Original**: अपनी चेतना खो बैठे। चतुर पुरुषोंके लिये कारण आपको सब कुछका ज्ञान है। फिर मैं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11863)
- **Original**: नारीका वियोग सब शोकोंसे बढ़कर होता है। आपको क्‍या समझाऊँ! उत्तम बचन, कटु वचन,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11864)
- **Original**: एक ही क्षणमें उन्हें चेत हुआ और वे अपने क्रोध, संताप, लोभ, मोह, काम, क्षुधा, पिपासा,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11865)
- **Original**: प्राण त्याग देनेको उद्यत हो गये। उन्होंने वहीं स्थूलता, कृशता, नाश, दृश्य, अदृश्य तथा उत्पन्न
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11866)
- **Original**: योगासन लगाकर वायुधारणा आरम्भ की। इतनेहीमें होना-ये सब शरीरके धर्म हैं। न तो जीवके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11867)
- **Original**: एक ब्राह्मण-बालक वहाँ आ पहुँचा। उसके धर्म हैं और न आत्माके ही। सत्त्व, रज और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11868)
- **Original**: हाथमें दण्ड और चक्र था। उसने लाल बस्त्र तम-इन तीन गुणोंसे शरीर बना है। वह भी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11869)
- **Original**: धारण किया था और ललाठमें उत्तम चन्दन लगा नाना प्रकारका है। सुनिये, मैं आपको बताती
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11870)
- **Original**: रखा था। उसकी अद्भकान्ति श्याम थी। वह हूँ। किसी शरीरमें सत्त्तगुणकी अधिकता होती
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11871)
- **Original**: ब्रह्मतेजसे जाज्वल्यमान था। उसकी अवस्था है, किसीमें रजोगुणकी और किसीमें तमोगुणकी।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11872)
- **Original**: बहुत छोटी थी; परंतु वह शान्त, ज्ञानवान्‌ तथा मुने! कहीं भी सम गुणोंवाला शरीर नहीं है।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11873)
- **Original**: वेदवेत्ताओंमें श्रेष्ठ जान पड़ता था। उसे देख जब सत्त्वगुणका उद्रेक होता है तब मोक्षकी ! दुर्बासाने वेगपूर्वक प्रणाम किया, वहीं बैठाया इच्छा जाग्रतू होती है, रजोगुणकी वृद्धिसे कर्म और भक्तिभावसे उसका पूजन किया। ब्राह्मण करनेकी इच्छा प्रबल होती है और तमोगुणसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11874)
- **Original**: बटुकने मुनिको शुभाशीर्वाद दे वार्तालाप आरम्भ जीब-हिंसा, क्रोध एवं अहंकार आदि दोष प्रकट
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11875)
- **Original**: किया। उसके दर्शन और आशीर्वादसे मुनिका होते हैं। क्रोधसे निश्रय ही कटु वचन बोला
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11876)
- **Original**: सारा दुःख दूर हो गया। वह नीतिविशारद जाता है। कटु बचनसे शत्रुता होती है और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11877)
- **Original**: विचक्षण बालक क्षणभर चुप रहकर अमृतमयी शत्रुतासे मनुष्यमें तत्काल अप्रियता आ जाती है।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11878)
- **Original**: बाणीमें बोला। अन्यथा इस भूतलपर कौन किसका शत्रु है? कौन. शिशुने कहा--सर्वज्ञ विप्र ! आप गुरुमन्त्रके प्रिय है और कौन अप्रिय ? कौन मित्र है और! प्रसादसे सब कुछ जानते हैं; फिर भी शोकसे कातर कौन बैरी? सर्वत्र शत्रु और मित्रकी भावनामें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11879)
- **Original**: हो रहे हैं; अत: मैं पूछता हूँ, इसका यथार्थ रहस्य इन्द्रियाँ ही बीज हैं। स्त्रियोंक लिये पति प्राणोंसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11880)
- **Original**: क्या है? ब्राह्मणोंका धर्म तप है। तपस्यासे तीनों भी अधिक प्रिय है और पतिके लिये स्त्री प्राणोंस
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11881)
- **Original**: लोकोंको वशमें किया जा सकता है। मुने! इस
- **Translation**: 

---

