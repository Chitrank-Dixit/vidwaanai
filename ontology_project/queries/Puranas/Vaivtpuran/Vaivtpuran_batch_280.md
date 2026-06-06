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

### Verse 1 (Vaivtpuran 13.11742)
- **Original**: विद्या, श्री, उत्तम कवित्व, पुत्र-पौत्र तथा यश गोषियोंके प्राणाधिदेव तथा श्रीराधाके प्राणाधिक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11743)
- **Original**: भी पाता है। प्रियतम हैं। वसुदेवके पुत्र, शान्तस्वरूप तथा भगवान्‌ भ्रीनारायण कहते हैं-- दैत्ययाजकी देबकौके दुःखका निवारण करनेवाले हैं। आपका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11744)
- **Original**: यह स्तुति सुनकर करुणानिधान श्रीकृष्णने मन- स्वरूप अयोनिज है। आप पृथ्वीका भार उतारनेके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11745)
- **Original**: ही-मन विचार किया कि 'अहो! ऐसे भक्तका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11746)
- **Original**: 720 * संक्षिप्त ब्रह्मवैयर्तपुराण * ऋक्कऋक्ऋककऋकऋ ऋक्कऋऋऋऋऋ्क्ऋ्ऋ्ऋ्क्ऋझऋ ऋऋ्ऋ्ऋ्ऋझऋ ऋऋऋ्ऋऋ्ऋऋ्ऋ%ऋ ऋ कक कक ऋक संहार मैं कैसे करूँ? ऐसा सोचकर भगवान्‌ने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11747)
- **Original**: उस महात्मा दानवका मस्तक पृथ्वीपर गिर पड़ा। स्वयं ही उसकी पूर्वजन्मकी स्मृति हर ली; उसके शरीरसे सैकड़ों सूर्योके समान कान्तिमान्‌ क्योंकि स्तुति करनेवालेका वध उचित नहीं है। जज, न उद्त्त दुर्बचन बोलनेवालेके ही वधका विधान है। तब कैम दानव वैष्णवी मायाके प्रभावसे पुनः अपने- आपको भूल गया। उसके कण्ठदेशमें दुर्वचनने स्थान जमा लिया। मुने! वह शीघ्र ही मरना
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11748)
- **Original**: री हे चाहता था, इसलिये दुर्देवसे ग्रस्त हो विवेक खो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11749)
- **Original**: ।.8 बैठा। क्रोध्भे उसके ओठ फड़कने लगे और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11750)
- **Original**: 6 वह दैत्य श्रीहरिसे इस प्रकार बोला। ! दैत्यने कहा--दुर्मते! तू निश्चय ही मरना 80 स्प्ज्नल 130 चाहता है। मनुष्यके बच्चे! मैं आज तुम्हें यमलोक £: 4#
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11751)
- **Original**: ले भेज दूँगा। तेज:पुझ्ल॒ उठा, जो श्रीहरिकी ओर देखकर इस प्रकार बहुत-से दुर्वचन कहकर उस
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11752)
- **Original**: उन्हींके चरणकमलोंमें लीन हो गया। अहो! उस गदहेने श्रीकृष्पपर आक्रमण कर दिया। भयानक
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11753)
- **Original**: दानवराजने परम मोक्ष प्राप्त कर लिया। उस समय युद्ध हुआ। अन्तमें श्रीहरिने प्रसन्नतापूर्वक हँसकर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11754)
- **Original**: आकाशमें खड़े हुए समस्त देवता और मुनि उस दानवराजकी प्रशंसा करते हुए कहा--'मेरे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11755)
- **Original**: अत्यन्त हर्षसे उत्फुल्ल हो बहाँ पारिजातके भक्त बलिके पुत्र! दानवेन्द्र ! तुम्हारा उत्तम जीवन
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11756)
- **Original**: फूलोंकी वर्षा करने लगे। स्वर्गमें दुन्दुभियाँ बज धन्य है। वत्स! तुम्हाता कल्याण हो। अब तुम
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11757)
- **Original**: उठीं। अप्सराएँ नाचने लगीं। गन्धर्व-समूह गीत मोक्ष प्राप्त करो। मेरा दर्शन कल्याणका बीज तथा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11758)
- **Original**: गाने लगे और मुनिलोग सानन्द स्तुति करने लगे। मोक्षका परम कारण है। तुम सबसे अधिक और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11759)
- **Original**: स्तुति करके हर्षसे विह्लल हुए समस्त देवता और सबसे उत्कृष्ट मनोहर स्थान प्राप्त करो।' मुनि चले गये। ' धेनुकासुर मारा गया'--यह देख यों कहकर श्रोकृष्णने अपने उत्तम चक्रका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11760)
- **Original**: ग्वाल-बाल वहाँ आ गये। बलवानोंमें श्रेष्ठ स्मरण किया, जो अपनी दीप्तिसे करोड़ों सूर्योके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11761)
- **Original**: बलरामने पुरुषोत्तमका स्तवन किया। समस्त समान उद्दीप्त होता है। स्मरण करते ही वह आ
- **Translation**: 

---

