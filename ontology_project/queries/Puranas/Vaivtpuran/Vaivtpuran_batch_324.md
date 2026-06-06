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

### Verse 1 (Vaivtpuran 15.6833)
- **Original**: दाता, सर्वेश्वर, सर्वरूप, सम्पूर्ण कर्मोंके साक्षी, वक्ष:स्थलकी, स्वयं सूर्य नाभिकी और सर्वदेवनमस्कृत
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6834)
- **Original**: समस्त लोकोंके दृष्टिगोचर, अप्रत्यक्ष, मनोहर, कट्ढालकी सदा देख-रेख करें। ब्रध्त हाथोंको,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6835)
- **Original**: निरन्तर रसको हरनेवाले, तत्पश्चात्‌ रसदाता, प्रभाकर पैरोॉंको और सामर्थ्यशाली विभाकर मेरे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6836)
- **Original**: सर्वसिद्धिप्रद, सिद्धिस्वरूप, सिद्धेश और सिद्धोंके सारे शरीरकों निरन्तर सुरक्षित रखें। वत्स! यह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6837)
- **Original**: परम गुरु हैं, उन आपकी मैं स्तुति करना चाहता *जगद्विलक्षण' नामक कवच अत्यन्त मनोहर तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6838)
- **Original**: हूँ। वत्स! मैंने इस स्तबराजका वर्णन कर दिया। त्रिलोकीमें परम दुर्लभ है। इसे मैंने तुम्हें बतला
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6839)
- **Original**: यह गोपनीयसे भी परम गोपनीय है।* जो नित्य ब्रह्मोघाच-- त्व॑ ब्रह्म परम धाम ज्योतीरूप॑ सनातनम्‌। त्वामहं स्तोतुमिच्छामि भक्तानुग्रहकारकम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.8617)
- **Original**: + भ्रीकृष्णाजन्यमखण्ड *+ 399 ऋऋकऋकऋककऋकऋऋकऋऊऋऊऋऊऋऊऋकऋऊऋऋऋ्ऋऋ्ऋऋ्ऋ्ऋऋ्ऋक़
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.8618)
- **Original**: #%######### ## #%#### ####ऋ######## कक $%%%$% 4 कर देती है। भगवानकी कथा शोक-सागरका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.8619)
- **Original**: पवित्र हो गया है, वही इस भारतवर्षमें जन्म नाश करनेवाली मुक्ति है। वह कानोंमें अमृतके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.8620)
- **Original**: पाता है। वह यदि श्रीहरिकी अमृतमयी कथाका समान मधुर प्रतीत होती है। कृपानिधे! मैं आपका श्रवण करे, तभी अपने जन्मकों सफल कर भक्त एवं शिष्य हूँ। आप मुझे श्रीहरिकथाका ज्ञान
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.8621)
- **Original**: सकता है। भगवान्‌की पूजा, वन्दना, मन्त्र-जप, प्रदान कीजिये। तप, जप, बड़े-बड़े दान, पृथ्वीके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.8622)
- **Original**: सेवा, स्मरण, कीर्तन, निरन्तर उनके गुणोंका तीर्थोंके दर्शन, श्रुतिपाठ, अनशन, ब्रत, देवार्चन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.8623)
- **Original**: श्रवण, उनके प्रति आत्मनिवेदन तथा उनका तथा सम्पूर्ण यज्ञोंमें दीक्षा ग्रहण करनेसे मनुष्यको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.8624)
- **Original**: दास्यभाव-ये भक्तिके नौ लक्षण हैं*। नारद! जो फल मिलता है, वह सब ज्ञानदानकी सोलहवीं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.8625)
- **Original**: इन सबका अनुष्ठान करके मनुष्य अपने जन्मकों कलाके बराबर भी नहीं है। पिताजीने मुझे आपके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.8626)
- **Original**: सफल बनाता है। उसके मार्ममें विघ्र नहीं आता पास ज्ञान प्राप्त करनेके लिये भेजा है। सुधा-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.8627)
- **Original**: और उसकी पूरी आयु नष्ट नहीं होती। उसके समुद्रके पास पहुँचकर कौन दूसरी वस्तु (जल
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.8628)
- **Original**: सामने काल उसी तरह नहीं जाता है, जैसे आदि) पीनेकी इच्छा करेगा? गरुड़के सामने सर्प। भगवान्‌ श्रीहरि उस भक्तका भगवान्‌ नारायण बोले--कुलको पवित्र
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.8629)
- **Original**: सामीप्य एक क्षणके लिये भी नहीं छोड़ते हैं। करनेवाले नारद! मैं तुम्हें अच्छी तरह जानता
- **Translation**: 

---

