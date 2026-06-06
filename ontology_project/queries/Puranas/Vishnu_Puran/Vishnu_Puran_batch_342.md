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

### Verse 1 (Vishnu Puran 0.6821)
- **Original**: राजकुमार असमञ्सके आओशझ्ुमान्‌ नामक पुत्र बुआ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6822)
- **Original**: यह असमज़स बाल्यावस्थासे ही बड़ा दुराचारी था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6823)
- **Original**: पिताने सोचा कि बाल्याबस्थाके बीत जानेपर यह यहुत समझदार होगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6824)
- **Original**: किन्तु यौबनके बीत जानेपर भी जब उसका आचरण न सुधरा तो पिताने उसे ल्याग दिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6825)
- **Original**: उनके साठ हजार पुत्रोंने भी असमञ्ञसके चरित्रकाा ही अनुकरण,किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6826)
- **Original**: तब, असमजसके चरित्रका अतुकरण करनेबाले उन सगयपुत्रोंद्रार संसारमें यज्ञादि सतार्गका उच्छेद हो जानेपर सकल-विद्यानिधान, .अशेषदोषहीन, भगवान्‌ पुरुषोत्तमके अंद्ञाभूत श्रीकपिलदेबसे देवताओंने प्रणाम करनेके अनन्त्तर उनके विषयमें कहा--
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6827)
- **Original**: “भरगवन्‌ ! राजा सगरके ये सभी पुत्र असमञसके चरिक्का ही अनुसरण कर रहे हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6828)
- **Original**: इन सबके असन्मार्गमें प्रवृत्त रहनेसे संसारकी क्या दहला छोगी ?
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6829)
- **Original**: प्रभो! संसारमें दीनजनॉकी रक्षाके लिये ही आपने यह शरीर ग्रहण किया है [ अतः इस घोर आपत्तिसे संसारको रक्षा कीजिये ] ।” यह सुनकर भगवान्‌ कपिल्ने कहा, “ये सब थोड़े हो दिनोंमें नष्ट हो जायैंगे''
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6830)
- **Original**: 2446 श्रीविष्णुपुराण (अण्ड अत्रान्तरे स्व सगरो हयमेधमारभत
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6831)
- **Original**: तस्य चपुत्रैरधिष्ठितमस्याश्च को उप्यपहुत्य भुवो बिल प्रवियेश
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6832)
- **Original**: _ ततस्तत्तनयाश्षाश्वखुरगति- निर्बनधेनावनीमेकेको योजन चस्नु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6833)
- **Original**: पाताले चाश्व॑ परिभ्रमन्त तमवनीपतितनयास्ते ददुशुः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6834)
- **Original**: नातिदूरेशबस्थितं. ऊन भगवन्‍न्तमपघने अआरत्कालेईर्कमिय तेजोभिरनवरतपूर्ध्यमश्रश्नादोषदिश श्षोजासयमारन हयहर्त्तार कपिलर्षिमपश्यन्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6835)
- **Original**: ततश्लोद्यतायुधा. दुरात्पानोउयमस्मदपकारी अज्ञविश्नकारी हन्यतां हयहर्त्ता हन्यतामित्यवोच- ऋ््यधावंश्ष
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6836)
- **Original**: _ ततस्तेनापि भगवता भक्तिनप्रस्तता. तुष्टाव
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6837)
- **Original**: अथेैनं भगवानाह
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6838)
- **Original**: गच्कैनं पितामहायाश्व॑ प्रापय बर॑ वृणीघ्र च पुत्रक पोत्रश्न ते स्वर्गाढड्रो भुवमानेष्यतः इति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6839)
- **Original**: _ अश्रांशुमानपि स्वर्यातानां. ब्रह्मदण्डहतानामस्मत्पितृणामस्वर्ग योग्यानां स्वर्गप्राप्तिकरं वरमस्मारक प्रयच्छेति प्रत्याह
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6840)
- **Original**: तदाकर्ण्य ते क्ष भगवानाह उत्तमेवैतन्मयाद्य.. पौज्नस्ते .. त्रिदिवादडां पझ्रुबसानेष्यतीति
- **Translation**: 

---

