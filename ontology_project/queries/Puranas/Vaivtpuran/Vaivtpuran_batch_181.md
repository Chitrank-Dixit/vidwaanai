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

### Verse 1 (Vaivtpuran 13.2989)
- **Original**: राज्य भी उनके हाथमें नहीं है। एकमात्र लक्ष्मीकी ही मनुष्य सदाके लिये अभय एवं मड्भलमय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.2990)
- **Original**: उपासना ही उनके जीवनका उद्देश्य बन गया बन जाते हैं। परंतु जगत्प्रभो! अब मेरे उस
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.2991)
- **Original**: है। अत: उनकी भार्याओंके उदरसे भगवतों भक्तकी जीवनचर्या कैसे चलेगी-यह बतानेकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.2992)
- **Original**: लक्ष्मी अपनी एक कलासे प्रकट होंगी। तब वे कृपा कीजिये; क्योंकि सूर्यके शापसे उसकी श्री
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.2993)
- **Original**: दोनों नरेश लक्ष्मीसे सम्पन्न हो जायँगे। शम्भो! नष्ट हो चुकी है। उसमें सोचने-समझनेकी शक्ति
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.2994)
- **Original**: अब आपके सेवक वृषध्वजका शरीर नहीं रहा। भी तनिक-सी नहीं रह गयी है। अत: आप यहाँसे पधार सकते हैं। देवताओ।! भगवान्‌ विष्णु बोले--शम्भो! दैवकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.2995)
- **Original**: अब आप लोग भी जानेका कष्ट करें। प्रेरणासे बहुत समय बीत गया। इक्कीस युग समाप्त नारद! इस प्रकार कहकर भगवान्‌ श्रीहरि हो गये। यद्यपि वैकुण्ठमें अभी आधी घड़ीका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.2996)
- **Original**: लक्ष्मीके सहित सभासे उठे और अन्तःपुरमें चले समय बीता है। अतः अब आप शोघ्र अपने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.2997)
- **Original**: गये। देवताओंने भी बड़ी प्रसन्नताके साथ अपने स्थानपर पधारिये। किसीसे भी न रुकनेवाले
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.2998)
- **Original**: आश्रमकी यात्रा की। परिपूर्णतम शंकर उसी क्षण अत्यन्त भयंकर कालने इस समय वृषध्वजकों
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.2999)
- **Original**: तपस्या करनेके विचारसे चल पड़े। (अध्याय 13) 42+00-नियपान्‍ज+>त0> वेदबतीकी कथा, इसी प्रसड्रमें भगवान्‌ रामके चरित्रका एक अंश-कथन, भगवती सीता तथा द्रौपदीके पूर्वजन्मका वृत्तान्त भगवान्‌ नारायण कहते हैं--मुने ! धर्मध्वज
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3000)
- **Original**: मन्त्रोंका उच्चारण किया और उठकर खड़ी हो और कुशध्वज--इन दोनों नरेशोंने कठिन तपस्याद्वार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3001)
- **Original**: गयो। इसलिये विद्वान्‌ पुरुष उसे 'वेदबती' कहने भगवती लक्ष्मीकी उपासना करके अपने प्रत्येक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3002)
- **Original**: लगे। उत्पन्न होते ही उस कन्याने स्नान किया अभीष्ट मनोरथको प्राप्त कर लिया। महालक्ष्मीके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3003)
- **Original**: और तपस्या करनेके विचारसे वह बनकी ओर बर-प्रसादसे उन्हें पुन: पृथ्वीपति होनेका सौभाग्य
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3004)
- **Original**: चल दी। भगवान्‌ नारायणके चिन्तनमें तत्पर प्राप्त हो गया। वे दोनों धनवान्‌ और पुत्रवान्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3005)
- **Original**: रहनेबाली उस देवीको प्राय: सभीने रोका; परंतु हो गये। कुशध्वजकी परम साध्वी भार्याका नाम
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3006)
- **Original**: उसने किसौकी भी नहीं सुनी। बह तपस्थबिनी मालाबती था। समयानुसार उसके एक कन्या
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3007)
- **Original**: कन्या एक मन्वन्तरतक पुष्करक्षेत्रमें तपस्या करती उत्पन्न हुई, जो लक्ष्मीका अंश थी। वह भूमिपर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3008)
- **Original**: रही। उसका तप अत्यन्त कठिन था तो भी पैर रखते ही ज्ञानसे सम्पन्न हो गयी। उस कन्याने
- **Translation**: 

---

