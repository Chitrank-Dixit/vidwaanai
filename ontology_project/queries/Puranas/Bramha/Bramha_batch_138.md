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

### Verse 1 (Bramha 0.2741)
- **Original**: बलराम तथा सुभद्राका दर्शन करता है, वह सब और सात पीढ़ी नीचेके पुरुषोंका उद्धार करके
- **Translation**: 

---

### Verse 2 (Bramha 0.2742)
- **Original**: पापोंसे मुक्त हो विष्णुलोकमें जाता है। जो वैशाख- इच्छानुसार गतिवाले विमानके द्वारा विष्णुलोकमें ' कृष्णा तृतीयाकों चन्दन-चर्चित श्रीकृष्णका दर्शन जाता है। इस प्रकार पाँच तीर्थोंका सेवन करके
- **Translation**: 

---

### Verse 3 (Bramha 0.2743)
- **Original**: करता है, वह विष्णु-धाममें जाता है। ज्येष्ठा नक्षत्रसे एकादशीको उपवास करें। जो मनुष्य ज्येष्ठकी
- **Translation**: 

---

### Verse 4 (Bramha 0.2744)
- **Original**: युक्त ज्येष्टमासको पूर्णिमाके दिन जो श्रीपुरुषोत्तमका यूर्णिमाकों भगवान्‌ पुरुषोत्तमका दर्शन करता है,
- **Translation**: 

---

### Verse 5 (Bramha 0.2745)
- **Original**: दर्शन करता है, वह अपनी इक्कीस पीढ़ियोंका उद्धार वह पूर्वोक्त फलका भागी होकर परम धामको
- **Translation**: 

---

### Verse 6 (Bramha 0.2746)
- **Original**: करके श्रीविष्णुलोकमें जाता है। जाता है, जहाँसे पुनः उसका लौटना नहीं होता।। . जिस दिन राशि और नक्षत्रके योगसे महाज्येष्ट भुनियोंने घूछा--पितामह! आप माघ आदि
- **Translation**: 

---

### Verse 7 (Bramha 0.2747)
- **Original**: (ज्येष्ठकी पूर्णिमा) हो, उस दिन यल्पूर्वक महीनोंको छोड़कर ज्येष्ट मासकी इतनी प्रशंसा
- **Translation**: 

---

### Verse 8 (Bramha 0.2748)
- **Original**: श्रीपुरुषोत्तमतीर्थमें पहुँचना चाहिये। महाज्येष्टी- क्यों करते हैं? प्रभो! इसका कारण बतलाइये।
- **Translation**: 

---

### Verse 9 (Bramha 0.2749)
- **Original**: पर्वके दिन श्रीकृष्ण, बलराम तथा सुभद्राका दर्शन ब्रह्मजी बोले--मुनिवरो! सुनो। अन्य मासोंकी
- **Translation**: 

---

### Verse 10 (Bramha 0.2750)
- **Original**: करके मनुष्य बारह यात्राओंसे भी अधिक फलका अपेक्षा जो ज्येष्ट मासकी बारंबार प्रशंसा करता हूँ,
- **Translation**: 

---

### Verse 11 (Bramha 0.2751)
- **Original**: भागी होता है। प्रयाग, कुरुक्षेत्र, नैमिषारण्य, पुष्कर, उसका कारण संक्षेपसे बतलाता हूँ। पृथ्वीपर जो-
- **Translation**: 

---

### Verse 12 (Bramha 0.2752)
- **Original**: गया, हरिद्वार, कुशावर्त, गज्जा-सागर-संगम, महानदी, जो तीर्थ, नदियाँ, सरोवर, पुष्करिणी, तड़ाग, वापी,
- **Translation**: 

---

### Verse 13 (Bramha 0.2753)
- **Original**: वैतरणी तथा अन्य जितने तीर्थ हैं, अथवा अधिक कूप, हृद और समुद्र हैं, बे सब ज्ये्ठके शुक्लपक्षकी
- **Translation**: 

---

### Verse 14 (Bramha 0.2754)
- **Original**: कहनेकी क्या आवश्यकता, पृथ्वीतलके सब तीर्थ, दशमीसे लेकर पूर्णिमातक एक सप्ताह प्रत्यक्षरूपसे
- **Translation**: 

---

### Verse 15 (Bramha 0.2755)
- **Original**: सब मन्दिर, सब समुद्र, सब पर्वत, सब नदी और पुरुषोत्तमतीर्थमें जाकर रहते हैं। यह उनका सदाका
- **Translation**: 

---

### Verse 16 (Bramha 0.2756)
- **Original**: सब सरोवरोंमें ग्रहणके समय स्रान-दानसे जो फल नियम है। इसलिये वहाँ स्नान-दान, देवदर्शन आदि
- **Translation**: 

---

### Verse 17 (Bramha 0.2757)
- **Original**: होता है, बही महाज्येष्टीको श्रोकृष्णका दर्शन जो कुछ पुण्य कार्य उस समय किया जाता है, वह
- **Translation**: 

---

### Verse 18 (Bramha 0.2758)
- **Original**: करलेमात्रसे मनुष्य पा लेता है। अत: महास्येष्टीको अक्षय होता है। द्विजवरो ! ज्येष्ठ मासके शुक्लपक्षकी
- **Translation**: 

---

### Verse 19 (Bramha 0.2759)
- **Original**: सर्वथा प्रयल्॒ करके पुरुषोत्तमतीर्थकी यात्रा करनी दशमी तिथि दस पापोंकों हरती है, इसलिये उसे
- **Translation**: 

---

### Verse 20 (Bramha 0.2760)
- **Original**: चाहिये। सुभद्राके साथ श्रीकृष्ण और बलरामका दशहरा कहा गया है। उस दिन जो लोग अपनी
- **Translation**: 

---

