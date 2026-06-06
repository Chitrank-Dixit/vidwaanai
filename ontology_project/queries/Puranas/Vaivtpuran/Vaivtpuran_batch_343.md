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

### Verse 1 (Vaivtpuran 16.3354)
- **Original**: ब्रह्मराक्षस, वेताल, राक्षस, यक्ष और किन्नर भी समीप आ पहुँचे। वीरभद्र, नन्दीश्वर, महाकाल,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3355)
- **Original**: सहयोग देनेके लिये आ पहुँचे। इन सबको साथ सुभद्र, विशालाक्ष, पिड्रलाक्ष, बाणासुर, बिकम्पन,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3356)
- **Original**: लेकर स्वामी कार्तिकेयने अपने पिता चन्द्रशेखर विरूप, विकृति, मणिभद्र, बाष्कल, कपिलाक्ष,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3357)
- **Original**: शिवको प्रणाम किया और सहायता करनेके दीर्घदंष्र, विकट, ताम्रलोचन, कालंकट, बलीभद्र,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3358)
- **Original**: विचारसे उनकी आज्ञा लेकर पास बैठ गये। कालजिह्न, कुटीचर, बलोन्मत्त, रणश्लाघी, दुर्जय, इधर दूतके चले जानेपर प्रतापी शह्ढुचूड़ दुर्ग, आठों भैरव, ग्यारहों रुद्र, आठों वसु, इन्द्र
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3359)
- **Original**: अन्तःपुरमें गया और उसने अपनी पत्नी तुलसीसे आदि देवता, बारहों सूर्य, अग्नि, चन्द्रमा, विश्वकर्मा,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3360)
- **Original**: युद्धसम्बन्धी बातें बतायीं। सुनते ही तुलसीके दोनों अश्विनीकुमार, कुबेर, यमराज, जयन्त, नलकूबर,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3361)
- **Original**: होठ और तालु सूख गये। उसका हृदय संतप्त
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3362)
- **Original**: + प्रकृतिंखण्ड + 153 5546#£6£4## $£ 4 $ 4 % 4 44 4 44 5 ऋ% 4 4 4 55% 444 54% / 44% 4 डक 4 क्र ह कक कक कक 4 4 कक $ 5 ध कड़क ड़ हो उठा। फिर परम साध्वी तुलसी मधुर वाणीमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3363)
- **Original**: जनका संहार करते हैं, उन्हीं त्रिगुणातीत परम कहने लगी। प्रभु राधावल्लभकी तुम उपासना करो। उन्हींकी तुलसीने कहा--प्राणबन्धों ! नाथ! आप मेरे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3364)
- **Original**: आज्ञासे सदा शीघ्रगामी पवन प्रवाहित होते हैं, प्राणोंके अधिष्ठाता देव हैं। आप विराजिये। क्षणभर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3365)
- **Original**: सूर्य आकाशमें तपते हैं, इन्द्र समयानुसार वर्षा मेरे जीवनकी रक्षा कीजिये। मैं अपने नेत्रोंसे कुछ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3366)
- **Original**: करते हैं, मृत्यु प्राणियोंमें बिचरती है, अग्नि समयतक तो आदरपूर्वक आपके दर्शन कर लूँ।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3367)
- **Original**: यथावसर दाह उत्पन्न करते हैं तथा शीतल चन्द्रमा मेरे प्राण फड़फड़ा रहे हैं। आज मैंने रातके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3368)
- **Original**: भयभीतकी भाँति आकाशमण्डलमें चक्कर लगाते अन्तिम क्षणमें एक बुरा स्वप्न देखा है। हैं। प्रिये! जो मृत्युकी मृत्यु, कालके काल, महाराज शह्लुचूड़ ज्ञानी पुरुष था। तुलसीकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3369)
- **Original**: यमगजके श्रेष्ठ शासक, ब्रह्माके स्वामी, माता- बात सुनकर उसने भोजन किया। जल पिया।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3370)
- **Original**: की-माता, जगत्‌की जननी तथा संहार करनेवालेके' फिर अवसर पाकर उसने सत्य, हितकर एवं
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3371)
- **Original**: भी संहारकर्ता हैं, उन परम प्रभु भगवान्‌ यथार्थ बचन तुलसीसे कहे। श्रीकृष्णकी शरणमें तुम जाओ। प्रिये! यहाँ कौन शब्डुचूड़ बोला--प्रिये ! कर्म-भोगका सारा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3372)
- **Original**: किनका बन्धु है! जो सबके बन्धु हैं, उन्हींकी निबन्ध कालके सूत्रमें बँधा है। शुभ, हर्ष, सुख,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3373)
- **Original**: तुम उपासना करो। ब्रह्माने हम दोनोंकों एक दुःख, भय, शोक और मदुल-सभी कालके
- **Translation**: 

---

