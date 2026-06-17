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

### Verse 1 (Vaivtpuran 12.6454)
- **Original**: जीवित हुए बालकको देखकर शिव-पार्वतीने जो सम्पूर्ण चराचर जगतू-स्वरूप हैं, उन्हीं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6455)
- **Original**: ब्राह्मणॉंकों असंख्य रत्न दान किये। मरे हुए श्रीकृष्णमें विनायक स्थित हैं। बालकके जी उठनेपर हर्षगद्रद हुए हिमालयने इस प्रकार श्रीविष्णुका कथन सुनकर पार्वतीका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6456)
- **Original**: वन्दियोंको एक सौ हाथी और एक सहसख्र घोड़े मन संतुष्ट हो गया। तब वे उन गदाधर भगवान्‌को
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6457)
- **Original**: प्रदान किये तथा देवगण हर्षित होकर ब्राह्मणोंको प्रणाम करके शिशुकों दूध पिलाने लगीं। तदत़न्तर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6458)
- **Original**: और सभी नारियोंने बन्दियोंको दान दिया। लक्ष्मीपति प्रसन्न हुई पार्वतीने शंकरजीकी प्रेरणासे अज्जञलि विष्णुने माज़लिक कार्य सम्पन्न कराया, ब्राह्मणोंको बाँधकर भक्तिपूर्वक उन कमलापति भगवान्‌ विष्णुकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6459)
- **Original**: भोजनसे तृत्त किया और वेदों तथा पुराणोंका पाठ स्तुति की। तब विष्णुने शिशुकों तथा शिशुकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6460)
- **Original**: कराया। तत्पश्चात्‌ शनैश्वरकों लज्जायुक्त देखकर माताको आशीर्वाद दिया और अपने आभूषण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6461)
- **Original**: पार्वतीको क्रोध आ गया और उन्होंने उस सभाके कौस्तुभभणिको बालकके गलेमें डाल दिया।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6462)
- **Original**: बीच शबनैश्वरको यों शाप देते हुए कहा--' तुम ब्रह्माने अपना मुकुट और धर्मने रन्नका आभूषण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6463)
- **Original**: अड्भहीन हो जाओ।' (अध्याय 12) हडलजल्‍ रिवर्स 7)> >> विष्णु आदि देवताओंद्वारा गणेशकी अग्रपूजा, पार्वतीकृत विशेषोषचारसहित गणेशपूजन, विष्णुकृत गणेशस्तवन और 'संसारमोहन ' नामक कवचका वर्णन श्रीनारायणजी कहते हैं--नारद! तदनन्तर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6464)
- **Original**: बुलवाकर उसे आशीर्वाद दिलाया। तदनन्तर सभी बिष्णुने शुभ समय आनेपर देवों तथा मुनियोंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6465)
- **Original**: देव-देवियोंने तथा मुनियों आदिने अनेक प्रकारके साथ सर्वश्रेष्ठ उपहारोंसे उस बालकका पूजन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6466)
- **Original**: उपहार गणेशकों दिये और फिर क्रमशः उन्होंने किया और उससे यों कहा--' सुरश्रेष् ! मैंने सबसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6467)
- **Original**: भक्तिपूर्वक्त उसकी पूजा की। पहले तुम्हारी पूजा की है; अतः वत्स! तुम नारद! तदनन्तर जगज्जननी पार्वतीने, जिनका सर्वपूज्य तथा योगीन्द्र होओ।' यों कहकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6468)
- **Original**: मुखकमल हर्षक कारण विकसित हो रहा था, श्रीहरिने उसके गलेमें वनमाला डाल दी और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6469)
- **Original**: अपने पुत्रकों रत्ननिर्मित सिंहासनपर बैठाया। फिर उसे मुक्तिद्ायक ब्रह्मज्ञान तथा सम्पूर्ण सिद्धियाँ
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6470)
- **Original**: उन्होंने आनन्दपूर्वक समस्त तीर्थोंके जलसे भरे प्रदान करके -अपने समान बना दिया। फिर हुए सौ कलशोंसे मुनियोंद्रारा वेद-मन्त्रोच्चारणपूर्वक थोडशोपचारकी सुन्दर बस्तुएँ दीं और मुनियों तथा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6471)
- **Original**: उसे स्नान कराया और अग्रिमें तपाकर शुद्ध किये देवॉके साथ उसका इस प्रकार नामकरण किया--
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.6472)
- **Original**: हुए दो बस्त्र दिये। फिर पाचद्यके लिये गोदाबरीका विध्लेश, गणेश, हेरम्ब, गजानन, लम्बोदर, एकदन्त,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.6473)
- **Original**: जल, अध्यके निर्ित्त गड़ाजल और आचमनके शूर्पकर्ण और विनायक--उसके ये आठ नाम रखे
- **Translation**: 

---

