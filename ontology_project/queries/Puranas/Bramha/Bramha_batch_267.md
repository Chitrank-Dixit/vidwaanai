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

### Verse 1 (Bramha 0.5321)
- **Original**: फल देती हैं। भाव भी तीन प्रकारका जानना धाराओंमें विभक्त किया। सबसे दक्षिणकी धारा
- **Translation**: 

---

### Verse 2 (Bramha 0.5322)
- **Original**: चाहिये-सात्त्विक, राजल और तामस। जिस वासिष्ठी कहलायी। उससे उत्तर वैश्वामित्री, उससे
- **Translation**: 

---

### Verse 3 (Bramha 0.5323)
- **Original**: भावनाके अनुरूप कर्म होगा, बैसा ही फल उत्तर वामदेवी, बीचकी धारा गौतमी, उससे उत्तर
- **Translation**: 

---

### Verse 4 (Bramha 0.5324)
- **Original**: मिलेगा। अत: फलकी प्राप्ति कर्मके अनुसार और भारद्वाजी, उससे उत्तर आत्रेयी और अन्तिम धारा
- **Translation**: 

---

### Verse 5 (Bramha 0.5325)
- **Original**: भावनाके अनुरूप भी होती है; इसलिये कर्मोंकी जामदग्नी है। उन सब ऋषियोंने मिलकर वहाँ
- **Translation**: 

---

### Verse 6 (Bramha 0.5326)
- **Original**: स्थिति विचित्र है, यों समझकर विद्वान्‌ पुरुषको बहुत बड़े सत्रका अनुष्ठान किया। इसी बौचमें
- **Translation**: 

---

### Verse 7 (Bramha 0.5327)
- **Original**: अपनी इच्छाके अनुकूल भाव भी बनाना चाहिये। देवताओंका प्रबल शत्रु विश्वकप वहाँ आया और
- **Translation**: 

---

### Verse 8 (Bramha 0.5328)
- **Original**: फिर उसके अनुरूप कर्म भी करना चाहिये। फल ब्रह्मचर्य तथा तपस्याके द्वारा उन ऋषियोंको प्रसन्न
- **Translation**: 

---

### Verse 9 (Bramha 0.5329)
- **Original**: देनेवाला भी जब फल चाहनेबालोंको फल देनेमें करके विनयपूर्वक पूछा--“मुनिवरो! यज्ञ अथवा
- **Translation**: 

---

### Verse 10 (Bramha 0.5330)
- **Original**: प्रवृत्त होता है, तब उसके कर्म और भावनाके तपस्या--जिस उपायसे भी मुझे बलवान पत्र प्रात्त
- **Translation**: 

---

### Verse 11 (Bramha 0.5331)
- **Original**: अनुसार ही फल देता है। कर्म धर्म, अर्थ, काम हो, जिसे देवता भी परास्त न कर सकें, वह
- **Translation**: 

---

### Verse 12 (Bramha 0.5332)
- **Original**: और मोक्ष-चारों पुरुषाथोंका कारण है। यदि उपाय बतलाइये।' निष्कामभावसे कर्म हो तो बह मुक्तिदायक होता तब परम बुद्धिमान्‌ विश्वामित्रने कहा--' तात!
- **Translation**: 

---

### Verse 13 (Bramha 0.5333)
- **Original**: है और सकामभावसे होनपर वही बन्धनका कर्मसे नाना प्रकारके फल प्राप्त होते हैं। तीन
- **Translation**: 

---

### Verse 14 (Bramha 0.5334)
- **Original**: कारण बन जाता है। अपने भावके अनुसार ही कारणोंमें कर्म ही पहला कारण हैं। दूसरा कारण
- **Translation**: 

---

### Verse 15 (Bramha 0.5335)
- **Original**: कर्म बनता है तथा वही इस लोक और परलोकमें कर्ता है तथा तीसरे कारणके अन्तर्गत उपादान
- **Translation**: 

---

### Verse 16 (Bramha 0.5336)
- **Original**: भाँति-भाँतिके फल देता है। भावके अनुकूल कर्म और बीज आदि अन्य उपकरण हैं। उपादान और , होता और तदनुसार भोग मिलता है; अतः भाव बीजको विद्वानोंने कर्म नहीं माना है। जहाँ बहुत-
- **Translation**: 

---

### Verse 17 (Bramha 0.5337)
- **Original**: सबसे बढ़कर है। तुम भी भावके अनुसार कर्म से कारण उपस्थित हों, बहाँ कर्म ही प्रधान
- **Translation**: 

---

### Verse 18 (Bramha 0.5338)
- **Original**: करो। फिर जो चाहोगे, प्राप्त कर लोगे।'
- **Translation**: 

---

### Verse 19 (Bramha 0.5339)
- **Original**: स्ध्द * संक्षिप्त अहापुराण « बुद्धिमानू विश्वामित्र मुनिका कथन सुनकर
- **Translation**: 

---

### Verse 20 (Bramha 0.5340)
- **Original**: भी भगवान्‌ शिवके धाममें जाता है। जो वेदान्तद्वारा विश्वरूपने तामस भावका आश्रय ले दीर्घकालतक
- **Translation**: 

---

