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

### Verse 1 (Vishnu Puran 0.2321)
- **Original**: 11 कि देव: किमनन्तेन किमन्येन तवाश्रय: । पिता ते सर्वलोकानां त्वं तथैव भविष्यसि
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2322)
- **Original**: 12 श्रीपराप्रजी बोले--उनकी ऐसी चेष्टा देख टैल्यॉने दैत्यगज हिरण्यकशिपुसे डरकर उससे सारा यूत्तान्त कह सुनाया; और उसने भी तुरन्त अपने रसोइयॉको बुल्ककर कहा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2323)
- **Original**: हिरण्यकशिपु ओला--अरे सूदगण ! मेशा यह दुष्ट और दुर्मति पुत्र औरोंको भी कुमार्गका उपदेश देता है, अतः तुम शीघ्र हो इसे मार डालो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2324)
- **Original**: तुम उसे उसके ब्रिना जाने समस्त स्वाद्मपदार्थोर्मे हल्लाहल त्रिष मिल्त्रकर दो और किसी प्रकारका शोच-लिचार न कर उस पापीको मार डाल्मे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2325)
- **Original**: श्रीपराहस्जी कोले--ठब उन रसोइयोने महात्मा प्रद्मादको, जैसी कि उनके पिताने आज्ञा दी थी डसीके अनुसार बिष दे दिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2326)
- **Original**: हे मैत्रेय
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2327)
- **Original**: तब वे उस घोर हलाहल विषको भगबज्नामके ठन्चारणसे अभिमन्त्रित कर अन्नके साथ स्वरा गये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2328)
- **Original**: तथा भगवनज्नामके प्रभावसे निस्तेज हुए उस विषको खाकर उसे बिना किसी तिकारके पचाकर स्वस्थ चित्तसे स्थित रहे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2329)
- **Original**: उस महान्‌ विषको पचा छुआ देख रसोइयोंने भयसे व्याकुछ हो हिरण्यकशिपुके पास जा उसे प्रणाम करके कहा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2330)
- **Original**: सुदगण बोले--हे दैत्यराज ! हमने आपकी आज्ञासे अत्यज्त तीक्ष्ण विष दिया था, तथापि आपके पुत्र अह्ादने उसे अन्नके साथ पथा लिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2331)
- **Original**: हिरण्यकशिपु खोला--हे पुरोहितगण ! झीघ्रता करो, शीघ्रता करो ! उसे नष्ट करनेके लिये अब कृत्या उत्पन्न करो; और देरी न करो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2332)
- **Original**: श्रीपराह्यरजी बोलले---तब पुरोहितोनि अति विनीत प्रह्मादसे, उसके पास जाकर शात्तिपूर्वक कहा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2333)
- **Original**: पुरोहित खोले--हे आयुष्मन्‌ ! तुम ब्रिलोकीमें बिख्यात गह्याजीके कुछमें उत्पन्न हुए हो और दैत्यराज हिरण्यकहिपुके पुत्र हो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2334)
- **Original**: तुम्हें देवता अनन्त अथवा और भी किसीसे क्‍या प्रयोजन है ? तुम्हारे पिता तुम्हारे तथा सम्पूर्ण स्प्रेकोंके आश्रय हैं और तुम भी ऐसे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2335)
- **Original**: डे तस्मात्परित्यजैनां त्व॑ विपक्षस्तवसंहिताम्‌। इलाघ्य: पिता समस्तानां गुरूणां परमो गुरु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2336)
- **Original**: 13 एबपेतन्म्हाभागा: इलाध्यमेतन्महाकुलम्‌। मरीचे: सकलेउप्यस्मिन जैल्मेक्ये नान्यथा वदेत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2337)
- **Original**: 14 पिता च मम सर्वस्मिश्जगत्युत्कृष्टचेष्टित: । एतदष्यवगच्छामि सत्यमत्रापि नानृतम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2338)
- **Original**: 15 गुरूणामपि सर्वेधा पिता परमको गुरु: । यतुक्त भ्रान्तिस्तत्रापि स्वल्पापि हि न विद्यते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2339)
- **Original**: 16 तत्रापि नापराध्यामीत्येब॑ मनसि मे स्थितम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2340)
- **Original**: 17 यक्वेतत्किमनन्तेनेत्युक्ते युष्माभिरीदृशम्‌ । को ब्रवीति यथान्याय्य॑ कि तु नैतद्वचो3र्थवत्‌
- **Translation**: 

---

