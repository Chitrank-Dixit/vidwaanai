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

### Verse 1 (Vaivtpuran 543.16174)
- **Original**: सारे शरीरमें रोमाज्न हो आया। वे भक्तिविह्लल जिसे परात्पर सर्वेश्वर शंकर भक्तिपूर्बवक अपने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16175)
- **Original**: हो रुदन करते हुए मूर्च्छित होकर भूमिपर गिर सिरपर धारण करते हैं, विरक्त होकर सदा उन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16176)
- **Original**: पड़े। तत्पश्चात्‌ परमेश्वर श्रीकृष्णका ध्यान करके तीर्थकीर्ति श्रीकृष्णका कीर्तन करते रहते हैं तथा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16177)
- **Original**: वे अपनेकों तुच्छ मानने लगे और भक्तिपूर्वक आहार, भूषण और वस्त्रका परित्याग करके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16178)
- **Original**: उस गोपीसे बोले। दिगम्बर हो भक्तिके आवेशमें क्षणभरमें नाचने उद्धवने कहा--सातों द्वीपोंमें मनोहर जम्बूद्दीप लगते हैं और क्षणभरमें गाने लगते हैं। ब्रह्मा,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16179)
- **Original**: धन्य एवं प्रशंसनीय है। उसमें श्रेष्ठ भारतवर्ष--जो
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16180)
- **Original**: 706 * संक्षिप्त ब्रह्मवैवर्तपुराण के #5####$# # #$ 55 #4 88 # 8 #$ 4 8 # 8 95 # 5 48 85 ## #$# 4 ## # 5 95 8 5 # # # 8 8 $ #% $ 9 #5 98 # 5 4 $ 8 $ #8 9 5 8 68% 8# पुण्य और मज्ुलोंका दाता है--गोपियॉके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16181)
- **Original**: गोपियोंका किंकर होकर तोर्थश्रव्ा श्रीकृष्णका चरणकमलोंकी रजसे पावन और परम निर्मल
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16182)
- **Original**: कीर्तन सुनता रहूँगा; क्योंकि गोपियोंसे बढ़कर होकर और भी धन्यवादका पात्र हो गया है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16183)
- **Original**: परमात्मा श्रीहरिका कोई अन्य भक्त नहीं है। इस भारतवर्षमें नारियोंके मध्य गोपिकाएँ सबसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16184)
- **Original**: गोपियोंने जैसी भक्ति प्राप्त की है, जैसी भक्ति बढ़कर धन्या और मान्या हैं; क्योंकि वे उत्तम दूसरोंकों नहीं नसीब हुई। पुण्य प्रदान करनेवाले श्रीराधाके चरणकमलोंका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16185)
- **Original**: ._तदनन्तर कलावती और तुलसीके द्वारा नित्य दर्शन करती रहती हैं*। इन्हों राधिकाके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16186)
- **Original**: श्रीकृष्णकी महिमा कही जानेके बाद कालिकाने चरणकमलोंकी रजको प्राप्त करनेके लिये ब्रह्माने कहा--बुद्धिमान्‌ उद्धव! बाल, युवा और वृद्ध-तीनों साठ हजार वर्षोतक तप किया था। ये पराशक्ति
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16187)
- **Original**: प्रकारके मनुष्य तथा जो देवता आदि और राधा गोलोकमें निवास करनेवाली और श्रीकृष्णकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16188)
- **Original**: सिद्धगण हैं; वे सभी उन परमेश्वर श्रीकृष्णको प्राणप्रिया हैं। जो-जो श्रीकृष्णके भक्त हैं, वे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16189)
- **Original**: जानते हैं। इस समय इन मूच्छित हुई राधाको राधाके भी भक्त हैं। ब्रह्मा आदि देवता गोपियोंकी जगाना ही युक्त है; अत: इसके लिये जो प्रधान सोलहवीं कलाकी भी समानता नहीं कर सकते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16190)
- **Original**: युक्ति हो उसके द्वारा इन्हें चैतन्य करो। श्रीकृष्णकी भक्तिका मर्म पूर्णरूपसे तो योगिरिज
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16191)
- **Original**: त्तब उद्धव बोले--कल्याणि! चेत करो। महे श्वर, राधा तथा गोलोकवासी गोप और गोपियाँ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16192)
- **Original**: जगन्मात:! मेरी ओर ध्यान दो। मैं कृष्णभक्तके ही जानती हैं। ब्रह्मा और सनत्कुमारको कुछ-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16193)
- **Original**: किंकरका भी किंकर उद्धव हूँ। माँ! मुझपर कृपा कुछ ज्ञात है। सिद्ध और भक्त भी स्वल्प हो
- **Translation**: 

---

