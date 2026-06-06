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

### Verse 1 (Bramha 0.701)
- **Original**: थे। उसके बाद विदर्भके भीम नामक पुत्र हुआ। अकेले ही नर्मदाके तटपर जाकर उन्होंने मेकला,
- **Translation**: 

---

### Verse 2 (Bramha 0.702)
- **Original**: उसके पुत्रका नाम कुन्ति हुआ। कुन्तिसे धृष्टका मृत्तिकाबती तथा ऋ्षवान्‌ पर्वतको जीतकर शुक्तिमती
- **Translation**: 

---

### Verse 3 (Bramha 0.703)
- **Original**: जन्म हुआ, जो संग्राममें धृष्ट और प्रतापी था। नगरीमें निवास किया। ज्यामघकी पत्नी शैब्या थी,
- **Translation**: 

---

### Verse 4 (Bramha 0.704)
- **Original**: धृष्टके आवन्त, दशाह तथा विषहर नामक तीन जो पतिब्रता होनके साथ ही बड़ी प्रबल थी।
- **Translation**: 

---

### Verse 5 (Bramha 0.705)
- **Original**: पुत्र हुए, जो बड़े धर्मात्मा और शूरवीर थे। यद्यपि राजाको कोई पुत्र नहीं था, तथापि उन्होंने
- **Translation**: 

---

### Verse 6 (Bramha 0.706)
- **Original**: दशाहके व्योमा और व्योमाके पुत्र जीमूत बतलाये
- **Translation**: 

---

### Verse 7 (Bramha 0.707)
- **Original**: * क्रोष्दु आदिके बंशका वर्णन तथा स्थमनन्‍्तकमणिकी कथा * क्5 जाते हैं। जीमूतके विकृति, विकृतिके भीमरथ,
- **Translation**: 

---

### Verse 8 (Bramha 0.708)
- **Original**: रूप धारण करके राजाको पतिरूपमें वरण किया। भीमरथके नवर्थ और नवरथके पुत्र दशरथ हुए।
- **Translation**: 

---

### Verse 9 (Bramha 0.709)
- **Original**: राजाने भी उसकी कामना की। तदनन्तर उन दशरसथके पुत्रका नाम शकुनि था। शकुनिसे करम्भ
- **Translation**: 

---

### Verse 10 (Bramha 0.710)
- **Original**: ठदारबुद्धि नरेशने उसमें एक तेजस्वी गर्भकी तथा करम्भसे देवरातका जन्म हुआ। देवरातके पुत्र
- **Translation**: 

---

### Verse 11 (Bramha 0.711)
- **Original**: स्थापना को। तत्पश्चात्‌ दसवें महीनेमें पर्णाशाने देवक्षत्र तथा देवक्षत्रके महायशस्वी वृद्धक्षत्र हुए। वे
- **Translation**: 

---

### Verse 12 (Bramha 0.712)
- **Original**: देवावृधके सर्वगुणसम्पन्न पुत्र बभ्रुको जन्म दिया। देवकुमारके समान कान्तिमानू थे। इनके सिवा
- **Translation**: 

---

### Verse 13 (Bramha 0.713)
- **Original**: इस वंशके विषयमें पुराणोंके ज्ञाता देवावृधके मधुरभाषी राजा मधुका भी जन्म हुआ, जो मधुबंशके
- **Translation**: 

---

### Verse 14 (Bramha 0.714)
- **Original**: गुणोंका बखान करते हुए निप्नाड्धित प्रसिद्ध प्रबर्तक थे। मधुके उनकी पत्नी वैदर्भीसे नरश्रेष्ठ
- **Translation**: 

---

### Verse 15 (Bramha 0.715)
- **Original**: गाथाका गान करते हैं। 'हम जैसे आगे देखते हैं, पुरुद्वान्‌की उत्पत्ति हुई। मधुकी दूसरी पत्नी इक्ष्वाकुलंशकी
- **Translation**: 

---

### Verse 16 (Bramha 0.716)
- **Original**: वैसे ही दूर और निकट भी देखते हैं। हमारी कन्या थी। उससे सर्वगुणसम्पन्न सत्त्वानू हुए, जो
- **Translation**: 

---

### Verse 17 (Bramha 0.717)
- **Original**: दृष्टिमें बभु सब मनुष्योंमें श्रेष्ठ हैं और देवावृध तो सात्त्वत कुलकी कीर्तिको बढ़ानेवाले थे।
- **Translation**: 

---

### Verse 18 (Bramha 0.718)
- **Original**: देवताओंके तुल्य हैं। बध्चु और देवावृधके सम्पर्कमें सत्त्वानूसे सत्त्वगुणसम्पन्ना कौसल्याने भजमान, , आकर एक हजार चौहत्तर मनुष्य अमृतत्वको प्राप्त देवावृध, अन्धक तथा वृष्णि नामक पुत्र उत्पन्न
- **Translation**: 

---

### Verse 19 (Bramha 0.719)
- **Original**: हो चुके हैं।' किये। इनके चार कुल यहाँ विस्तारपूर्वक बतलाये
- **Translation**: 

---

### Verse 20 (Bramha 0.720)
- **Original**: बधुका वंश बहुत बड़ा था। उसमें सब-के- गये हैं। भजमानके दो स्त्रियाँ थीं। एकका नाम था
- **Translation**: 

---

