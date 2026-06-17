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

### Verse 1 (Bramha 0.4741)
- **Original**: पतिकी सेवामें सदा संलग्न रहती हूँ; तो भी तीनों पुत्र क्रमश: दत्त, सोम और दुर्वासाके पतिदेव मुझे कटु वचन सुनाते और व्यर्थ ही नामसे प्रसिद्ध हुए। अग्निसे अड्विराकी उत्पत्ति
- **Translation**: 

---

### Verse 2 (Bramha 0.4742)
- **Original**: रोषपूर्ण दृष्टिसे देखा करते हैं। सुरश्रेष्ठ आप मेरे हुई थी। अड्भारसे उत्पन्न होनेके कारण ही उन्हें ' पति-देवताकों समझा दें। अक्लिरा कहते हैं। महर्षि अत्रिने अम्लरासि ही
- **Translation**: 

---

### Verse 3 (Bramha 0.4743)
- **Original**: अप्नि बोले--कल्याणों! तुम्होरे पति अद्विरा अपनी तेजस्वी कन्या आत्रेयीकों ब्याह दिया।! ऋषि अज्ञारसे प्रकट हुए हैं। वे जिस प्रकार शान्त अक्लिरामें अग्निकी तीत्रताका प्रभाव था। अत: बे
- **Translation**: 

---

### Verse 4 (Bramha 0.4744)
- **Original**: हो सकें, वैसी नीति बर्तनी चाहिये। तुम्हारे पति आत्रेयीसे सदा परुष (कठोर) भाषण किया करते
- **Translation**: 

---

### Verse 5 (Bramha 0.4745)
- **Original**: अद्विरा जब अग्रिमें प्रवेश करें, तब तुम मेरी थे। आत्रियी भी सदा पतिको सेवामें संलग्र रहतो
- **Translation**: 

---

### Verse 6 (Bramha 0.4746)
- **Original**: आज्ञासे जलरूप होकर उन्हें बहा ले जाना।
- **Translation**: 

---

### Verse 7 (Bramha 0.4747)
- **Original**: 232 * संक्षिप्त ब्रह्मपुराण * >> ड€::7%ऋनबछ मे % ऋ#ऋमनममखखऊईखडइ >> ऋऋऋऋ ऋऋऋाननननन्न्न् न आत्रेयीने कहा--भगवन्‌! मैं उनको कठोर
- **Translation**: 

---

### Verse 8 (Bramha 0.4748)
- **Original**: वे दोनों शोभा पाने लगे। पतिको आप्लाबित यातें सह लूँगी, किंतु मेरे स्वामी अग्निमें प्रवेश न
- **Translation**: 

---

### Verse 9 (Bramha 0.4749)
- **Original**: करती हुई आत्रेयीने जलमय शरीर धारण किया करें। जो स्त्रियाँ अपने स्वामीसे प्रतिकूल चलती
- **Translation**: 

---

### Verse 10 (Bramha 0.4750)
- **Original**: था, अत: वह परुष्णी नदीके नामसे विख्यात हुई हैं, उनके जीवनसे क्या लाभ। मैं तो इतना ही
- **Translation**: 

---

### Verse 11 (Bramha 0.4751)
- **Original**: और गज्जामें जा मिली। उसमें स्नान करनेसे सौ चाहती थी कि वे शान्तिमय वचन बोलें। गोदानोंका पुण्य प्राप्त होता है। आज्लिरस नामवाले अग्रि बोले--जलमें, शरीरमें तथा स्थावर-
- **Translation**: 

---

### Verse 12 (Bramha 0.4752)
- **Original**: पुत्रने गड़्ा और परुष्णीके संगमपर बहुत-से यज्ञ जज्जमरूप जगतमें सर्वत्र मेरा निवास है। मैं तुम्हारे
- **Translation**: 

---

### Verse 13 (Bramha 0.4753)
- **Original**: किये। वहाँ स्नान-दान आदिसे जो पुण्य होता है, पतिका नित्य आश्रय हूँ, क्‍योंकि मैं हो उनका
- **Translation**: 

---

### Verse 14 (Bramha 0.4754)
- **Original**: उसका वर्णन नहीं हो सकता। जनक हूँ। जो मैं हूँ, वही वे भी हैं। यह जानकर
- **Translation**: 

---

### Verse 15 (Bramha 0.4755)
- **Original**: गड्जाके उत्तर-तटपर नारसिंह नामक विख्यात तुम्हें चिन्ता नहीं करनी चाहिये। एक बात और
- **Translation**: 

---

### Verse 16 (Bramha 0.4756)
- **Original**: तीर्थ है, जो सबकी रक्षा करनेवाला है। उसके है--जलको तो तुम माता समझो और अग्निको
- **Translation**: 

---

### Verse 17 (Bramha 0.4757)
- **Original**: प्रभावका वर्णन करता हूँ, सुनो। पूर्वकालमें श्वशुर। इस बातका अपनी बुद्धिसे भलीभाँति
- **Translation**: 

---

### Verse 18 (Bramha 0.4758)
- **Original**: हिरण्यकशिपु नामक दैत्य हुआ था, जो बलवानोमें निश्चय करके तुम विषाद न करो।
- **Translation**: 

---

### Verse 19 (Bramha 0.4759)
- **Original**: श्रेष्ट था। तपस्या और पराक्रमकी दृष्टिसे भी बह आत्रेयीने कह्ा-- भगवन्‌! आप जलको माता
- **Translation**: 

---

### Verse 20 (Bramha 0.4760)
- **Original**: बहुत बढ़ा हुआ था। देवता भी उसे परास्त नहीं कहते हैं और मैं आपके पुत्रकी पत्नी हूँ। जननी
- **Translation**: 

---

