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

### Verse 1 (Vishnu Puran 0.9021)
- **Original**: ग्रह, नक्षत्र और तारागणको धारण करनेबाला तथा [ वृष्टि आदिके द्वारा इस अखिल विश्वका ] कारणस्वरूप आकाञ् तू ही है । हे जगद्धात्रि ! हे देवि ! ये सब्र तथा और भी सहस्त्रों और असंख्य विभूतियाँ इस समय तेरे उदरमें स्थित हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9022)
- **Original**: अआ0 3 ] पश्चम अंश अण्क ] आआ पश्चाआंश रेप समुद्राद्रिनदीद्वीपवनपत्तनभूषणा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9023)
- **Original**: ] आमखर्वटखेटाढ्या समस्ता पृथिवी शुभे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9024)
- **Original**: 13 समस्तव्कयो5म्मांसि सकलाश्व समीरणा: । अहर्क्तारकाचित्र विपानझतसंकुछम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9025)
- **Original**: 14 अबवकाशमशेषस्थ यहदाति नभःस्थलम्‌। भूलोंकश्व भुवल्लोंकस्स्वर्ोॉको5थ महर्जन:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9026)
- **Original**: 15 तपश्च ब्रह्मलोकश्ष ब्रह्माण्डसखखिले शुभे। ., तदत्तरे स्थिता देवा दैत्यगन्थर्वचारणा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9027)
- **Original**: 16 महोरगास्तथा यक्षा राक्षसा: प्रेतगुह्मका: । मनुष्या: पशवश्चान्ये ये च जीवा यशस्विनि
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9028)
- **Original**: 17 नैरन्तःस्थैरनन्तोउसो सर्वग: सर्वभावन:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9029)
- **Original**: 18 रूपकर्मस्वरूपाणि न परिच्छेदगोचरे । अस्थाखिलप्रमाणानि स विष्णुर्गर्भगस्तव
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9030)
- **Original**: 19 स्व स्वाहा स्व स्वधा विद्या सुधा त्वं ज्योतिरम्बरे । ते सर्वल्लेकरक्षार्थभवतीर्णा महीतले
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9031)
- **Original**: 20 प्रसोद देवि सर्वस्थ जगतइशं शुभे कुरु। है शुभे ! समुद्र, पर्वत, नदी, द्वीप, बन और नगरोंसे सुशोधित तथा ग्राम, खर्वट और खेटादिसे सम्पन्न समस्त पृथिवो, सम्पूर्ण आग्रि और जल तथा समस्त बायु, अह, नक्षत्र एवं तारागणोंसे चित्रित तथा सैकड़ों विमानोंसे पूर्ण सबको अवकाश देनेवाला आकाश, भूलोंक, भुवलोंक, स्वर््नेक तथा मह, जन, तप और बह्यलेकपर्यन्त सम्पूर्ण ब्रह्माप्ड तथा उसके अन्तर्वती देव, असुर, गन्धर्व, चारण, नाग, यक्ष, राक्षस, प्रेत, गुलाक, मनुष्य, पश्ञु और जो अन्यान्य जोव हैं, हे यशास्विनि ! वे सभी अपने अन्तर्गत होनेके कारण जो श्रोअनन्त सर्वगामी और सर्वभावन हैं तथा जितके रूप, कर्म, स्वभाव तथा [ बालत्व महत्त्त आदि ] समस्त परिमाण परिच्लेद (विचार) के विषय नहीं हो सकते जे ही श्रीविष्णु- भगवान्‌ त्तेरे गर्भमें स्थित हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9032)
- **Original**: 13---19
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9033)
- **Original**: तू ही स्वाहा, स्वधा, विद्या, सुधा और आकाशस्थिता ज्योति है। सम्पूर्ण लोकॉंकी रक्षाके लिये ही तूने पृथिबीमें अबतार लिया है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9034)
- **Original**: हे देवि : तू प्रसन्न हो। हे शुभे ! तू सम्पूर्ण जगतका कल्याण कर। जिसने इस सम्पूर्ण जगतको धारण किया है उस प्रभुको तू प्रीतिपूर्वक अपने प्रीत्या ते धारयेश्ानं धृ्ते येनाखिलं जगत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9035)
- **Original**: गर्भमें घारण कर
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9036)
- **Original**: सन नह 2200-ह इति श्रीविष्णुपुराणे पश्चमेंडशे द्वितीयोउध्याय:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9037)
- **Original**: कम है & सम्पन्न तीसरा अध्याय भरगवान्‌का आविर्भाव तथा योगमायाद्वारा कंसकी वच्चना औपयशर उवाच एबं संस्तृयमाना सा देवेदेंबमधारयत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9038)
- **Original**: गर्भेण पुण्डरीकाक्ष॑ जगतसत्राणकारणम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9039)
- **Original**: 1 ततो5खिलजगत्पदबोधायाच्युतभानुना .। देवकीपूर्वसन्ध्यायामाविर्भीत॑. महात्मना
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9040)
- **Original**: 2 #2200390 0 2 5 म्‌ । बभूव सर्वत्लोकस्य कौमुदी यथा
- **Translation**: 

---

