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

### Verse 1 (Vishnu Puran 0.6101)
- **Original**: 22 अन्यानप्यन्यपाषण्डप्रकारैर्यहुभि्द्धिज..। दैतेयामोहयामास मायामोहो5तिमोहकृत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6102)
- **Original**: 23 स्वल्पेनेव हि कालेन मायामोहेन तेउसुराः । मोहितास्तत्यजुस्सवाँ त्रयीमार्गाश्नितां कथाम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6103)
- **Original**: 24 केचिद्विनिन्दां वेदानां देवानामपरे द्विज। यज्ञकर्मकलापस्य तथान्ये च द्विजन्मनाम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6104)
- **Original**: 25 वैतब्युक्तिसहं वाक्य हिंसा धर्माय चेष्यते। हर्वीष्यनलदाःधानि फल्ल्रयेत्यर्भकोदितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6105)
- **Original**: 26 यज्ैरनेकैर्देबत्वमवाप्येद्रेण भुज्यते । शाम्यादि यदि चेत्काएं तदूर पत्रभुक्पतुः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6106)
- **Original**: 27 निहतस्थ पश्ोर्यज्ञे स्वर्गप्राप्तियदीष्यते । स्वपिता यज़मानेन किन्नु तस्मान्न हन्यते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6107)
- **Original**: 28 तृष्यते जायते पुंसो धुक्तमन्येन चेत्ततः । कुर्याच्छारध भ्रमायान्न॑ न बहेयुः प्रवासिनः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6108)
- **Original**: 29 जनश्रद्धेयमित्येतद्वगम्य॒ ततोउञ्र॒ व: । उपेक्षा श्रेयसे वाक्य रोचतां यन्मरयेरितम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6109)
- **Original**: 30 न झ्याप्ततादा नभसो निपतन्ति महासुरा:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6110)
- **Original**: युक्तिमहचन ग्राह्म॑ मयान्यैश्ञ भवद्वियै:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6111)
- **Original**: 39 श्रीविष्णुपुराण [ अ* 18 यह सम्पूर्ण जगत्‌ विज्ञानमय है--ऐसा जानो। मेरे जाज्योंपर पूर्णतया ध्यान दो। इस विषयमें युधजनोंका ऐसा ही मत है कि यह संसार अनाधार है, भ्रमजन्य पदार्थोकी प्रतीतिपर ही स्थिर है तथा रागादि दोषोंसे दूषित है। इस संसारसकूटमें जोव अत्यन्त भटकता रहा है”
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6112)
- **Original**: इस प्रकार 'बुध्यत (जानों), युध्यध्ये (समझो), बुध्यत (जानो)' आदि अन्‍्दोंसे बुद्धधर्मका निर्देश कर मायामोहने दैल्योंसे उनका निजधर्म छुड़ा दिया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6113)
- **Original**: मायामोहने ऐसे नाना प्रकारके युक्तियुक्त वाक्य कहें जिससे उन दैत्यगणने त्रयीधर्मकों त्याग दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6114)
- **Original**: उन दैत्यगणने अन्य दैल्योंसे तथा उन्हेंने अन्यान्यसे ऐसे ही वाक्य कहे। हे मैत्रेय ! इस प्रकार उन्होंने श्रुतिस्मृतिविह्ठित अपने परम घर्मको त्याग दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6115)
- **Original**: है द्विज ! मोहकारी मायामोहने और भी अनेकानेक दैत्योंकों भिन्न-भिन्न प्रकारके विविध पाषण्डॉसे मोहित कर दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6116)
- **Original**: इस प्रकार थोड़े ही समयमें मायासोहके द्वारा मोहित होकर असुरगणने लैदिक घर्मकी बातचीत करना भी झोड़ दिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6117)
- **Original**: हे ट्विज ! उनमेंसे क्ेई वेदोंकी, कोई देखताओंकी, कोई याज़िक कर्म-कल्लपॉकी तथा कोई ब्राह्मणोंकी निन्‍दा करने लगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6118)
- **Original**: [वे कहने लगे--] “हिसासे भी धर्म होता है--यह बात किसी प्रकार युक्तिसंगत नहीं है । अग्रिमें हजि जलानेसे फल होगा--यह भी बच्चोंकी-सो यात है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6119)
- **Original**: अनेकों यज्ञोंके द्वार देवत्व छाभ करके यदि इन्द्रको शमी आदि काप्ठका ही भोजन करना पड़ता है तो इससे तो पत्ते खानेवाला पशु ही अच्छा है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6120)
- **Original**: यदि यज्ञमें बलि किये गये पशुक्ो स्वर्गकी प्राप्ति होती है तो यजमान अपने पिताको ही क्यों नहीं मार डालता ?
- **Translation**: 

---

