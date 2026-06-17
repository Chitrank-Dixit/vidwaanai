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

### Verse 1 (Vishnu Puran 0.12161)
- **Original**: 29 एतद्ट: कथितं विप्रा यत्रिमित्तमिहागता: । तत्पृच्छत यथाकामम सर्व वक्ष्यामि व: स्फुटम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12162)
- **Original**: 30 ऋषयस्ते तत: प्रोचुर्यत्पष्टव्य॑ महामुने । अस्मिन्नेव च तत्‌ प्रश्ने यथावत्कथितं त्वया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12163)
- **Original**: 31 औीपरादार उवाच ततः प्रहस्य तानाह कृष्णद्वैपायनों मुनिः । विस्मयोत्फुल्लनयनांस्तापसांस्तानुपागतान्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12164)
- **Original**: 32 मरयैष भवतां ग्रश्नो ज्ञातो दिव्येन चक्षुषा । ततो हि व: प्रसज़ेन साधु साध्विति भाषितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12165)
- **Original**: 33 स्वल्पेन हि प्रयत्रेन धर्मस्सिद्धयति वै कलो । नौरात्मगुणाम्भोभि: क्षालताखिलकिल्बिषै:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12166)
- **Original**: 34 धर्मसम्पादने क्लेझो द्विजातीनां कृतादिषु
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12167)
- **Original**: 36 भवद्धिर्यद्भिप्रेते तदेतत्कथित॑ मया । अपूष्टेनापि धर्मज्ञा: किमन्यत्क्रियतां द्विजा:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12168)
- **Original**: 37 घष्ठ अंश ल्तेकोंको प्राप्त करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12169)
- **Original**: किंतु जिसे केवल [ मन्‍तहीन ] पाक-यज्ञका ही अधिकार है वह शूद्र द्विजोंकी सेवा करनेसे ही सद्रति प्राप्त कर लेता है, इसलिये यह अन्य जातियोंकी अपेक्षा धनन्‍्यतर है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12170)
- **Original**: हे मुनिशार्दूलो ! शूद्रको भक्ष्याभक्ष्य अथवा पेयापेयका कोई नियम नहीं है, इसलिये मैंने उसे साधु कहा है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12171)
- **Original**: [ अब स्््रियॉंकों किसलिये श्रेष्ठ कहा, यह बतलाते हैं-- ] पुरुषोंको अपने धर्मानुकूल प्राप्त किये हुए धनसे ही सर्वदा सुपात्रकों दान और विधिपूर्वक यज्ञ करना चाहिये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12172)
- **Original**: हे द्विजोत्मगण ! इस द्रब्यके उपार्जन तथा रक्षणमें महान्‌ क्वेश होता है और डसको अनुचित कार्यमे लूगानेसे भी मनुष्योव्त्रे जो कष्ट भोगना पड़ता है वह माल्ठूम ही है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12173)
- **Original**: इस प्रकार हे ट्रिजसत्तमो ! पुरुषणण इन तथा ऐसे ही अन्य कष्टसाध्य उपायोंसे क्रमञ्ञ: प्राजापत्य आदि शुभ लोकोंको प्राप्त करते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12174)
- **Original**: किंतु र्बियाँ तो तन-मन-वचनसे पतिकी सेवा करनेसे ही उनकी हितकारिणी होकर पत्तिके समान शुभ लोकोंफ्प्रे अनायास डो प्राप्त कर लेती हैं जो कि पुरुषोंको अत्यन्त परिश्रमसे मिलते हैं। इसीलिये मैंने तीसरी यार यह कहा था कि “त्त्रियाँ साधु हैं'
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12175)
- **Original**: “हे विप्रगण ! मैंने आपस्लेगोंसे यह [ अपने साथुवादका रहस्य ) कह दिया, अब आप जिसलिये पधारे हैं बह इच्छानुसार पूछिये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12176)
- **Original**: मैं आपसे सब बातें स्पष्ट करके कह दूँगा”
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12177)
- **Original**: तब ऋषियोंने कहा--“'हे महासुने ! हमें जो कुछ पूछना था उसका यथावत्‌ उत्तर आपने इसी प्रश्ममें दे दिया है। [ इसल्प्ये अब हमें और कुछ पूछना नहीं है ]
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12178)
- **Original**: श्रीपराश्रजी बोले--तब मुनिवर कृष्णद्रैपायनने विस्मयसे खिले हुए नेत्रोंवाले उन समागत तपस्कियोंसे हँसकर कहा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12179)
- **Original**: मैं दिव्य दृष्टिसे आपके इस प्रश्नको जान गया था इसीलिये मैंने आपल्मेगोंके प्रसंगसे हो “साधु-साधु' कहा था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12180)
- **Original**: जिन पुरुषोनि गुणरूप जलसे अपने समस्त दोष धो डाले हैं उनके थोड़े-से प्रचल्लसे ही कलियुगमें धर्म सिद्ध हो जाता है 34
- **Translation**: 

---

