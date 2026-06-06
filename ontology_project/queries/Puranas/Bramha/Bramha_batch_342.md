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

### Verse 1 (Bramha 0.6821)
- **Original**: तथापि यदुकुमारोंने उनके साथ छल किया। यह वध कराकर इस पृथ्वीका भार उतारा। इस प्रकार
- **Translation**: 

---

### Verse 2 (Bramha 0.6822)
- **Original**: देख उत्तम ब्रतका पालन करनेवाले उन महर्षियोंने सम्पूर्ण दुष्ट राजाओंका संहार करके भृभार उत्तारनेके
- **Translation**: 

---

### Verse 3 (Bramha 0.6823)
- **Original**: थादवोंके वाशके लिये शाप देते हुए कहा--' यह है)».
- **Translation**: 

---

### Verse 4 (Bramha 0.6824)
- **Original**: 330 « संक्षिप्त अहमपुराण « स्त्री एक मुसल पैदा करेगी, जिससे सम्पूर्ण. श्रीभगवान्‌ बोले-'दूत! तुम जो कुछ कहते यदुकुलका संहार हो जायगा।' उनके यों
- **Translation**: 

---

### Verse 5 (Bramha 0.6825)
- **Original**: हो, वह सब मैं जानता हूँ। इसीलिये मैंने कहनेपर यदुकुमारोंने पुरीमें आकर राजा उप्रसेनको
- **Translation**: 

---

### Verse 6 (Bramha 0.6826)
- **Original**: यादबोंके संहारका कार्य आरम्भ कर दिया है। सब हाल कह सुनाया। साम्बके पेटसे मुसल
- **Translation**: 

---

### Verse 7 (Bramha 0.6827)
- **Original**: यदि यदुबंशियोंका संहार न हो तो यह पृथ्बीपर पैदा हुआ। उग्रमसेनने उस मुसलके लोहेको
- **Translation**: 

---

### Verse 8 (Bramha 0.6828)
- **Original**: बहुत बड़ा भार रह जायगा; अत: मैं सात रातके कुटवाकर चूर्ण बना दिया और उसे समुद्रमें फेंक
- **Translation**: 

---

### Verse 9 (Bramha 0.6829)
- **Original**: भीतर जल्दी ही इस भारको भी उतार डालूँगा। दिया। बह चूर्ण एरका नामकी घासके रूपमें
- **Translation**: 

---

### Verse 10 (Bramha 0.6830)
- **Original**: जिस प्रकार मैंने द्वारकापुरी बसानेके लिये उत्पन्न हो गया। मुसलका जो लोहा था, उसे
- **Translation**: 

---

### Verse 11 (Bramha 0.6831)
- **Original**: समुद्रसे भूमि माँगी थी, उसी प्रकार उसे वह चूर्ण कर देनेपर भी उसका एक टुकड़ा बचा रह
- **Translation**: 

---

### Verse 12 (Bramha 0.6832)
- **Original**: भूमि लौटा भी दूँगा और यादवोंका संहार करके गया। उसे यादवगण किसी प्रकार भी चूर्ण न
- **Translation**: 

---

### Verse 13 (Bramha 0.6833)
- **Original**: अपने परमधामको जाऊँगा। देवराज इन्द्र तथा कर सके। उसका आकृति तोमरके समान थीं। देवताओंकों यों मानना चाहिये कि मैं बलरामजीके वह दुकड़ा भी समुद्रमें फेंक दिया गया, किंतु साथ अब अपने धाममें आ ही गया। इस उसे एक मत्स्यने निगल लिया। उस मत्स्यको
- **Translation**: 

---

### Verse 14 (Bramha 0.6834)
- **Original**: पृथ्वीके भाररूप जो जरासंध आदि राजा थे, वे मछेरोंने जाल बिछाकर पकड़ लिया। जब
- **Translation**: 

---

### Verse 15 (Bramha 0.6835)
- **Original**: मारे गये; तथापि इन यदुवंशियोंका भार उनसे ठसका पेट चीरा गया, तब वह लोहा निकला
- **Translation**: 

---

### Verse 16 (Bramha 0.6836)
- **Original**: भी बढ़कर है, अतः पृथ्बीके इस महाभारकों और उसे जरा नामक व्याधने ले लिया। भगवान्‌
- **Translation**: 

---

### Verse 17 (Bramha 0.6837)
- **Original**: उतारकर ही मैं देवलोककी रक्षाके लिये अपने श्रीकृष्ण इन सभी बातोंकों अच्छी तरह जानते
- **Translation**: 

---

### Verse 18 (Bramha 0.6838)
- **Original**: धाममें जाऊँगा।!' थे तो भी उन्होंने विधाताके विधाननमो बदलना
- **Translation**: 

---

### Verse 19 (Bramha 0.6839)
- **Original**: भगवान्‌ वासुदेवके यों कहनेपर देबदूत नहीं चाहा। इसी बीचमें देवताओंने भगवान्‌
- **Translation**: 

---

### Verse 20 (Bramha 0.6840)
- **Original**: उन्हें प्रणाम करके दिव्य गतिसे देवराजके श्रीकृष्णके पास अपना दूत भेजा। उसने एकान्तमें
- **Translation**: 

---

