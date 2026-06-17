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

### Verse 1 (Vishnu Puran 0.5981)
- **Original**: नम्न कौन है 7 और किस प्रकारके आचरणवाला पुरुष नप्न-संज्ञा प्राप्त करता है? हे धर्मात्माओमें श्रेष्ठ ! मैं आपके द्वारा नमग्रके स्वरूपका यथावत्‌ वर्णन सुनना चाहता हैं; क्योंकि आपको ब्य्रेई भी आत अखिदित नहीं है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5982)
- **Original**: श्रीपराशरजी बोले--हे द्विज ! ऋकू, साम और यजुः यह बेदत्रयी नर्णॉका आवरणस्वरूप है। जो पुरुष मोहसे इसका त्याग कर देता है वह पापी “नप्र' कहलाता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5983)
- **Original**: हे त्रहमन्‌ ! समस्त वर्णोंका संवरण (ढंकनेवाल्का बस्तर) वेदत्रयी ही है; इसलिये उसका त्याग कर देनेपर पुरुष “नप्न' हो जाता है, इसमें कोई सन्देह नहीं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5984)
- **Original**: हमारे पितामह धर्मज्ञ वसिष्ठजीने इस विषयमें महात्पा भोष्णजोसे जो कुछ कहा था बह श्रवण करो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5985)
- **Original**: है मैत्रेय ! तुमने जो मुझसे नम्रक्के लिषयमें पूछा है इस सम्बन्धमें भीष्मके प्रति वर्णन करते समय मैंने भी महात्मा ससिष्ठजीका कथन सुना था
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5986)
- **Original**: पूर्वकालमें किसी समय सौ दिव्यवर्षतक देवता और असुरेंक्प परस्पर युद्ध हुआ । उसमें ह्वाद प्रभ॒ति टैत्योंद्वारा देवगण पराजित हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5987)
- **Original**: अतः देवगणने क्षीरसागरके उत्तरीय लटपर जाकर तपस्या की और भगबान्‌ विष्णुकी आराघनाके लिये उस समय इस स्तवका गान किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5988)
- **Original**: 216 श्रीविष्णुपुराण [ आ* 17 देखा ऊचु: आराधनाय लोकानां विष्णोरीक्षस्थ यो गिरम्‌। बक्ष्यामो भगवानाशस्तया बिष्णुः प्रसीदतु
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5989)
- **Original**: 11 यतो भूतान्यझेषाणि प्रसृतानि महात्मन: । यस्मिश्व लयमेष्यन्ति कस्त॑ स्तोतुमिहेश्वर:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5990)
- **Original**: 12 तथाप्यरातिविध्वंसध्वस्तवीर्या भयार्थिन: । त्वां स्तोष्यापस्तवोक्तीनां याथार्थ्य नैब गोचरे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5991)
- **Original**: 13 त्वमुर्वी सलिलें वहिर्वावुराकाशझमेव च। समस्तमन्तःकरणं प्रधान॑ तत्पर: पुमान्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5992)
- **Original**: 14 अकसर सरकार ।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5993)
- **Original**: 15 तत्रेश तब यत्पूर्व त्वन्नाभिकमलोद्धवम्‌। रूप विश्वोपकाराय तस्मै ब्रह्मात्मने नमः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5994)
- **Original**: 186 शक्रार्करुद्रवस्वश्चिरुत्सोपादिभेदकत्‌ू..। वयपेक॑ स्वरूप ते तस्मै देवात्मने नमः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5995)
- **Original**: 17 दम्भप्रायमसम्भोधि तितिक्षादमवर्जितम्‌ । यत्रूप॑ तब गोविन्द तस्मै दैत्यात्मने नमः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5996)
- **Original**: 18 नातिज्ञानवह्न यरिमिन्नाहमः स्तिमिततेजसि । शब्दादित्लोभि यत्तस्मै तुभ्य॑ यक्षात्मने नमः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5997)
- **Original**: 19 क्रौर्यमायामयं घोर॑ यश्च रूप॑ तवासितम्‌। निशाचरात्मने तस्मै नमस्ते पुरुषोत्तम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5998)
- **Original**: 20 स्वर्गस्थधर्मिसद्धरमफलोपकरणं तब । धर्माख्य॑ं च तथा रूप नमस्तस्मै जनारदन
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5999)
- **Original**: 269 हर्षप्रायमसंसर्गि गतिमदमनादिषु । सिद्धाख्यं तव यद्गुपं तस्मे सिद्धात्मने नमः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6000)
- **Original**: 22 अतितिक्षायन. क्रूरमुपभोगसह. हरे । ब्विजिड्ढं तत्र यद्रूप तस्मैं नागात्मने नमः
- **Translation**: 

---

