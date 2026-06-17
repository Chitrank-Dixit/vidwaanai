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

### Verse 1 (Bramha 0.2801)
- **Original**: हुए विधिवत्‌ स्नान करे। ऋषियोंने स्रान-कर्ममें सब प्रकारसे प्रयत्त करके गुण्डिचा-मण्डपमें
- **Translation**: 

---

### Verse 2 (Bramha 0.2802)
- **Original**: जिसके लिये जैसी विधि बतलायी है, उसको समस्त अभिलषित बस्तुओंकों देनेवाले भगवान्‌
- **Translation**: 

---

### Verse 3 (Bramha 0.2803)
- **Original**: उसी विधिसे स्नान करना चाहिये। स्नानके पश्चात्‌ पुरुषोत्तमका दर्शन करना चाहिये। वहाँ पुरुषोतमका
- **Translation**: 

---

### Verse 4 (Bramha 0.2804)
- **Original**: नाम, गोत्र और विधिका ज्ञाता पुरुष शास्त्रो दर्शन करके स्त्री या पुरुष जिन-जिन भोगोंको
- **Translation**: 

---

### Verse 5 (Bramha 0.2805)
- **Original**: विधिसे देवताओं, ऋषियों, पितरों तथा अन्य चाहें, उन्हें प्राप्त कर सकते हैं। जीवॉका तर्पण करे। फिर जलसे निकलकर दो मुनियोने पूछा--भगवन्‌! गुण्डिचाकी एक-
- **Translation**: 

---

### Verse 6 (Bramha 0.2806)
- **Original**: स्वच्छ वस्त्र पहने और विधिपूर्वक आचमन एक यात्राका पृथक्‌-पृथक्‌ क्या फल है? उसे
- **Translation**: 

---

### Verse 7 (Bramha 0.2807)
- **Original**: करके एक सौ आठ बार गायत्रीका मानसिक जप करनेसे नर या नारीकों कौन-सा फल मिलता है?
- **Translation**: 

---

### Verse 8 (Bramha 0.2808)
- **Original**: करे। गायत्री सब बेदोंकी माता, सम्पूर्ण पापोंको ब्रह्माजी बोले--श्राह्मणो! सुनो। मैं प्रत्येक
- **Translation**: 

---

### Verse 9 (Bramha 0.2809)
- **Original**: दूर करनेवाली तथा परम पवित्र है। इसके सिवा यात्राका फल बताता हूँ। गुण्डिचामें प्रबोधिनी
- **Translation**: 

---

### Verse 10 (Bramha 0.2810)
- **Original**: अन्यान्य सूर्यसम्बन्धी मन्त्रोंका भी श्रद्धापूर्वक जप एकादशौके दिन, फाल्गुनकी पूर्णिमाको तथा
- **Translation**: 

---

### Verse 11 (Bramha 0.2811)
- **Original**: करना चाहिये। तत्पश्चात्‌ तीन बार परिक्रमा करके विषुवयोगमें विधिपूर्वक यात्रा करके श्रीकृष्ण,
- **Translation**: 

---

### Verse 12 (Bramha 0.2812)
- **Original**: सूर्यदेवको प्रणाम करे। ब्राह्मण, क्षत्रिय और वैश्य--इन बलराम और सुभद्राका दर्शन करनेसे मनुष्य
- **Translation**: 

---

### Verse 13 (Bramha 0.2813)
- **Original**: तीन वर्णोका स्नान और जप वैदिक विधिके अनुसार यैकुण्ठ-धाममें जाता है। क्षेत्रोमें श्रेष्ठ पुरुषोत्तमतीर्थ
- **Translation**: 

---

### Verse 14 (Bramha 0.2814)
- **Original**: बताया गया है; किंतु स्त्री और शूद्रोंके स्नान और बड़ा ही पवित्र, रमणीय, मनुष्योंकों भोग और
- **Translation**: 

---

### Verse 15 (Bramha 0.2815)
- **Original**: जपमें वैदिक विधिका निषेध है। मोक्षका दाता तथा सब जीवॉको सुख पहुँचानेवाला
- **Translation**: 

---

### Verse 16 (Bramha 0.2816)
- **Original**: इसके बाद मौन होकर घरमें जाय और हाथ- है। जो जितेन्द्रिय स्त्री या पुरुष ज्येप्टमासमें वहाँ ' पैर धोकर विधिबत्‌ आचमन करके श्रीपुरुषोत्तमकी शास्त्रोक्त विधिके अनुसार बारह यात्राएँ करके
- **Translation**: 

---

### Verse 17 (Bramha 0.2817)
- **Original**: पूजा करे। पहले भगवान्‌कों घीसे स्नान कराये। एकाग्रचित्तसे उनको प्रतिष्ठा करता है और उस
- **Translation**: 

---

### Verse 18 (Bramha 0.2818)
- **Original**: फिर दूधसे; उसके बाद मधु, गन्‍्ध और जलसे; समय धन खर्च करनेमें कृपणता नहीं करता, वह
- **Translation**: 

---

### Verse 19 (Bramha 0.2819)
- **Original**: फिर तीर्थक चन्दन और जलसे स््रान कराये। भाँति-भाँतिक भोगोंका उपभोग करके अन्तमें
- **Translation**: 

---

### Verse 20 (Bramha 0.2820)
- **Original**: तदनन्तर भक्तिपूर्वक दो उत्तम वस्त्र पहनाये; फिर मोक्ष-पदको प्राप्त होता है। चन्दन, अगर, कपूर और केसर भगवान्‌के अश्ञॉमें मुनियोने कहा--देव! जगत्पते! हम आपके
- **Translation**: 

---

