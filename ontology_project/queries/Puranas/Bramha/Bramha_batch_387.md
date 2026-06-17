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

### Verse 1 (Bramha 0.7721)
- **Original**: करना चाहिये। जलके भीतरकी, घरकी, बाँबीकी, समय रात्रिमें भी स्नान करना बहुत उत्तम है।
- **Translation**: 

---

### Verse 2 (Bramha 0.7722)
- **Original**: चूहेके बिलकोी और शौचसे बची हुई-ये पाँच इसके सिवा अन्य समयमें दिनमें ही स्रानका
- **Translation**: 

---

### Verse 3 (Bramha 0.7723)
- **Original**: प्रकारकी मिट्टियाँ त्याग देने योग्य हैं। हाथ-पैर विधान है। वस्त्रके छोरसे अथवा वस्त्र हाथमें
- **Translation**: 

---

### Verse 4 (Bramha 0.7724)
- **Original**: धोकर एकाग्रचित्तसे मार्जन करके घुटनोंको समेटकर लेकर उससे शरीरकों न मले। बालों और
- **Translation**: 

---

### Verse 5 (Bramha 0.7725)
- **Original**: तौन या चार बार आचमन करे; फिर दो बार ओठ बस्त्रोंको न झटकारे। विद्वान्‌ पुरुष स्रान किये
- **Translation**: 

---

### Verse 6 (Bramha 0.7726)
- **Original**: पॉछकर आँख, कान, मुख,नासिका तथा मस्तकका बिना कभी चन्दन न लगाये। एक-दूसरेके वस्त्र ' स्पर्श करे। इस प्रकार जलसे भलीभौँति आचमन और आभूषणोंको अदल-बदलकर न पहने। करके पवित्र हो देवपूजन तथा श्राद्ध आदिकी क्रिया जिसमें कोर न हो और जो बहुत फट गया हो,
- **Translation**: 

---

### Verse 7 (Bramha 0.7727)
- **Original**: करनी चाहिये। छींकने, चाटने, यमन करने, थूकते * घरदारा न गन्तव्या: पुरुषेण विपक्षिता। इहापूर्तायुषां हन्त्री परदारगतिर्नृणाम्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.7728)
- **Original**: न होदुशमनायुष्य॑ लोके किंचन विद्यते। यादृ्श पुरुषस्येह. परदाराभिमर्शनम्‌
- **Translation**: 

---

### Verse 9 (Bramha 0.7729)
- **Original**: (121। 60-62)
- **Translation**: 

---

### Verse 10 (Bramha 0.7730)
- **Original**: + गृहस्थोचित सदाचार तथा कर्त॑व्याकर्तव्यका वर्णन « 371 तथा अस्पृश्यका स्पर्श करनेपर आचमन, सूर्यका
- **Translation**: 

---

### Verse 11 (Bramha 0.7731)
- **Original**: परिहास न करे। सदा माड्ूलिक बेष धारण किये दर्शन अथवा दाहिने कानका स्पर्श करना चाहिये।
- **Translation**: 

---

### Verse 12 (Bramha 0.7732)
- **Original**: रहे। कभी भी अमग्नलमय वेष न धारण करे। इनमें पहलेके अभावमें दूसरा ठपाय करना चाहिये।
- **Translation**: 

---

### Verse 13 (Bramha 0.7733)
- **Original**: स्वच्छ वस्त्र पहने और श्वेत पुष्पोंकी माला धारण फहले उपायके सम्भव होनेपर उपायान्तरका अवलम्बन
- **Translation**: 

---

### Verse 14 (Bramha 0.7734)
- **Original**: करे। उद्धत, उन्मत्त, मूढ़, अविनीत, शीलहीन, अभीष्ट नहीं। अवस्था और जातिसे दूषित, अधिक अपव्ययी, दाँत न कटकटाये। अपने शरीरपर ताल न दे।
- **Translation**: 

---

### Verse 15 (Bramha 0.7735)
- **Original**: बरी, कार्यमें असमर्थ, निन्दित, धूतोंका संग करनेवाले, दोनों संध्याऑंके समय अध्ययन, भोजन और
- **Translation**: 

---

### Verse 16 (Bramha 0.7736)
- **Original**: निर्धन, बिवाद करनेवाले तथा अन्य अधम पुरुषोंके शयनका त्याग करे। सन्ध्याकालमें मैथुन और
- **Translation**: 

---

### Verse 17 (Bramha 0.7737)
- **Original**: साथ कभी मित्रता न करे। सुदृदद, यज्ञदीक्षित, राजा, रास्ता चलना भी मना है। पूर्वाह््में देवताओंका,
- **Translation**: 

---

### Verse 18 (Bramha 0.7738)
- **Original**: स्नातक तथा श्वशुर-इनके साथ मैत्रीका भाव रखे मध्याहमें मनुष्योंका तथा अपराष्ट्रकालमें पितरोंका
- **Translation**: 

---

### Verse 19 (Bramha 0.7739)
- **Original**: और जब ये घरपर पधारें तो उठकर खड़ा हो जाय; भक्तिपूर्वक्क पूजत करना चाहिये। देवकार्य या
- **Translation**: 

---

### Verse 20 (Bramha 0.7740)
- **Original**: साथ ही अपने वैभवके अनुसार इनका पूजन करे। पितृकार्यमें सिरसे स्नान करके प्रवृत्त होना उचित है।
- **Translation**: 

---

