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

### Verse 1 (Markende Puran 0.3861)
- **Original**: प्रार्थना करें।' इस प्रकार एक निश्चय करके कुछ पृथ्चोका पाला किया, अब मेरें लिये यह
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3862)
- **Original**: लोग अपने पघरोंपर विधिपूर्वक अर्थ्य, इप्चार तनबासकी समय आ गया। मेरे कई पुन्न हों गढे।
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3863)
- **Original**: आदि उपहारोंसे भगवान्‌ भास्‍्करकी पृ्णों करने मेरी सन्तानोंकों देखकर थोड़े ही दिनोंमें यमराज
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3864)
- **Original**: लगे। दूसरे लोग मौन रहकर ऋग्वेद, थजुर्वेद और मेरा यहाँ रहता नहीं सह सकेगा। नागरिकों! मेरे
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3865)
- **Original**: सामबेदके जपसे सर्वदेवको सन्तुष्ट करने लगे। पस्तकपर जो यह सफेद बाल दिखायो देता है,
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3866)
- **Original**: अन्य लोग रिराहार रहकर नदीके तटपर निवास इसे आत्यन्त भयानऋ कर्म करनेबालों पृत्दुका दूत
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3867)
- **Original**: करते हुए तपस्याके द्वारा भगवान्‌ सूर्यक्षो आराधनामें समझी; अत; मैं राज्यपर अपने पुत्रकां अभिषेक
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3868)
- **Original**: लग गये। कुछ लोग शग्निहोत्र करते, कुछ दिन- करके सक भौगोंकों त्याग दूँगा और घनमें रहकर
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3869)
- **Original**: गत सूर्यसूक्तका 58 करते और कुक्त लोग मूर्थकी तपस्या करूँगा। जबतक वमग़जक्रे सैंतिक नहीं
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3870)
- **Original**: ओर दृष्टि लगाकर खड़े रहते थे। आते,
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3871)
- **Original**: भीतेक बह सब कुछ मुझे कर लेना है।। . सूर्वकों आराधनाके लिये इस प्रकार यत्त तदनन्तर बनपें जानेकों इन्छासे महारजने
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3872)
- **Original**: करनेवाले ठत लोगोॉके समोपष आक़र सुदामा श्योतिपियोंकों बुलाया और पुत्रके रज्याभिषेकके
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3873)
- **Original**: नापक गन्भवंने कहा--द्विजवरो! यदि आपलोगोको लिये शुभ दिन एवं लग्न पूछे। राजाकी यात
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3874)
- **Original**: सूर्यदेचक्कों आएधना अभोष्ट है तो ऐसा कौजिये, सुनकर थे शारबदर्शी ज्योतिपों ब्याकुदा हो गये।
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3875)
- **Original**: जिससे भगवान्‌ भास्कर प्रसन्न हो सकें। आपलोग उन्हें दिने, लान और होरा आदिक। ठौ ज्ञान न
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3876)
- **Original**: यहाँसे शीघ्र ही कामरूप पर्वतपर जाहये। वहाँ हो सका। त़दनन्तर अन्य नगरों, अधोनस्थ राज्यों
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3877)
- **Original**: गुरुविशाल नामक जन है, जिसमें सिद्ध पुरुष तथा 3स नगदसे भी बहुत-से श्रेष्ठ ब्राह्मण आये
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3878)
- **Original**: निचास ऋरते हैं। उहाँपर एकाग्रनित्त होकर और बनमें जानेके लिये उत्पुक राजा राज्यचर्धनसे
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3879)
- **Original**: आपल्लोग सूर्यक्रो आराभना करें। वह परग दितकारी मिलें। त॒त्त सपय उनका माथा काँप ठटा। ते
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3880)
- **Original**: सिद्ध क्षेत्र है। वहाँ आपलोगोंकों संबे कापनाएँ बोले--' राजद
- **Translation**: 

---

