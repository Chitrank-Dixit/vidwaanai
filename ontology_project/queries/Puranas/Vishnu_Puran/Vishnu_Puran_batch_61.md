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

### Verse 1 (Vishnu Puran 0.1201)
- **Original**: और यदि सुरुचिके वाक्योंसे तुझे अत्यन्त दुःख ही हुआ है तो सर्वफलदायक पुण्यके संग्रह करनेका प्रयल कर
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1202)
- **Original**: तू सुझोल, चुण्यात्मा, प्रेमी और समस्त प्राणियोंका हितैधी बन, क्योंकि जैसे नीची भूमिकी ओर ढलकता हुआ जल अपने-आप ही पाजमें आ जाता है वैसे हो सत्पात्र मनुष्यके पास स्वतः ही समस्त सम्पत्तियाँ आ जाती हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1203)
- **Original**: घुल खोल्ला--माताजी ! तुमने मेरे चित्तको झान्त करनेके छिये जो बचन बड़े हैं वे दुर्वाक्योंसे बिथे हुए मेंरे हृदयमें तनिक भी नहीं ठहरते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1204)
- **Original**: इसलिये मैं तो अब नहीं प्रयल करूँगा जिससे सम्पूर्ण ल्लेकोंसे आदरणीय सर्वश्रेष्ठ पदक प्राप्त कर सकूँ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1205)
- **Original**: राजाकी प्रेयसी तो अवदय सुरुचि ही है और मैंने उसके उदरसे जन्म भी नहीं लिया है, तथापि हे माता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1206)
- **Original**: अपने गर्भमें बढ़े हुए मेरा प्रभाव भी तुम देखना
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1207)
- **Original**: उत्तम, जिसक्तरे उसने अपने गर्भमें धारण किया है, मेरा भाई ही है। पिताका दिया हुआ राजासन कही प्राप्त करे। [ भगवान्‌ करें
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1208)
- **Original**: ऐसा ही हो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1209)
- **Original**: माताजी ! मैं किसी दूसरेके दिये हुए पदका इच्छुन्क नहीं हूँ; मैं तो अपने पुरुषार्थसे ही उस पटकी इच्छा करता हूँ जिसको पिताजीने भी नहों प्राप्त किया है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1210)
- **Original**: श्रीपराहरजी जोले-- मातासे इस प्रकार कह घुव॑ उसके महलसे निकल पड़ा और फिर नगरसे बाहर आकर जाहरी उपबन्ें पहुँचा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1211)
- **Original**: यहाँ धुयने पहलेसे ही आये हुए सात मुनोश्वरोंको कृष्ण मृग-चर्मके बिछौनोंसे युक्त आसतॉपर .यैठे देखा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1212)
- **Original**: उस राजकुमारने उन सबको प्रणाम कर अति नम्नता और समुचित अभिवादनादिपूर्यक उनसे कहा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1213)
- **Original**: ध्ंवनें कहा--हे महात्माओ'! मुझे आंप संनीतिसे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1214)
- **Original**: आ« 131 ] ऋषय ऊूचूः चतुःपश्चाब्दसम्भूतो बालस्त्वे नृपनन्दन। निर्वेदकारणं किझ्नलित्तव नाद्यापि वर्त्ती
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1215)
- **Original**: 34 न चिन्त्यं भवतः किल्निदप्रियते भूषति: पिता । ने चैवेष्टवियोगादि तब पश्याम बालक
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1216)
- **Original**: 35 झरीरे न अर ते व्याधिरस्माभिरुपलक्ष्यते । निर्वेदः किन्निमित्तस्ते कथ्यतां यदि विद्यते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1217)
- **Original**: 36 ओपराशर उवाच ततः स कथयामास सुरुच्या यदुदाहतम्‌। तन्निशम्य॒ ततः प्रोचुर्मुनयस्ते परस्परम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1218)
- **Original**: 37 अहो क्षात्रं पर॑ तेजो यालस्यापि यदक्षमा । सपलया मातुरुक्त यदधृदयान्नापसर्पति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1219)
- **Original**: 38 भो भो क्षत्रियदायाद निर्वेदाद्मत्व्याधुना । कर्तु व्यवसितं तन्न: कश्यतां यदि रोचते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1220)
- **Original**: 39 यश्ञ कार्य तवास्माभि: साहाय्यममितझुते । तदुच्यतां विवक्षुस्वमस्माभिरुपलक्ष्यसे
- **Translation**: 

---

