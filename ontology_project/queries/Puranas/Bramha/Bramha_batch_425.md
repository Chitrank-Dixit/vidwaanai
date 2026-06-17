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

### Verse 1 (Bramha 0.8481)
- **Original**: (235। 22-23)
- **Translation**: 

---

### Verse 2 (Bramha 0.8482)
- **Original**: *योग और सांख्यका वर्णन « 07 आकाशमें चिड़ियोंके और जलमें मछलियोंके । विद्वानेने उसे 'हंस' कहा है। 'हंस' नामसे जिस चलनेके चिट्ठ दिखायो नहीं पड़ते, उसी प्रकार
- **Translation**: 

---

### Verse 3 (Bramha 0.8483)
- **Original**: अविनाशी जीवात्माका प्रतिपादन किया गया है, वह ज्ञानियोंकी मतिका भी किसीकों पता नहीं चलता।
- **Translation**: 

---

### Verse 4 (Bramha 0.8484)
- **Original**: कूटस्थ अक्षर ही है। इस प्रकार जो विद्वान्‌ू उस काल सम्पूर्ण प्राणियोंको पकाता (नष्ट करता)
- **Translation**: 

---

### Verse 5 (Bramha 0.8485)
- **Original**: अक्षर आत्माको जान लेता है, वह जन्म-मृत्युके है; किंवु जहाँ काल भी पकाया जाता है--जो
- **Translation**: 

---

### Verse 6 (Bramha 0.8486)
- **Original**: बन्धनसे छुटकारा पा जाता है। कालका भी काल है, उस आत्माकों कोई नहीं
- **Translation**: 

---

### Verse 7 (Bramha 0.8487)
- **Original**: ब्राह्मणो! इस प्रकार तुम्हारे पूछनेपर मैंने जानता। फरब्रह्म परमात्मा न ऊपर है न नीचे है, न
- **Translation**: 

---

### Verse 8 (Bramha 0.8488)
- **Original**: ज्ञानयुक्त सांख्यका यथावत्‌ वर्णन किया। अब इधर-उधर है और न बीचमें हो; कोई किसी अंशमें
- **Translation**: 

---

### Verse 9 (Bramha 0.8489)
- **Original**: योगकी बातें बताऊँगा, सुनो। इन्द्रिय, मन और उसको ग्रहण कर सकता है। सम्पूर्ण लोक उसके
- **Translation**: 

---

### Verse 10 (Bramha 0.8490)
- **Original**: बुद्धिकी वृत्तियोंको सब ओरसे रोककर व्यापक भीतर ही स्थित हैं। उसके बाहर कुछ भी नहीं है।
- **Translation**: 

---

### Verse 11 (Bramha 0.8491)
- **Original**: आत्माके साथ उनकी एकता स्थापित करना ही यध्वपि कोई धनुषसे छूटे हुए बाण अथवा मनके
- **Translation**: 

---

### Verse 12 (Bramha 0.8492)
- **Original**: योगशास्त्रके मतमें उत्तम ज्ञान है। योगी पुरुषको समान वेगसे निरन्तर आगेकी ओर दौड़ता रहे तो
- **Translation**: 

---

### Verse 13 (Bramha 0.8493)
- **Original**: शम-दमसे सम्पन्न होना चाहिये। बह अध्यात्मशास्त्रका भी कभी उस परमेश्वरका अन्त नहीं पा सकता।
- **Translation**: 

---

### Verse 14 (Bramha 0.8494)
- **Original**: अनुशीलन करे, आत्मामें ही अनुराग रखे, शास्त्रोंका उससे अधिक सूक्ष्म तथा उससे बढ़कर स्थूल
- **Translation**: 

---

### Verse 15 (Bramha 0.8495)
- **Original**: तत््व जाने और निष्कामभावसे पवित्र कर्मोंका दूसरी कोई वस्तु नहीं है। उसके सब ओर हाथ-
- **Translation**: 

---

### Verse 16 (Bramha 0.8496)
- **Original**: अनुष्ठान करे। इस प्रकार साधनसम्पन्न होकर पैर हैं, सब ओर नेत्र हैं तथा सब ओर सिर, मुख
- **Translation**: 

---

### Verse 17 (Bramha 0.8497)
- **Original**: योगोक्त उत्तम ज्ञानको प्राप्त करें। काम, क्रोध, और कान हैं। वह संसारमें सबको व्याप्त करके
- **Translation**: 

---

### Verse 18 (Bramha 0.8498)
- **Original**: लोभ, भय और स्वपत--ये पाँच योगके दोष हैं; स्थित है। छोटे-से-छोटा और बड़े-से-बड़ा भी
- **Translation**: 

---

### Verse 19 (Bramha 0.8499)
- **Original**: इन्हें विद्वान्‌ पुरुष जानते हैं। इन सभी दोषोंका वही है। यद्यपि वह सब प्राणियोंके भीतर निश्चय
- **Translation**: 

---

### Verse 20 (Bramha 0.8500)
- **Original**: उच्छेद करके अपनेकों योगका अधिकारी बनाये। ही स्थित रहता है तो भी वह किसीको दिखायी
- **Translation**: 

---

