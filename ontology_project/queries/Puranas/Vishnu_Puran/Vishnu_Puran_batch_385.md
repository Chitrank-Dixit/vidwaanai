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

### Verse 1 (Vishnu Puran 0.7681)
- **Original**: तदनन्तर सत्राजितके प्रणाम तथा स्तुति आदि कर चुकनेपर सहस्लोशु भगवान्‌ आदित्यने उससे कहा--'तुम अपना अभीष्ट खबर माँगो'
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7682)
- **Original**: सत्राजितने उस स्थमन्तकमणिकों ही माँगा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7683)
- **Original**: तब भगवान्‌ सूर्य उसे वह मणि देकर अत्तरिक्षमें अपने स्थानकों चके गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7684)
- **Original**: फिर सज्नाजितने उस निर्मल मणिरत्रसे अपना कण्ठ सुशोभित होनेके कारण तेजसे सूर्यके समान समस्त दिशाओंको प्रकाशित करते हुए द्वारकामें प्रवेद्ट किया । 19
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7685)
- **Original**: द्वारकावासी ल्मेगोने उसे आते देख, पृथिवीका भार उतारनेके ल्विये अंद्ाकपसे अवतोर्ण हुए मनुष्यरूपधारी आदिपुल्ष भगवान्‌ पुरुषोत्तमसे प्रणाम कस्के क्हा--
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7686)
- **Original**: “भगवन्‌ ! आपके दर्शनोके ल्थ्ये निश्रय ही ये भगवान्‌ सूर्यदेव आ रहे है'' उनके ऐसा कहनेपर भगखान्‌ने उनसे कहा--
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7687)
- **Original**: “ये भगवान्‌ सूर्य नहीं हैं, सत्नाजित्‌ है। यह सूर्यभगवानसे प्राप्त हुई स्यमत्तक नामको महाम्णिकों धारणकर यहाँ आ रहा है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7688)
- **Original**: तुमल्छोेग अब विश्वस्त होकर इसे देखो ।” भगवानके ऐसा वजनेपर द्वारकावासी उसे ठसी प्रकार देखने लगे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7689)
- **Original**: सत्राजितने वह स्थसन्तकमणि अपने घरमें रख दी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7690)
- **Original**: 272 प्रतिदिन तनन्‍्मणिरत्रमष्टो. कनकभारान्सत्रवति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7691)
- **Original**: तत्प्रभाबाद्च सकलस्थैव राष्ट्स्योप- सर्गनावृष्टिव्यालामिचोरदुर्भिक्षादिभय॑ न भवति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7692)
- **Original**: अच्युतो5पि तद्विव्यं रत्रमुग्रसेनस्य भूपतेयोग्यमेतदेति लिप्सां. चक्रे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7693)
- **Original**: गोत्रभेदभयाच्छक्तो5पि न जहार
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7694)
- **Original**: सत्राजिदष्यच्युतों मामेतद्याचयिष्यतीत्यवगम्य रत्ललो भाद्ात्रे प्रसेनाय तद्॒त्लमदात्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7695)
- **Original**: तच्च झुचिना ध्रियमाणमशेषमेब सुवर्णस्रवादिकं गुणजातमुत्पादबति अन्यथा धारयन्तमेव हन्ती- त्यजानत्नसावपि प्रसेनस्तेन कण्ठसक्तेन स्थमन्तके- नाश्वमारुद्माटव्यां मृगवामगच्छत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7696)
- **Original**: तत्र च सिंहाद्धमवाप
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7697)
- **Original**: साश्च च ते निहत्य सिंहो5प्यमलछमणिरल्रमास्थाग्रेणादाय गन्तु- मभ्युद्यतः, ऋक्षाध्रिपतिना जाम्बबता दृष्टो घातितश्च
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7698)
- **Original**: । _ जाम्बबानप्यमलमणिरल्न- मादाय स्वबिले प्रविवेश ।। 33
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7699)
- **Original**: सुकुमारसंज्ञाय बालकाय च क्रीडनकमकरोत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7700)
- **Original**: अनागच्छति तस्मिग्सेने कृष्णो मणिरत्र- मभिलषितवाग्स च॑ प्राप्तवाब्यूनमेतदस्य कर्मेत्यखिल एवं यदुलोक: परस्पर कर्णाकर्ण्य- कथयत्‌
- **Translation**: 

---

