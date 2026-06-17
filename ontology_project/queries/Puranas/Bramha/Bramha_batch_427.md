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

### Verse 1 (Bramha 0.8521)
- **Original**: दृष्टिगोचर होता है। जो महात्मा ब्राह्मण मनीषी, (संकल्प)-का परिणाम है। ध्यान, वेदाध्ययन, , थ्रैरयबान्‌, महाज्ञानी और सम्पूर्ण प्राणियोंके हितमें दान, सत्य, लज्जा, सरलता, क्षमा, शौच, आत्मशुद्धि
- **Translation**: 

---

### Verse 2 (Bramha 0.8522)
- **Original**: तत्पर रहनेवाले हैं, वे ही उस आत्माका दर्शन कर एवं इन्द्रियसंयम--इनसे तेजकी वृद्धि होती है
- **Translation**: 

---

### Verse 3 (Bramha 0.8523)
- **Original**: पाते हैं। जो योगी एकान्तमें बैठकर कठोर और पापका नाश होता है।* नियमोंका पालन करते हुए थोड़े समय भी इस योगीको चाहिये कि वह सम्पूर्ण प्राणियॉमें
- **Translation**: 

---

### Verse 4 (Bramha 0.8524)
- **Original**: प्रकार योगाभ्यास करता है, वह अक्षर ब्रह्मकी समान भाव रखे; जो कुछ मिल जाय, उसीसे
- **Translation**: 

---

### Verse 5 (Bramha 0.8525)
- **Original**: समानताको प्राप्त हो जाता है। निर्वाह करे। पापरहित, तेजस्वी, मिताहारी और
- **Translation**: 

---

### Verse 6 (Bramha 0.8526)
- **Original**: योग-साधनामें अग्रसर होनेपर मोह, भ्रम और जितेन्द्रिय होकर, काम और क्रोधकों वशमें करके
- **Translation**: 

---

### Verse 7 (Bramha 0.8527)
- **Original**: आवर्त आदि विष्न प्राप्त होते हैं। दिव्य सुगन्ध ब्रह्मपदका सेवन करे। योगी रातके पहले और
- **Translation**: 

---

### Verse 8 (Bramha 0.8528)
- **Original**: आती है, दिव्य बाणीका श्रवण तथा दिव्य रूपोंके पिछले पहरमें मन एवं इन्द्रियॉकों एकाग्र करके
- **Translation**: 

---

### Verse 9 (Bramha 0.8529)
- **Original**: दर्शन होते हैं। अद्भुत बातें देखनेमें आती हैं। ध्यानस्थ हो मनकों आत्मामें लगाबे। जैसे मशकमें
- **Translation**: 

---

### Verse 10 (Bramha 0.8530)
- **Original**: अलौकिक रस और स्पर्शका अनुभव होता है। एक जगह भी छेद हो जानेपर सारा पानी बह
- **Translation**: 

---

### Verse 11 (Bramha 0.8531)
- **Original**: इच्छानुकूल सर्दी और गर्मो प्राप्त होती है। वायुकी जाता है, उसी प्रकार यदि साधककौ पाँच
- **Translation**: 

---

### Verse 12 (Bramha 0.8532)
- **Original**: भाँति आकाशमें चलने-फिरनेकी शक्ति आ जाती इन्द्रियॉमेंसे एक इन्द्रिय भी विकृत हो विषयोंकी
- **Translation**: 

---

### Verse 13 (Bramha 0.8533)
- **Original**: है। प्रतिभा बढ़ जाती है और उपद्रवोंका अभाव ओर चली जाय तो वह अपनी बुद्धि और विवेक
- **Translation**: 

---

### Verse 14 (Bramha 0.8534)
- **Original**: हो जाता है। योगसे इन सिद्धियोंके प्राप्त होनेपर खो बैठता है। जैसे मछुआ पहले जाल काटनेवाली
- **Translation**: 

---

### Verse 15 (Bramha 0.8535)
- **Original**: भी तत्त्ववेत्ता पुरुष उनकी उपेक्षा करके समभावसे मछलीको पकड़कर पीछे अन्य मछलियोंको
- **Translation**: 

---

### Verse 16 (Bramha 0.8536)
- **Original**: ही उन्हें लौटा दे। वह योगका ही अभ्यास बढ़ाये पकड्ता है, उसी प्रकार योगवेत्ता साधक पहले
- **Translation**: 

---

### Verse 17 (Bramha 0.8537)
- **Original**: और नियमपूर्वक रहते हुए पहाड़की चोटीपर, अपने मनकों वशमें करे। तत्पश्चात्‌ कान, नेत्र,
- **Translation**: 

---

### Verse 18 (Bramha 0.8538)
- **Original**: शून्य देवमन्दिर्में अथवा वृक्षोंके नीचे बैठकर जिद्बा तथा नासिका आदि इन्द्रियॉंका निग्रह करे।
- **Translation**: 

---

### Verse 19 (Bramha 0.8539)
- **Original**: योगका अभ्यास करे। इन्द्रिय-समुदायको संयममें इन सबको अधीन करके मनमें स्थापित करे और
- **Translation**: 

---

### Verse 20 (Bramha 0.8540)
- **Original**: रखकर एकाग्रचित्त हो निरन्तर आत्माका चिन्तन मसनको भी संकल्प-विकल्पसे हटाकर बुद्धिमें करता रहे। योगसे मनको उद्विग्न न होने दे। जिस स्थिर करे। इस प्रकार पाँचों इन्द्रियोंको मनमें और
- **Translation**: 

---

