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

### Verse 1 (Vaivtpuran 15.8670)
- **Original**: आओगे।' , ज्ञानगज़ामें अवगाहन करनेपर मनुष्य परम पदको श्रीराधाकों बड़े ही प्रेमके साथ हृदयसे प्राप्त हो जाता है। तथा जैसे तुलसीबनमें, गोशालामें,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.8671)
- **Original**: लगाकर भगवान्‌ने कहा--' बाराहकल्पमें मैं पृथ्वीपर श्रीकृष्ण-मन्दिरमें, वृन्दावनमें, हरिद्वारमें एवं अन्य
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.8672)
- **Original**: जाऊँगा और ब्रजमें जाकर वहाँके पवित्र काननोंमें ती्थोमें भी मृत्यु होनेपर मनुष्यको परम धामकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.8673)
- **Original**: तुम्हारे साथ विहार करूँगा। मेरे रहते तुमको क्‍या प्राप्ति होती है। तीर्थोमें स्नान करने या गोता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.8674)
- **Original**: भय है?' लगानेसे पापियोंके पाप धुल जाते हैं। फिर उन उधर विरजादेवी नदी हो गयीं और उनके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.8675)
- **Original**: * अ्रीकृष्णंजन्मखण्ड * 401 4444 444 4 4
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.8676)
- **Original**: ।।]+]+ पद ब, श्रीकृष्णके द्वारा जो सात सुन्दर पुत्र हुए थे-वे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.8677)
- **Original**: लीलामय श्रीराधा और श्रीकृष्ण वाराहकल्पमें लवण, इक्षु, सुरा, घृत, दधि, दुग्ध और जलरूप
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.8678)
- **Original**: पृथ्वीपर अवतीर्ण हुए। श्रीराधाजी गोकुलमें सात समुद्र हो गये (यह सब श्रीराधा और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.8679)
- **Original**: श्रीवृषभानुके घर प्रकट हुईं। यह कथा प्रसड्भानुसार श्रीकृष्णजी लीला ही है, जो ब्रजमें परम दिव्य [पहले भी आ चुकी है। (भगवान्‌, श्रोराधा- पवित्र॒तम विलक्षण प्रेमरसधारा बहानेके लिये
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.8680)
- **Original**: कृष्णके अवतार तथा ब्रजकी मधुरतम लीलाका निमित्तरूपसे कौ गयी थी)। इसी निमित्तसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.8681)
- **Original**: यह एक निमित्त कारणमात्र है।)( अध्याय 1-3) मजाक जज पृथ्वीका देवताओंके साथ ब्रहलोकमें जाकर अपनी व्यथा-कथा सुनाना, ब्रह्माजीका उन सबके साथ कैलासगमन, कैलाससे ब्रह्मा, शिव तथा धर्मका वैकुण्ठमें जाकर श्रीहरिकी आज्ञासे गोलोकमें जाना और वहाँ विरजातट, शतशजञ पर्वत, , रासमण्डल एवं 920 आदिके प्रदेशोंका अवलोकन करना, गोलोकका वर्णन नारदजीने पूछा--वेदवेत्ताओंमें श्रेष्ठ नारायण!
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.8682)
- **Original**: किस उद्देश्यसे तुम्हारा आगमन हुआ है? विश्वास किसकी प्रार्थासे और किस कारण जगदीश्वर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.8683)
- **Original**: करो, तुम्हारा भला होगा। कल्याणि! सुस्थिर हो श्रीकृष्णे इस भूतलपर अबतार लिया था?
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.8684)
- **Original**: जाओ, मेरे रहते तुम्हें क्या भय है? श्रीनारायणने कहा--प्राचीन कालकी बात इस प्रकार पृथ्वीको आश्वासन देकर ब्रह्माजीने है। वाराह-कल्पमें पृथ्वी असुरोंके अधिक भारसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.8685)
- **Original**: देवताओंसे आदरपूर्वक पूछा--' देवगण ! किसलिये आक्रान्त हो गयी थी; अत: शोकसे अत्यन्त
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.8686)
- **Original**: तुम्हारा मेरे समीप आगमन हुआ है?' पीड़ित हो वह ब्रह्माजीकी शरणमें गयी। उसके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.8687)
- **Original**: . ब्रह्माजीकी यह बात सुनकर देवतालोग साथ असुरोंद्वारा सताये गये देवता भी थे, जिनका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.8688)
- **Original**: उन प्रजापतिसे बोले--प्रभो! पृथ्वी दैत्योंके चित्त अत्यन्त उद्ठिग्ग हो रहा था। पृथ्वी उन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.8689)
- **Original**: भारसे दबी हुई है तेथां हम भी उनके कारण देवताओंके साथ ब्रह्माजीकी दुर्गम सभामें गयी।
- **Translation**: 

---

