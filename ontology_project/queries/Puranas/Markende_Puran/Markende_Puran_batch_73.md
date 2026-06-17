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

### Verse 1 (Markende Puran 0.1441)
- **Original**: + प्रजाक्री सृ्ि, निब्राम स्घात, जीविकाक्रे तपाय और थ्रणांक्राम-धर्मके पालतका माहात्प्य * श्र च्हध्या># € 0 0220:2286 # 35000 है उ-फफ + 0000 2 23:53 0000 5. 80303 75080 6.8 8050 106 34447 *16 186 4 #% 155 ऊऋ46 4 467 है <7/7 हों, अपनी समृद्धिसे वुक्त किरान रहते हाँ, जो
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1442)
- **Original**: पृथ्वोके साथ संयोग होनेसे बिना जोते-बोये ही खेतों और उपभोगयोग्य भूपि (थाग-बगोनों)क्े
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1443)
- **Original**: ग्राम्य और आरप्य---सब मिलकर चौंदह एकारओे बीचपें बस। हो, ठसका नाप गाँव है। जहाँ किसी
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1444)
- **Original**: अह्ा पैदा हुए। बुक्षों और लताओंगें ज्ल्ल्के कार्यके लिये मुख्य अन्य दगर आदिसे आकर
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1445)
- **Original**: अनुसार फूल और फल लगने लगे! जेतायगर्ये बसते हों, उस्तकों बस्ती कहते हैं। जहाँ अधिकांश । पहल-पहल अहूछा प्रादुर्भब हुआ। उसोसे उस वृष्टोका निवास हो, जहाँके रहेनेवाले अपने पास
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1446)
- **Original**: युग्ें सुब प्रजाका जीरूग-निर्वाह होने हुणा' खेत से होंनेपर भी दूस्तेकों भूभिपर उाधिकार
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1447)
- **Original**: फिर अकस्मत्‌ सब्र लोगोंके मरमें शव और जमाते और भोगते हैं, जह गाँव द्र्सीके नाससे
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1448)
- **Original**: लोभका प्राकटय हुआ। इससे ते ए+-दूसरेके परत पुआारा जाता है। वहाँ प्राय: थे हो लोग चिब्वास
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1449)
- **Original**: ईर्ष्या ऱने लगे और अपनों शक्तिक्रे अनुम्नार करते हैं, जो राजाके प्रिय हों। जहाँ ूहलले अपने
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1450)
- **Original**: दो, खेत, पर्वत, बृक्ष और झाद्ियोपर आंध्कऋर बर्तन- धाँड़े भाडियॉपर लादकर रखते हों, बना
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1451)
- **Original**: जमाने छगे। उनवेय इस दोपसे सबके देखते- बाजारके ही गोरस्त मिलता हो, गायोंका समूह
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1452)
- **Original**: देखते सब अदाज पड हो गये। पृथ्वीव एक साथ रहता हो, जहाँ इच्छानुसार भूमि रहनेके छिये
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1453)
- **Original**: हो स0 ओपधियोंको अपना ग्रात् बना लिया सुलभ हो. उस स्थानक्ला ताप घोध हैं। अनाजके नए होनेसे प्रजा भखसे व्याकृल ड्रॉकर इस प्रकार नगर आदिका निर्माण करके
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1454)
- **Original**: फिर इधर «3धर 'रकने लगी और अनतपें ब्रह्मजीकों प्रजाने अपने रहनेके लिये घर बनाये। से घर इस
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1455)
- **Original**: शरणमें गो । ब्रह्मजीने भो प्रजाका सारा समाचार उद्देश्यसे बनाये गये थे कि वहाँ शीए-उष्ण आदि
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1456)
- **Original**: टीक-ठीक जानकर पृथ्योंको गावक्के रूपमें बाधा इन्द्रोंसे रक्षा हो सके। जैसे 5हले उनके शरके
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1457)
- **Original**: और मेहर प्रत॑तकों बछड्ठा बनाकर उसका दूध आरके वृक्ष होते थे और बहाँ उन्हें जै»
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1458)
- **Original**: दुह्। ध्क्लाजीने दुधके रूपमें सत्र प्रकारके शात्रन झुविशएँ प्राप्त होती थीं, उप सबका स्परण करके दुह लिये थे, ते ही बीजरूपपें प्ररूट हुए और उन्होंने घर जनाये। जैसे वृक्षकी शाखाएँ एक्रके
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1459)
- **Original**: उसमे ग्राम्य तथा आरण्धथ- सब प्र>रके अज्र पैदा बाद दूसरी तथा छोटी-बड़ी, कैचों-नाची हो!
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1460)
- **Original**: हुए, छझो फलके पक जानेगर काट लिये जाते हैं। हैं, उसो प्रकार उन्होंने अनेर प्रकास्को शालाएँ
- **Translation**: 

---

