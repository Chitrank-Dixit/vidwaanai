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

### Verse 1 (Bramha 0.4981)
- **Original**: है। मेरे यज्ञका मुख्य स्थापन यह दण्डकारण्य है। पुरुषसे प्रकट हुआ। इसी समय भगवान्‌को दैवी
- **Translation**: 

---

### Verse 2 (Bramha 0.4982)
- **Original**: जब यज्ञ पूरा हुआ, तब मैंने भक्तिपूर्वक भगवान्‌ वाणीने पुनः मुझसे कहा--' ब्रह्मन्‌! सब पूरा हो
- **Translation**: 

---

### Verse 3 (Bramha 0.4983)
- **Original**: विष्णुको प्रसन्न किया। बिन्‍्हें वेदमें विराद कहते गया। मनोबाडिछत सृष्टि उत्पन्न हुईं। इस समय
- **Translation**: 

---

### Verse 4 (Bramha 0.4984)
- **Original**: हैं, जिनसे मूर्तिमान्‌ जगत्‌की उत्पत्ति हुई है तथा जितने पात्र हैं, उन सबकी अग्रिमें आहुति कर
- **Translation**: 

---

### Verse 5 (Bramha 0.4985)
- **Original**: जिनसे मेरा जन्म हुआ है, उन देवदेवेश्वर दो। यूप, प्रणीता, कुश, ऋत्विक्‌ , यज्ञ, खुबा,
- **Translation**: 

---

### Verse 6 (Bramha 0.4986)
- **Original**: भगवान्‌ विष्णुकी आराधना करके मैंने उनका पुरुष और पाश-सबका विसर्जन कर दो।'
- **Translation**: 

---

### Verse 7 (Bramha 0.4987)
- **Original**: विसर्जन कर दिया। आकाशवाणीके इतना कहते ही मैंने क्रमशः
- **Translation**: 

---

### Verse 8 (Bramha 0.4988)
- **Original**: . नारद! मेरे देवयजनका स्थान चौबीस योजन है। गारईपत्य, दक्षिणागिन तथा आहवनीयाग्रिमें हवन
- **Translation**: 

---

### Verse 9 (Bramha 0.4989)
- **Original**: आज भी यहाँ तीन कुण्ड हैं, जो यज्ञेध्वरस्वरूप हैं। किया। प्रत्येक होममें विश्वकी उत्पत्तिक कारणभूत
- **Translation**: 

---

### Verse 10 (Bramha 0.4990)
- **Original**: तभीसे वह स्थान मेरे देवयजनके नामसे प्रसिद्ध पुरुषका ध्यान किया। लोककर्त्ता जगन्नाथ भगवान्‌
- **Translation**: 

---

### Verse 11 (Bramha 0.4991)
- **Original**: हुआ। वहाँ रहनेबाले जो कीड़े-मकोड़े आदि हैं, ये विष्णु शुक्लरूप धारण करके आहबनीयाग्रिमें
- **Translation**: 

---

### Verse 12 (Bramha 0.4992)
- **Original**: भी अन्तमें मोक्षके भागी होते हैं। दण्डकारण्य धर्म स्थित हुए, श्यामरूपसे दक्षिणाग्रिमें और पीतरूपसे
- **Translation**: 

---

### Verse 13 (Bramha 0.4993)
- **Original**: और मोक्षका बीज बताया जाता है। विशेषत: वह गा्ईपत्याग्रिमें स्थित हुए। उन सभी देशोंमें भगवान्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.4994)
- **Original**: प्रदेश, जिसे गौतमी गज्जाने स्पर्श किया है, अधिक विष्णुका नित्य निवास है। कोई ऐसा स्थान या पुण्यमय हो गया है। प्रणीता-संगम तथा कुशतर्पण- वस्तु नहीं है, जहाँ विश्वयोनि भगवान्‌ विष्णु न
- **Translation**: 

---

### Verse 15 (Bramha 0.4995)
- **Original**: तीर्थमें जो स्नान और दान आदि करते हैं, थे
- **Translation**: 

---

### Verse 16 (Bramha 0.4996)
- **Original**: 242 * संक्षिप्त ब्रह्मपुराण « परमपदको प्राप्त होते हैं। उनके वृत्तान्तका स्मरण,
- **Translation**: 

---

### Verse 17 (Bramha 0.4997)
- **Original**: है। चराचर जगत्‌में इसके समान दूसरा कोई भी तीर्थ पठन अथवा भक्तिपूर्वक श्रवण भी मनुष्योंकी समस्त
- **Translation**: 

---

### Verse 18 (Bramha 0.4998)
- **Original**: नहीं है। इसके स्मरणमाजसे ब्रह्महत्या आदि पापोंका कामनाओंकों पूर्ण करनेबाला और भोग एवं मोक्षको
- **Translation**: 

---

### Verse 19 (Bramha 0.4999)
- **Original**: नाश हो जाता है। नारद! यह तीर्थ इस पृथ्वीपर देनेवाला है। मुने! कुशतर्पंणतीर्थ काशीसे भी उत्तम
- **Translation**: 

---

### Verse 20 (Bramha 0.5000)
- **Original**: स्वर्गका द्वार बताया जाता है। ढ#-;जस्फेप्ये2+-ल> सारस्वत तथा चिच्चिकतीर्थका माहात्म्य श्रह्माजी कहते हैं--सारस्वत नामक तीर्थ
- **Translation**: 

---

