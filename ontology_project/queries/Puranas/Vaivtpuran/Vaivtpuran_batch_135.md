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

### Verse 1 (Vaivtpuran 8.6260)
- **Original**: . सती पार्वति! भक्तोंके सद्गसे प्राणियोंके दुःख होता है न सुख, सब अपने कर्मका ही
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.6261)
- **Original**: हृदयमें भक्तिका अंकुर उत्पन्न होता है और भोग है; इसलिये विद्ठान्‌ पुरुष कर्मसे विरत हो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.6262)
- **Original**: भक्तिहीनोंके दर्शनसे वह सूख जाता है। पुनः जाते हैं। सत्पुरुष निरन्तर आनन्दपूर्वक बुद्धिद्वारा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.6263)
- **Original**: वैष्णवोंके साथ वार्तालाप करनेसे वह प्रफुल्लित हरिका स्मरण करनेसे, तपस्यासे तथा भक्तोंके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.6264)
- **Original**: हो उठता है। तत्पश्चात्‌ बह अविनाशी अंकुर सड़से कर्मको ही निर्मूल कर देते हैं; क्योंकि
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.6265)
- **Original**: प्रत्येक जन्ममें बढ़ता रहता है। सती! वृद्धिको इन्द्रिय और उनके विषयोंके संयोगसे उत्पन्न हुआ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.6266)
- **Original**: प्राप्त होते हुए उस वृक्षका फल हरिकी दासता सुख तभीतक रहता है, जबतक उनका नाश नहीं
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.6267)
- **Original**: है। इस प्रकार भक्तिके परिपक्व हो जानेपर हो जाता, परंतु हरिकीर्तनरूप सुख सब कालमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.6268)
- **Original**: परिणाममें वह श्रीहरिका पार्षद हो जाता है। फिर वर्तमान रहता है। तो महाप्रलयके अवसरपर ब्रह्मा, ब्रह्मतोक तथा सतीदेवि! हरिध्यानपरायण भक्तोंकी आयु
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.6269)
- **Original**: सम्पूर्ण सृष्टिका संहार हो जानेपर भी निश्चय ही नष्ट नहीं होती; क्योंकि काल तथा मृत्युज्रय उनपर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.6270)
- **Original**: उसका नाश नहीं होता। अम्बिके! इसलिये मुझे अपना प्रभाव नहीं डाल सकते-यह ध्रुव है। वे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.6271)
- **Original**: [सदा नारायणके चरणोंमें भक्ति प्रदान कौजिये; चिरजीवी भक्त भारतवर्षमें चिरकालतक जीवित
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.6272)
- **Original**: क्योंकि विष्णुमाये! आपके बिना विष्णुमें भक्ति रहते हैं और सम्पूर्ण सिद्धियोंका ज्ञान प्राप्त करके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.6273)
- **Original**: नहीं प्राप्त होती। आपकी तपस्या और पूजन तो स्वच्छन्दतापूर्वक सर्वत्रगामी होते हैं। हरिभक्तोंको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.6274)
- **Original**: लोकशिक्षाके लिये हैं; क्योंकि आप नित्यस्वरूपा पूर्वजन्मका स्मरण बना रहता है। वे अपने करोड़ों
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.6275)
- **Original**: सनातनी देवी हैं और समस्त कर्मोंका फल प्रदान जन्मोंको जानते हैं और उनकी कथाएँ कहते हैं;
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.6276)
- **Original**: करनेवाली हैं। प्रत्येक कल्पमें श्रीकृष्ण गणेशरूपसे फिर आनन्दके साथ स्वेच्छानुसार जन्म धारण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.6277)
- **Original**: आपके पुत्र बनकर आपकी गोदमें आते हैं। करते हैं। वे स्वयं तो पवित्र होते ही हैं, अपनी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.6278)
- **Original**: यों कहकर वे ब्राह्मण तुरंत ही अन्तर्धान लीलासे दूसरोंकों तथा तीर्थोंको पवित्र कर देते हैं।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.6279)
- **Original**: हो गये। वे परमेश्वर इस प्रकार अन्तर्हित होकर इस पुण्यक्षेत्र भारतमें वे परोपकार और सेवाके
- **Translation**: 

---

