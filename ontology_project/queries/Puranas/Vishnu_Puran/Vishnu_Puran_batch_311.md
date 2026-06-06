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

### Verse 1 (Vishnu Puran 0.6201)
- **Original**: 75 पुनस्तयोक्तं स ज्ञात्वा सत्य॑ सत्यवतां वर: । कानने स निराहारस्तत्याज स्व॑ं कलेवरम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6202)
- **Original**: 76 कुत्तेका जन्प ल्त््या
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6203)
- **Original**: तथा वह झुमलक्षणा काशीनरेशवी कन्या हुई, जो सब प्रकारके विज्ञानसे युक्त, सर्वलक्षणसम्पन्ना और जातिस्मरा (पूर्वजन्मका बृत्तान्त जाननेवाली) थी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6204)
- **Original**: राजाने उसे किसी बरकगे देनेकी इच्छा की, किन्तु उस सुन्दरीके ही रोक देनेपर यह उसके विचाहादिसे उपरत हो गये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6205)
- **Original**: तब उसने दिख्य दुृष्टिसे अपने पतिको श्रान हुआ जान विदिशा नामक नगरमें जाकर उसे ब्रहाँ कुत्तेकों अवस्थामें देखा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6206)
- **Original**: अपने महाभाग पतिकों श्रानरूपमें देखकर उस सुन्दरीने उसे सत्कारपूर्वक अति उत्तम भोजन कराया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6207)
- **Original**: उसके दिये रुए उस अति मधुर और इच्छित अन्नको खाकर यह अपनो जातिके अनुकूल नाना प्रकास्की चादुता प्रदर्शित करने छूगा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6208)
- **Original**: उसके चाटुता करनेसे अत्यन्त संकुचित हो उस बालिकाने कुत्सित योनिमें उत्पन्न हुए. उस अपने प्रियतमको प्रणाम कर उससे इस प्रकार कहा--
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6209)
- **Original**: “महाराज ! आप अपनी उस उदास्ताका स्मरण कीजिये जिसके कारण आज आप श्रान-योनिकों श्राप्त होकर मेरे चादुकार हुए हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6210)
- **Original**: हे प्रभो ! क्‍या आपको यह स्मरण नहों है कि तीर्थस्नानके अनन्तर पाखण्डीसे वार्ताल्‍लाप करनेके कारण ही आपको यह कुत्सित योनि मिली है 7?”
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6211)
- **Original**: श्रीपराशरजी बोल्ले--काहिराजसुताद्वारा इस प्रकार स्परण कराये जानेपर उसने बहुत देरतक अपने पूर्वजश्मका चिन्तन किया। तब उसे अति दुर्लभ निर्वेद प्राप्त हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6212)
- **Original**: उसने अति उदास चित्तसे नगरके बाहर आ प्राण त्याग दिये और फिर -शृगाक-योनिमें जन्म लिया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6213)
- **Original**: तब, काशिराजकन्या दिव्य दृष्टिसे ठसे दूसरे जझमें श्रूगाल हुआ जान उसे देखनेके लिये कोलाहलू-पर्वतपर गयी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6214)
- **Original**: वहाँ भी अपने पतिको श्ृूगाल-योनिमें उत्पन्न हुआ देख वह सुन्दरों राजकन्या उससे बोली---
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6215)
- **Original**: “हे राजेन्द्र ! श्रान-योनिमें जन्म लेनेपर मैंने आपसे जो पाखण्डसे वार्तात्मपविषयक पूर्वजन्पका कुतात्त कहा था क्‍या यह आपको स्मरण है ?”
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6216)
- **Original**: तब सत्यनिष्ठोमें श्रेष्ठ सजा झतधघनुने उसके इस प्रकार कहनेपर सार सत्य वृत्तात्त जानकर निणहार रह वनमें अपना दारीर छोड़ दिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6217)
- **Original**: 544./ भूयस्ततो वृको जज्ञे गत्वा तं निर्जने बने । स्मारयामास॒भत्तरिं पूर्ववृत्तमनिन्दिता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6218)
- **Original**: 77 न त्वं वृको महाभाग राजा शतधनुर्भवान्‌ । श्वा भूत्या त्वे श्रृगाल्ो5भूर्वुकत्व॑ साम्प्रते गतः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6219)
- **Original**: 78 स्मारितेन यदा त्यक्तस्तेनात्मा गृश्नतां गत: । अपापा सा पुनश्लैनं बोधयामास भामिनी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6220)
- **Original**: 79 नरेन्द्र स्मर्यतामात्मा हाल ते गृप्नचेष्टया
- **Translation**: 

---

