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

### Verse 1 (Vishnu Puran 0.9181)
- **Original**: भगवान्‌ बैकुण्ठ दिशज्ञाओंमें, मघुसूदन विदिज्ञाओं (कोर्णों)में, इृषोकेशा आकाझमें तथा पृथिवीको धारण करनेवाले श्रीशेषजी पृथिवीपर तेरी रक्षा ब्ँ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9182)
- **Original**: श्रीपराहस्जी बोल्ले--इस प्रकार स्वस्तिवाचन कर नन्‍्दगोपने बालक कृष्णको छकड़ेके नीचे एक ख़टोलेपर सुत्त दिया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9183)
- **Original**: मरी हुई पूतनाके महान्‌ कलेवरक्मा देस्ककर उन सभी गोपोक्त्रे अत्यन्त भय और मृताया: परम त्रासं विस्मयं च तदा ययुः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9184)
- **Original**: विस्मय हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9185)
- **Original**: _>--+>>मम. हज &---- इति श्रीविष्णुपुराणे पञमेंउशें पश्लपोउघ्यायः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9186)
- **Original**: मम हु कक छठा अध्याय जाना और वर्षा-वर्णन अपराशर उवान कदाचिच्छकटस्थाधइशयानो. मधुसूदन: । चिक्षेप चरणावूर्ध्व॑ स्तन्यार्थी प्रसरोद ह
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9187)
- **Original**: 1 तस्य पादप्रहारेण हाकर्ट परिवर्तितम्‌ । विध्वस्तकुम्मभाण्ड तद्विपरीत॑ पपात वैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9188)
- **Original**: 2 ततो हाहाकृत सर्बों गोपगोपीजनो ट्विंज । आजगामाथ ददृशे बालमुत्तानशायिनम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9189)
- **Original**: 3 गोपाः केनेति केनेद शक परिवर्तितम्‌। तत्रैव बालका: प्रोचु्बालिनानेन पातितम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9190)
- **Original**: 4 रुदता दृष्टमस्माभिः पादबिक्षेपपातितम्‌ । शकर्ट परिवृत्त वै नैतदन्यस्थ चेष्टितम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9191)
- **Original**: 5 ततः पुनरतीबासन्गोपा विस्मबचेतस: । नन्दगोषो5पि जग्राह बालमत्यन्तविस्मित:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9192)
- **Original**: 6 यशोदा झकटारूढभग्रभाण्डकपालिका: । जझकर् चार्चयामास दथधिपुष्पफलाक्षतैः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9193)
- **Original**: 7 गर्गक्ष गोकुले तत्र वसुदेवप्रचचोदित: । फ्रच्कक्ष एवं गोपानां संस्कारानकरोत्तयो:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9194)
- **Original**: 8 ज्येप्ठं च राममित्याह कृष्णं चैव तथावरम्‌। गर्णों मतिमतां श्रेष्ठो नाम कुर्बन्महामति:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9195)
- **Original**: 9 श्रोपराशरजी बोलले--एक दिन छकड़ेके नीचे सोये हुए मधुसूदनने दूधके लिये गेते-रोते ऊपरकों ल्प्रत मारी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9196)
- **Original**: उनकी ल्मत लगते ही बह छकड़ा लोट गया, उसमें रखे हुए कुम्भ और भाण्ड आदि फूट गये और यह उल्छटा जा पड़ा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9197)
- **Original**: हे ट्विज ! उस समय हाहाकार मच गया, समस्त गोप-गोपीगण वहाँ आ पहुँचे और उस बालक़को उतान सोये हुए देखा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9198)
- **Original**: तब गोपगण पूछने लगे कि 'इस छकड़ेकों किसने उछट दिया, किसने उत्प्ट दिया ?' तो बहाँगर खेलते हुए बालकोंने कहा---“'इस कृष्णने हो गियया है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9199)
- **Original**: हमने अपनी आँखोंसे देखा है कि रोते-रोते इसकी लात रूगनेले ही यह छकड़ा गिरकर उलट गया है। यह और किसीका काम नहीं है''
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9200)
- **Original**: यह सुनकर गोपगणके चित्तमें अत्यन्त विस्मय हुआ तथा नचगोपने अत्यक्त चक्तित होकर बराल्कको उठा लिया
- **Translation**: 

---

